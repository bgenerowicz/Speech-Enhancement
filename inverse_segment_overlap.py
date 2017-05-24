import numpy as np
def inverse_segment_overlap(x_array,len_data_extended,s_segment,s_overlap):
    new_frames = int(len_data_extended/ s_segment)
    # init matrix
    x_trunc = np.matrix(np.zeros([new_frames, s_segment]))
    for j in range(0, new_frames):
        x_trunc[j, :] = x_array[j * (2 * s_segment):j * (2 * s_segment) + s_segment]
    # transform back into array
    x_truncarray = np.ravel(x_trunc)
    return x_truncarray