import librosa
import speech_recognition as sr
r = sr.Recognizer()

sample_wav, rate = librosa.core.load(
    'stt/sample.wav')

korean_audio = sr.AudioFile(
    'stt/sample.wav')

with korean_audio as source:
    audio = r.record(source)
r.recognize_google(audio_data=audio, language='ko-KR')
