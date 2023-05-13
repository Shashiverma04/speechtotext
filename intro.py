import speech_recognition as sr

reco=sr.Recognizer()
# reco.recognize_google()


Audiofile=sr.AudioFile('Audios.wav')
with Audiofile as source:
    audio=reco.record(source)

    query=reco.recognize_google(audio)
    print(query)
# type(audio)