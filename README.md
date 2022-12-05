## Text-to-Speech (TTS)
**Text-to-Speech** from `.xlsx` files and generate `.mp3` or `.wav` audio files using `python`. This program uses api from [Google Translate](https://translate.google.com/) for tts. You can also choose `gTTs` python library.

### Procedures
1. ```git clone```
2. Provide the directory path of `.xlsx`, `.mp3` and `.wav` files through input. You can hit `Enter` to use default path (default: `{project-path}/files/{xlsx & mp3 & wav}`).
3. Run the program and get your output in folder (mp3 or wav).

### Requirements
1. If you're using **linux/osx**, make sure `ffmpeg` installed in system.
2. `openpyxl`
3. `pydub`
4. `gTTs`
