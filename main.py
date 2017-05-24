import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
# import math

#Variables
tsegment = 20e-3 #20ms segment
overlap = 0.5

#Import data & fs
data, fs = sf.read('Audio/clean.wav')

# Calc
s_segment = int(tsegment * fs)
s_overlap = int(overlap * s_segment)
# pad data with zeros
remainder = s_segment - (len(data) % s_segment)
data_extended = np.ravel(np.asmatrix(np.pad(data, (0, int(remainder)), 'constant')))



# #Calc
# s_segment = int(tsegment*fs)
# s_overlap = int(overlap*s_segment)
#
#
# #pad data with zeros
# remainder = s_segment - (len(data) % s_segment)
# data_extended = np.ravel(np.asmatrix(np.pad(data,(0,int(remainder)),'constant')))
#
# #calculate number of frames
# num_frames = int((len(data_extended)-s_overlap)/s_overlap)
#
# #init matrix
# x = np.matrix(np.zeros([num_frames,s_segment]))
# for i in range(0,num_frames):
#     x[i, :] = data_extended[i*s_overlap:i*s_overlap+s_segment]
#
# #transform back into array
# x_array = np.ravel(x)


#Making functions
def segment_overlap(data_extended,s_segment,s_overlap):
    # calculate number of frames
    num_frames = int((len(data_extended) - s_overlap) / s_overlap)

    # init matrix
    x = np.matrix(np.zeros([num_frames, s_segment]))
    for i in range(0, num_frames):
        x[i, :] = data_extended[i * s_overlap:i * s_overlap + s_segment]

    # transform back into array
    x_array = np.ravel(x)
    return x_array

def inverse_segment_overlap(x_array,len_data_extended,s_segment,s_overlap):
    new_frames = int(len_data_extended/ s_segment)
    # init matrix
    x_trunc = np.matrix(np.zeros([new_frames, s_segment]))
    for j in range(0, new_frames):
        x_trunc[j, :] = x_array[j * (2 * s_segment):j * (2 * s_segment) + s_segment]
    # transform back into array
    x_truncarray = np.ravel(x_trunc)
    return x_truncarray

x_array = segment_overlap(data_extended,s_segment,s_overlap)
x_truncarray = inverse_segment_overlap(x_array,len(data_extended),s_segment,s_overlap)

#calculate difference between initial and reconstructed signals
residual = data_extended - x_truncarray


#Plots
f, axarr = plt.subplots(3, sharex=True)
axarr[2].plot(residual)
axarr[2].set_title('Residual')
axarr[1].plot(x_truncarray)
axarr[1].set_title('Reconstructed')
axarr[0].plot(data_extended)
axarr[0].set_title('Original')

#########
#Reverse#
#########
#
# new_frames = int(len(data_extended)/s_segment)
# #init matrix
# x_trunc = np.matrix(np.zeros([new_frames,s_segment]))
# for j in range(0,new_frames):
#     x_trunc[j, :] = x_array[j*(2*s_segment):j*(2*s_segment)+s_segment]
#
# #transform back into array
# x_truncarray = np.ravel(x_trunc)
#
# #calculate difference between initial and reconstructed signals
# residual = data_extended - x_truncarray
#
#
# #Plots
# f, axarr = plt.subplots(3, sharex=True)
# axarr[2].plot(residual)
# axarr[2].set_title('Residual')
# axarr[1].plot(x_truncarray)
# axarr[1].set_title('Reconstructed')
# axarr[0].plot(data_extended)
# axarr[0].set_title('Original')


end = 1




