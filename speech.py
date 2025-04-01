import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Use the audio file as the source
with sr.AudioFile("output_file.wav") as source:
    audio = recognizer.record(source)

# Recognize speech using Google Speech Recognition
try:
    text = recognizer.recognize_google(audio, language="ru-RU")  # Use "ru-RU" for Russian
    # Write the output to a file with UTF-8 encoding (ensures the file can handle Russian/Cyrillic characters)
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(f"Texto reconhecido: {text}")
    print("Output written to output.txt")
except sr.UnknownValueError:
    print("Google Speech Recognition não entendeu o áudio.")
except sr.RequestError:
    print("Não foi possível solicitar resultados do Google Speech Recognition.")