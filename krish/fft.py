from scipy.fft import fft, ifft, rfft, irfft, fftfreq, rfftfreq
import numpy as np

def compute_fft(acceleration,sampling_rate):
    ## time as Time is second
    ## acc as Acceleration data
    ## sampling_rate as sampling rate
    T = 1.0 / sampling_rate 

    # Perform FFT
    fft_result = fft(acceleration)
    fft_freqs = fftfreq(len(acceleration), T)

    return fft_result, fft_freqs
    
def compute_rfft(acceleration,sampling_rate):
    ## time as Time is second
    ## acc as Acceleration data
    ## sampling_rate as sampling rate
    T = 1.0 / sampling_rate 

    # Perform FFT
    rfft_result = rfft(acceleration)
    rfft_freqs = rfftfreq(len(acceleration), T)

    return rfft_result, rfft_freqs

def split_fft(fft_result, fft_freqs,low_freq,high_freq):
    # Create a mask for the desired frequency range
    mask = (np.abs(fft_freqs) >= low_freq) & (np.abs(fft_freqs) <= high_freq)

    # Filter the FFT results using the mask
    filtered_fft_result = fft_result * mask

    return filtered_fft_result

def compute_ifft()