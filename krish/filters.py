from scipy.fft import fft, ifft, fftfreq
from scipy.signal import butter, filtfilt,cheby1, lfilter, freqz
import numpy as np
#===========================================================================
#===========================================================================

def fft_based_filter(acceleration,sampling_rate,low_cut,high_cut):
    T = 1.0 / sampling_rate  # Sample interval
    # Perform FFT
    fft_result = fft(acceleration)
    fft_freqs = fftfreq(len(acceleration), T)
    # Create a mask for the desired frequency range
    mask = (np.abs(fft_freqs) >= low_cut) & (np.abs(fft_freqs) <= high_cut)

    # Filter the FFT results using the mask
    filtered_fft_result = fft_result * mask

    # Perform IFFT on the filtered FFT results
    filtered_ifft_result = ifft(filtered_fft_result)
    return filtered_ifft_result

#===========================================================================
#===========================================================================

def butterworth_filter(acceleration,sampling_rate,low_cut,high_cut,order=4):
    """
    Apply a Butterworth band-pass filter to the given signal.

    Parameters:
    - signal: The input signal to be filtered.
    - sampling_rate: The sampling rate of the signal (Hz).
    - low_freq: The lower cutoff frequency of the band-pass filter (Hz).
    - high_freq: The upper cutoff frequency of the band-pass filter (Hz).
    - order: The order of the filter (default is 4).

    Returns:
    - filtered_signal: The filtered signal.
    """
    T = 1.0 / sampling_rate  # Sample interval
    # Design a Butterworth band-pass filter
    nyquist = 0.5 * sampling_rate
    low = low_cut / nyquist
    high = high_cut / nyquist
    b, a = butter(order, Wn=[low, high], btype='band')

    # Apply the filter to the signal
    filtered_signal = filtfilt(b, a, acceleration)

    return filtered_signal

#===========================================================================
#===========================================================================


def chebyshev_filter(signal, fs, cutoff, order=4, rp=0.05, btype='high'):
    """
    Apply a Chebyshev Type I filter to a signal.

    Parameters:
    - signal: The input signal (1D array).
    - fs: Sampling frequency of the signal (Hz).
    - cutoff: Desired cutoff frequency (Hz).
    - order: Order of the filter (default is 4).
    - rp: Maximum ripple in the passband (default is 0.05 dB).
    - btype: Type of the filter ('low', 'high', 'bandpass', 'bandstop').

    Returns:
    - filtered_signal: The filtered signal (1D array).
    """
    nyq = 0.5 * fs  # Nyquist frequency
    normalized_cutoff = cutoff / nyq  # Normalized cutoff frequency
    
    # Design the Chebyshev Type I filter
    b, a = cheby1(order, rp, normalized_cutoff, btype=btype, analog=False)
    
    # Apply the filter to the signal
    filtered_signal = lfilter(b, a, signal)
    
    return filtered_signal, b, a