# https://github.com/minkukjo/CapstoneDesign2/blob/python-client/sound_recorder.py
# https://gist.github.com/mabdrabo/8678538

import pyaudio
import wave


def record_sound():
    FORMAT = pyaudio.paInt16
    CHANNELS = 1 #only mono
    RATE = 16000
    CHUNK = 1024 # 스트림에서 읽는 프레임의 샘플 수
    RECORD_SECONDS = 3 #3초 녹음

    WAVE_OUTPUT_FILENAME = "file.wav"
    audio = pyaudio.PyAudio()

    # start Recording
    stream = audio.open(
        format=FORMAT, channels=CHANNELS,
        rate=RATE, input=True,
        frames_per_buffer=CHUNK
    )
    print ("recording...")

    frames = []
    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print ("finished recording")

    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

