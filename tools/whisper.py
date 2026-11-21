"""Transcribe uncaptioned lectures locally with faster-whisper (CPU int8; the MX150 GPU has too
little memory). Writes materials/transcripts/raw/CCC-<id>.whisper.txt as 'seconds<TAB>text' lines
(CCC = chapter number, taken from the file name), which tools/transcripts.py turns into CXX-VYY.txt.
Run: python -I -X utf8 tools/whisper.py materials/audio/001-wEI5Mm4P21M.webm [more files]
"""
import os, sys, time
from pathlib import Path
import av
import numpy as np
from faster_whisper import WhisperModel

ROOT = Path(__file__).resolve().parent.parent


def decode(path):
    """16 kHz mono float32 (the installed PyAV is older than faster-whisper's own decoder expects)."""
    with av.open(str(path)) as c:
        rs = av.AudioResampler(format='s16', layout='mono', rate=16000)
        out = [f.to_ndarray() for fr in c.decode(audio=0) for f in rs.resample(fr)]
    return np.concatenate(out, axis=1).flatten().astype(np.float32) / 32768.0


def language(chapter):
    return 'de' if chapter <= 20 else 'en'


# large-v3 on this CPU runs at ~0.25x real time (~7 h per lecture); distil-large-v3 is English only and much
# faster. Override with WHISPER_MODEL=<name>. Default: large-v3 for German, distil-large-v3 for English.
DEFAULT_MODEL = {'de': 'large-v3', 'en': 'distil-large-v3'}
# Names the model tends to mishear; whisper uses the prompt as preceding context.
PROMPTS = {'de': 'Vorlesung von Frederic Schuller, Theoretische Quantenmechanik: Hilbertraum, Spektralsatz, Pfadintegral, Schrödingergleichung, '
       'Dirac, Hamiltonoperator, Clebsch-Gordan, Wasserstoffatom, Banach, Lebesgue.',
       'en': 'Lecture by Frederic Schuller on quantum theory: Banach spaces, Hilbert spaces, measure theory, Lebesgue, '
       'self-adjoint operators, spectral theorem, Stone, Schrödinger, Fourier, Bloch.'}
models = {}
for a in sys.argv[1:]:
    a = Path(a)
    lang = language(int(a.stem.split('-')[0]))
    name = os.environ.get('WHISPER_MODEL', DEFAULT_MODEL[lang])
    if name not in models:
        models[name] = WhisperModel(name, device='cpu', compute_type='int8', cpu_threads=8)
    t0 = time.time()
    segs, _ = models[name].transcribe(decode(a), language=lang, vad_filter=True, initial_prompt=PROMPTS[lang])
    out = ROOT / 'materials/transcripts/raw' / (a.stem + '.whisper.txt')
    with open(out, 'w', encoding='utf-8') as f:
        for s in segs:
            f.write(f'{int(s.start)}\t{s.text.strip()}\n')
            f.flush()
    print(out.name, f'{(time.time() - t0) / 60:.0f} min')
