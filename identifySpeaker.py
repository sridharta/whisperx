import librosa
import pyannote.audio as pa
from speaker_recognition import SpeakerRecognition

# Load the audio file and resample it to a consistent sample rate
audio_file = '121326.mp3'
sr = 16000
audio, _ = librosa.load(audio_file, sr=sr)

# Segment the audio into homogeneous segments corresponding to individual speakers
diarization = pa.SpeakerDiarization(
    sad=pa.MAAP(),
    scd=pa.USE(),
    embedding=pa.TV,
    similarity=pa.CLS,
    threshold=0.5)
segments = diarization(audio)

# Extract speaker-specific features from each segment
features = []
for segment in segments:
    segment_audio = segment.crop(audio)
    feature = extract_features(segment_audio)
    features.append(feature)

# Identify each speaker based on their extracted features
model_file = 'path/to/speaker_model.pkl'
sr = SpeakerRecognition(model_file)
speakers = sr.identify(features)

# Associate each speaker segment with the corresponding identified speaker
results = []
for i, segment in enumerate(segments):
    speaker = speakers[i]
    start, end = segment.start, segment.end
    results.append((start, end, speaker))

print(results)