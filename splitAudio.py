from mutagen.mp3 import MP3

from pydub import AudioSegment
import subprocess

audio = MP3(".\\121326.mp3")
print(audio.info.length)

sound = AudioSegment.from_mp3(".\\121326.mp3")
'''
# len() and slicing are in milliseconds
halfway_point = len(sound) / 2
second_half = sound[halfway_point:]

# Concatenation is just adding
second_half_3_times = second_half + second_half + second_half

# writing mp3 files is a one liner
second_half_3_times.export("./output/test.mp3", format="mp3")
'''

# Input file name
input_file = "./121326.mp3"
output_format = "mp3"
# Output file name template
output_file_template = "output_{0}.mp3"

# Duration of each segment (in seconds)
segment_duration = 600

# Run FFmpeg command to split the file
#subprocess.call(['ffmpeg', '-i', input_file, '-f', 'segment', '-segment_time', str(segment_duration), '-c', 'copy', output_file_template])


# Get the duration of the input file using ffprobe
ffprobe_cmd = f"ffprobe -i {input_file} -show_entries format=duration -v quiet -of csv='p=0'"
#duration = float(subprocess.check_output(ffprobe_cmd, shell=True))
duration = audio.info.length
# Split the input file into segments
for i in range(int(duration // segment_duration)):
    segment_start_time = i * segment_duration
    segment_file = f"segment_{i:02d}.{output_format}"
    ffmpeg_cmd = f"ffmpeg -i {input_file} -ss {segment_start_time} -t {segment_duration} -c copy {segment_file}"
    subprocess.call(ffmpeg_cmd, shell=True)