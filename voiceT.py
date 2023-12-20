from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import soundfile as sf
import torch
import vFunctions as vf



# Function to transcribe audio using the local model
def transcribe_audio(audio_file):
    # Load the pre-trained model and processor from the cache (local storage)
    processor = Wav2Vec2Processor.from_pretrained("guillaumekln/faster-whisper-large-v2", use_auth_token=False, local_files_only=True)
    model = Wav2Vec2ForCTC.from_pretrained("guillaumekln/faster-whisper-large-v2", use_auth_token=False, local_files_only=True)

    # Read the audio file
    speech, sample_rate = sf.read(audio_file)

    # Preprocess the audio
    input_values = processor(speech, sampling_rate=sample_rate, return_tensors="pt").input_values

    # Perform inference
    with torch.no_grad():
        logits = model(input_values).logits

    # Decode the predicted text
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.batch_decode(predicted_ids)[0]
    return transcription

# Main workflow
audio_file = 'path/to/your/audio/file.wav'
transcription = transcribe_audio(audio_file)
print("Transcription:", transcription)

# Check for phrases
vf.check_phrases(transcription)
