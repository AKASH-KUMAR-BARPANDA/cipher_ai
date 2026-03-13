import sounddevice as sd
import numpy as np
from openwakeword import Model
from faster_whisper import WhisperModel
from core.command_router.router import route_command
import time
import warnings
warnings.filterwarnings('ignore')

SAMPLE_RATE = 16000
CHUNK_SIZE = 1280
LISTENING_COMMAND = False


model = Model()
Speech_to_text = WhisperModel('base.en',device='cpu',compute_type='int8')

print("--"*50)
print("\nCipher AI is listening... Say \"ALEXA\" .")

def record_command():
    print("Listening for command...")

    duration = 4

    audio = sd.rec(int(duration * SAMPLE_RATE),
                   samplerate=SAMPLE_RATE,channels=1,
                   dtype='int16',)

    sd.wait()

    print("Recording finished")

    audio_np = audio.flatten().astype(np.float32) / 32768.0

    segments,info = Speech_to_text.transcribe(audio_np)

    print("Transcribing...")
    
    text = ""
    for segment in segments:
        text = text + segment.text
    
    route_command(text.strip())

def audio_callback(indata,frame,time,status):

    global LISTENING_COMMAND

    if LISTENING_COMMAND:
        return
    
    audio = np.frombuffer(indata,dtype=np.int16)
    prediction = model.predict(audio)

    for wake_word, score in prediction.items():
        if score > 0.8 and wake_word == 'alexa' and not LISTENING_COMMAND:
            print(f"Wake word detected: {wake_word} (score={score:.2f})")
            print("Cipher AI activated.....")
            LISTENING_COMMAND = True


with sd.RawInputStream(
    samplerate=SAMPLE_RATE,
    blocksize=CHUNK_SIZE,
    dtype='int16',channels=1,
    callback=audio_callback) as stream:
    while True:
        if LISTENING_COMMAND:
            stream.stop()
            record_command()
            LISTENING_COMMAND = False
            print("Cleaning up audio buffer...")
            time.sleep(1.5)
            print("--"*50)
            print("\nCipher AI is listening... Say \"ALEXA\" .")
            stream.start()