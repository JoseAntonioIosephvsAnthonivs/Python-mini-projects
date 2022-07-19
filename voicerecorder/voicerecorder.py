import sounddevice 
from scipy.io.wavfile import write 
fs = 44100
second = int(input("Enter Recording Time in second: "))

print("Recording...\n")

record_voice = sounddevice.rec(int(second * fs), samplerate = fs, channels = 2)

sounddevice.wait()

write("MyRecording.wav", fs, record_voice)
print("Recorind is done Please check your folden to linsten recording")
