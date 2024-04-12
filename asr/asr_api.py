from flask import Flask, request, jsonify
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
import librosa
import torch
import os
import tempfile

SAMPLE_RATE = 16000


def get_transcription(audio_array):
    # Transcribe the audio using your model
    input_values = processor(audio_array, return_tensors="pt", padding="longest").input_values
    logits = model(input_values).logits
    # take argmax and decode
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.batch_decode(predicted_ids)

    return transcription

app = Flask(__name__)

@app.route('/asr', methods=['POST'])
def asr():
    if 'file' not in request.files:
        return jsonify({'error': 'Please include your file in form-data'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'File string is empty'}), 400

    if file:
        # Save the file temporarily
        _, temp_audio_path = tempfile.mkstemp(suffix='.mp3')
        file.save(temp_audio_path)

        # Process the audio file
        # TODO: Add your audio processing code here
        audio_array, _ = librosa.load(temp_audio_path, sr=SAMPLE_RATE)
        duration = len(audio_array) / SAMPLE_RATE

        # Call your model function to transcribe the audio
        transcription = get_transcription(audio_array)

        # Clean up the temporary file
        os.remove(temp_audio_path)

        # Return the transcription and duration
        return jsonify({
            'transcription': transcription,
            'duration': duration
        }), 200

if __name__ == '__main__':
    # load model and processor
    processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-960h")
    model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h")
    app.run(host='localhost', port=8001)
