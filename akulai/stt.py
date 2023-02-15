import vosk
import os

def recognize_speech():
    model = vosk.Model("model")
    sample_rate = 16000
    rec = vosk.KaldiRecognizer(model, sample_rate)
    rec.SetWords(True)

    os.system("arecord -D hw:1,0 -r 16000 -c 1 -t wav -d 5 -f S16_LE temp.wav")
    with open("temp.wav", "rb") as f:
        data = f.read()

    if rec.AcceptWaveform(data):
        result = rec.Result()
        return result.split('"text": "')[1].split('"')[0]

    return ""
