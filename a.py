import matplotlib.pyplot as plt
from scipy.signal import butter,filtfilt,find_peaks
import numpy as np

def bandpass(lowcut,highcut,fs,order=1):
    nyq=0.5*fs
    low=lowcut/nyq
    high=highcut/nyq
    b,a=butter(order,[low,high],btype='band')
    return b,a

def bandpassfilter(data,lowcut,highcut,fs,order=1):
    b,a=bandpass(lowcut,highcut,fs,order=1)
    y=filtfilt(b,a,data)
    return y

def notch(lowcut,highcut,fs,order=3):
    nyq=0.5*fs
    low=lowcut/nyq
    high=highcut/nyq
    b,a=butter(order,[low,high],btype='bandstop')
    return b,a


def notch_filter(data,lowcut,highcut,fs,order=1):
    b,a=notch(lowcut,highcut,fs,order=order)
    y=filtfilt(b,a,data)
    return y

def lowpass(cutoff,fs,order=1):
    nyq=0.5*fs
    normal_cutoff=cutoff/nyq
    b,a=butter(order,normal_cutoff,btype='low',analog=False)
    return b,a

def lowpass_filter(data,cutoff,fs,order=1):
    b,a=lowpass(cutoff,fs,order=order)
    y=filtfilt(b,a,data)
    return y

def highpass(cutoff,fs,order=1):
    nyq=0.5*fs
    normal_cutoff=cutoff/nyq
    b,a=butter(order,normal_cutoff,btype='high',analog=False)
    return b,a

def highpass_filter(data,cutoff,fs,order=1):
    b,a=highpass(cutoff,fs,order=order)
    y=filtfilt(b,a,data)
    return y

with open("7.txt","r") as file:
    
    raw_data=file.readlines()
    
    ppg_data=[]
    for i in raw_data:
        ppg_data.append(float(i[:-2]))
        
    size=len(ppg_data)
    time=int((size/1000)/60)
    
data=ppg_data[:5000]
data=np.array(data)  
f_data=lowpass_filter(data,1,1000,1)
peak,v=find_peaks(data,height=0)
  
plt.subplot(2,1,1)
plt.plot(data)

plt.subplot(2,1,2)       
plt.plot(data)
plt.plot(peak,data[peak],"x")

plt.show()


import tensorflow
