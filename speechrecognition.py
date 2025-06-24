import speech_recognition as sr 
import sounddevice as sd 
import numpy as np 

# function untuk merekam suara dengan sounddevice
def record_audio(duration=5, fs=16000):
    print("Mendengarkan..")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait() # menunggu sampai rekaman selesai
    return audio, fs

# function untuk mengenali suara
def recognize_audio(audio_data, sample_rate):
    recognizer = sr.Recognizer()
    audio = sr.AudioData(np.array(audio_data), sample_rate, 2)

    try:
        text = recognizer.recognize_google(audio, language="id-ID")
        print("Kamu berkata: " + text)
        return text.lower()
    except sr.UnknownValueError:
        print("Maaf, tidak bisa memahami suara kamu")
        return ""
    except sr.RequestError as e:
        print(f"Maaf, sepertinya terjadi kesalahan dalam permintaan ke API Google: {e}")
        return ""

# loop untuk terus menjalankan program hingga user mengatakan 'quit'
print("Selamat datang! Katakan sesuatu atau 'quit' untuk mengakhiri sesi")
while True:
    audio_data, sample_rate = record_audio()
    spoken_text = recognize_audio(audio_data, sample_rate)

    if spoken_text == 'quit':
        print("Mengakhiri percakapan")
        break