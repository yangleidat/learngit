import os, wave, Scrapy
import numpy as np

def wav2pcm(wav_file):
    f = open(wav_file)
    f.seek(0)
    f.read(44)
    data = np.fromfile(f, dtype = np.int16)
    data.tofile("test.pcm")

def pcm2wav(pcm_file, wav_file):
    f = open(pcm_file,'rb')
    str_data  = f.read()
    wave_out=wave.open(wav_file,'wb')
    wave_out.setnchannels(1)
    wave_out.setsampwidth(2)
    wave_out.setframerate(8000)
    wave_out.writeframes(str_data)

wav2pcm('D:\myCode\myPythonCode\API\\baidu\yuyin2wenzi\public\\test1.wav')