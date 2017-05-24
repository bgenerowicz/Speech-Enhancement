import numpy as np
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