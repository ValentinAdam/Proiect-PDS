import numpy as np
from scipy.io import wavfile
import time

# Define optimization flags
np.seterr(all='ignore')
np.use_fastnumpy = True

def apply_audio_effect(input_audio, delay, decay):
    output_audio = np.zeros_like(input_audio, dtype=np.float32)
    
    for i in range(len(input_audio)):
        if i - delay >= 0:
            output_audio[i] = input_audio[i] + decay * output_audio[i - delay]
    
    return output_audio

def apply_echo_reverberation(input_file, echo_output_file, reverberation_output_file, echo_delay, echo_decay, reverberation_delay, reverberation_decay):
    # Read the audio file
    sample_rate, audio_data = wavfile.read(input_file)

    # Convert stereo audio to mono by taking the average of the two channels
    if audio_data.ndim == 2:
        audio_data = audio_data.mean(axis=1)

    # Apply the echo effect and measure execution time
    start_time = time.time()
    echo_audio = apply_audio_effect(audio_data, echo_delay, echo_decay)
    echo_time = time.time() - start_time

    # Apply the reverberation effect and measure execution time
    start_time = time.time()
    reverberation_audio = apply_audio_effect(audio_data, reverberation_delay, reverberation_decay)
    reverberation_time = time.time() - start_time

    # Normalize the audio to prevent clipping
    echo_audio = np.int16(echo_audio / np.max(np.abs(echo_audio)) * 32767)
    reverberation_audio = np.int16(reverberation_audio / np.max(np.abs(reverberation_audio)) * 32767)

    # Save the output audio to separate WAV files for echo and reverberation
    wavfile.write(echo_output_file, sample_rate, echo_audio)
    wavfile.write(reverberation_output_file, sample_rate, reverberation_audio)

    return echo_time, reverberation_time

if __name__ == "__main__":
    input_file = "yiruma.wav"
    echo_output_file = "yiruma_echo_v4.wav"
    reverberation_output_file = "yiruma_reverberation_v4.wav"
    echo_delay = 10000  # Adjust the echo delay in samples
    echo_decay = 0.5   # Adjust the echo decay factor
    reverberation_delay = 20000  # Adjust the reverberation delay in samples
    reverberation_decay = 0.7  # Adjust the reverberation decay factor

    # Measure the execution time for applying echo and reverberation effects
    echo_time, reverberation_time = apply_echo_reverberation(input_file, echo_output_file, reverberation_output_file, echo_delay, echo_decay, reverberation_delay, reverberation_decay)

    print("Echo effect saved to:", echo_output_file)
    print("Reverberation effect saved to:", reverberation_output_file)
    print("Echo execution time: {:.6f} seconds".format(echo_time))
    print("Reverberation execution time: {:.6f} seconds".format(reverberation_time))
