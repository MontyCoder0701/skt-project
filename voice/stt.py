import requests
import sys
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


client_id = "id 입력"
client_secret = "비번 입력"
lang = "Kor"  # 언어 코드 ( Kor, Jpn, Eng, Chn )
url = "https://naveropenapi.apigw.ntruss.com/recog/v1/stt?lang=" + lang
data = open('stt/sample.mp3', 'rb')
headers = {
    "X-NCP-APIGW-API-KEY-ID": client_id,
    "X-NCP-APIGW-API-KEY": client_secret,
    "Content-Type": "application/octet-stream"
}
response = requests.post(url,  data=data, headers=headers)
rescode = response.status_code
if (rescode == 200):
    print(response.text)
else:
    print("Error : " + response.text)
