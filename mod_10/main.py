import pyaudio
import wave
import speech_recognition as sr
import subprocess
from commands import Commander

def say(text):
    subprocess.call('say ' + text, shell=True)

def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename,'rb')
    pa = pyaudio.PyAudio()

    stream = pa.open(
        format=pa.get_format_from_width(wf.getsamwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
        )

    data_stream = wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()

r = sr.Recognizer()
cmd = Commander()
running = True

def initSpeech():
    print('Listening....')
    play_audio('light.wav')

    with sr.Microphone() as source:
        print('Say Something')
        audio = r.listen(source)

    play_audio('light.wav')

        command = ""
        try:
            command = r.recognize_google(audio)
        except:
            print('Could not understand')

        print('Your Command : {}'.format(command))
        #say('You said: ' + command)

        if command in ['quit','exit','bye','goodbye']:
            global running
            running = False

        cmd.discover(command)

while running = True:
    initSpeech()
