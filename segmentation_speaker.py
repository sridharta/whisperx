import subprocess
from pyAudioAnalysis import audioSegmentation as aS
import numpy as np
input_file = "processAudio.wav"
segment_duration = 10  # in seconds
duration = 1698
# Split the input file into segments
for i in range(int(duration // segment_duration)):
    segment_start_time = i * segment_duration
    segment_file = f"./output/segment_{i:02d}.wav"
    ffmpeg_cmd = f"ffmpeg -i {input_file} -ss {segment_start_time} -t {segment_duration} -vn -acodec copy {segment_file}"
    subprocess.call(ffmpeg_cmd, shell=True)
    print(segment_file)
    print(type(segment_file))
    # Detect speaker change using VAD

    np.seterr(divide='ignore', invalid='ignore') # disables the warning
    segment = int(aS.speaker_diarization(segment_file, "svm", False))
    # The speaker_diarization function returns a list of (speaker_label, segment_duration) tuples

    # Print the speaker labels and durations for each segment
    for speaker, duration in segment:
        print(f"Speaker {speaker}: {duration:.2f} seconds")