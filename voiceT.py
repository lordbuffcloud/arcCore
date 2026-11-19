# ⬡ CK42X · ck42x.com
# MODULE: local audio transcription entry point feeding phrase triggers
# gold on black. sting once.

from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import soundfile as sf
import torch
import vFunctions as vf



def transcribe_audio(audio_file):
    """decode audio_file to text offline; local_files_only=True rejects an uncached checkpoint.
    TRAP: the checkpoint id names faster-whisper-large-v2 but loads through wav2vec2 classes."""
    processor = Wav2Vec2Processor.from_pretrained("guillaumekln/faster-whisper-large-v2", use_auth_token=False, local_files_only=True)
    model = Wav2Vec2ForCTC.from_pretrained("guillaumekln/faster-whisper-large-v2", use_auth_token=False, local_files_only=True)

    speech, sample_rate = sf.read(audio_file)

    input_values = processor(speech, sampling_rate=sample_rate, return_tensors="pt").input_values

    with torch.no_grad():
        logits = model(input_values).logits

    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.batch_decode(predicted_ids)[0]
    return transcription

# TRAP: audio_file below is a placeholder path, not a real recording.
audio_file = 'path/to/your/audio/file.wav'
transcription = transcribe_audio(audio_file)
print("Transcription:", transcription)

vf.check_phrases(transcription)
