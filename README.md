# Quantum Theory (Schuller): lecture notes

LaTeX study notes of Frederic P. Schuller's two quantum-mechanics courses at FAU Erlangen, 41 lectures, 70.9 h:
one chapter per lecture, every point linked to the second of the video where it is said.

- **Part I (ch. 1-20)**: *Theoretische Physik 2: Theoretische Quantenmechanik* (TP-2, WS 2014/15, German, 20 lectures, physics first:
  experimentum crucis, path integral, wave functions, rigged Hilbert spaces, hydrogen). YouTube only for lectures 1-11,
  [FAU.tv](https://www.fau.tv/series/theoretische-physik-2-theoretische-quantenmechanik-tp-2-w14) for all 20.
- **Part II (ch. 21-41)**: *Lectures on Quantum Theory* (SS 2015, English, 21 lectures, maths first: Banach spaces, measure theory,
  self-adjoint operators, Stone, Fourier operator, perturbation theory). [YouTube playlist](https://www.youtube.com/playlist?list=PLPH7f_7ZlzxQVx5jRjbfRGEzWY_upS5K6),
  [FAU.tv](https://www.fau.tv/series/lectures-on-quantum-theory-elite-graduate-programme-2015-measurements-s15).
- Build: `cd lecture-notes && python build.py all` (latexmk + scroll book `build/book.pdf`).
- Transcripts: `python -I -X utf8 tools/transcripts.py` turns YouTube captions or whisper output in
  `materials/transcripts/raw/` into `materials/transcripts/CXX-VYY.txt` (C = chapter, V = video of the chapter);
  `tools/whisper.py` transcribes lectures without captions. `materials/` is gitignored (third-party material, never committed).

## Backup sources (checking only, never copied)
- Backup notes (checking only, never copied): Simon Rea and Richie Dadhley, *Lectures on Quantum Theory* [PDF](https://tales.mbivert.com/Lectures_on_Quantum_Theory_complete.pdf), LaTeX [sreahw/schuller-quantum](https://github.com/sreahw/schuller-quantum); Apoorv Potnis, lecture 8 of TP-2 [apoorvpotnis/schuller_rigged_hilbert_spaces](https://github.com/apoorvpotnis/schuller_rigged_hilbert_spaces). No licence stated on any of them: all rights reserved.

Full inventory of Schuller's material: `../lecture-notes-schuller-courses/SOURCES.md` (local).
All rights on the lectures belong to their authors; these are personal, non-commercial study notes.
