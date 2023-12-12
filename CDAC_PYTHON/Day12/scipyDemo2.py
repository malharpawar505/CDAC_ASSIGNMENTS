import matplotlib.pyplot as plt
import numpy as np
from scipy.io.wavfile import read #import the required function from the module
samplerate, data = read(r'C:\Snehal\CDAC\Sept 23\DBDA\Python\PythonProgs\Day12\Ring10.wav')
print(samplerate) #echo samplerate
print(data) #echo data -> note that the data is a single dimensional array


duration = len(data)/samplerate

time = np.arange(0,duration,1/samplerate) #time vector


plt.plot(time,data)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('CantinaBand3.wav')
plt.show()

