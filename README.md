# 🎙️ Audio Transcription Tool  

A Python script for transcribing audio files using Google Speech Recognition API.  

---

## 🛠️ Setup  

### 1️⃣ Install Requirements  
```bash
# Install Python package
pip install SpeechRecognition

# Manual FFmpeg install:
# 1. Download from ffmpeg.org (Windows build)
# 2. Extract zip folder
# 3. Add the 'bin' folder path to System Environment Variables
# 4. Verify with: ffmpeg -version
```  

### 2️⃣ Convert Audio (MP4 → WAV)  
```bash
ffmpeg -i input.mp4 -vn -ar 16000 output_file.wav
```
| Parameter    | Description                                  |
|-------------|----------------------------------------------|
| `-vn`       | Disables video stream                       |
| `-ar 16000` | Sets audio sample rate to 16kHz (optimal for speech) |  

### 3️⃣ Configure Language  
Edit `transcribe.py`:  
```python
text = recognizer.recognize_google(audio, language="ru-RU")  # Change language code
```
#### Common language codes:  
| Code      | Language      |
|-----------|--------------|
| `en-US`   | English (US)  |
| `es-ES`   | Spanish       |
| `fr-FR`   | French        |
| `ja-JP`   | Japanese      |
| `pt-BR`   | Portuguese    |  

🔗 [Full language support](https://cloud.google.com/speech-to-text/docs/languages)  

### 4️⃣ Run Transcription  
```bash
python transcribe.py
```  
➡️ Output saves to `output.txt` (UTF-8 encoded)  

---

## ⚠️ Limitations  
- ▶️ Max 60s audio (Google free tier)  
- 🌐 Internet connection required  
- 🎙️ Accuracy varies with audio quality  
- 💬 Best for clear speech (no heavy accents)  

---
