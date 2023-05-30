from pydub import AudioSegment
from pydub.silence import split_on_silence

def convertToWave(mp3file):
    sound = AudioSegment.from_mp3(mp3file)
    sound.export("processAudio.wav", format="wav")


input_file = "./121326.mp3"
convertToWave(input_file)
min_silence_len = 1000  # in milliseconds
silence_thresh = -50  # in decibels
segment_duration = 10  # in seconds

# Open the audio file using pydub
audio = AudioSegment.from_file("processAudio.wav", format="wav")

# Find the silence duration after the 10th second
start_time = segment_duration * 1000  # in milliseconds
end_time = len(audio)
silence_chunks = split_on_silence(audio[start_time:end_time], 
                                  min_silence_len=min_silence_len, 
                                  silence_thresh=silence_thresh)

# Split the audio file into segments based on the silence duration
for i, chunk in enumerate(silence_chunks):
    segment_file = f"segment_{i:02d}.wav"
    chunk.export("./output/"+segment_file, format="wav")
