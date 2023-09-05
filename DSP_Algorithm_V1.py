import numpy as np
from scipy.io import wavfile
import time

def apply_echo_reverberation(input_file, echo_output_file, reverberation_output_file, delay, decay):
    # Read the audio file
    sample_rate, audio_data = wavfile.read(input_file)

    # Create empty arrays for echo and reverberation outputs
    echo_audio = np.zeros_like(audio_data, dtype=np.float32)
    reverberation_audio = np.zeros_like(audio_data, dtype=np.float32)

    # Measure the execution time for applying the echo effect
    start_time = time.time()
    for i in range(len(audio_data)):
        if i - delay >= 0:
            echo_audio[i] = audio_data[i] + decay * audio_data[i - delay]
    echo_execution_time = time.time() - start_time

    # Measure the execution time for applying the reverberation effect
    start_time = time.time()
    for i in range(len(audio_data)):
        if i - delay >= 0:
            reverberation_audio[i] = audio_data[i] + decay * reverberation_audio[i - delay]
    reverberation_execution_time = time.time() - start_time

    # Normalize the audio to prevent clipping
    echo_audio = np.int16(echo_audio / np.max(np.abs(echo_audio)) * 32767)
    reverberation_audio = np.int16(reverberation_audio / np.max(np.abs(reverberation_audio)) * 32767)

    # Save the output audio to separate WAV files for echo and reverberation
    wavfile.write(echo_output_file, sample_rate, echo_audio)
    wavfile.write(reverberation_output_file, sample_rate, reverberation_audio)

    return echo_execution_time, reverberation_execution_time

if __name__ == "__main__":
    input_file = "yiruma.wav"
    echo_output_file = "yiruma_echo_v1.wav"
    reverberation_output_file = "yiruma_reverberation_v1.wav"
    delay = 10000  # Adjust the delay in samples
    decay = 0.5   # Adjust the decay factor

    echo_time, reverberation_time = apply_echo_reverberation(input_file, echo_output_file, reverberation_output_file, delay, decay)
    print("Echo effect saved to:", echo_output_file)
    print("Reverberation effect saved to:", reverberation_output_file)
    print(f"Echo execution time: {echo_time:.6f} seconds")
    print(f"Reverberation execution time: {reverberation_time:.6f} seconds")
