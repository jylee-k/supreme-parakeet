from flask import Flask, request, jsonify
import os
import tempfile


# Assuming your model function is named transcribe_audio
def transcribe_audio(audio_file_path):
    # Placeholder function, replace with actual model inference
    transcription = "BEFORE HE HAD TIME TO ANSWER A MUCH ENCUMBERED VERA BURST INTO THE ROOM"
    duration = "20.7"
    return transcription, duration

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
        
        # Call your model function to transcribe the audio
        transcription, duration = transcribe_audio(temp_audio_path)

        # Clean up the temporary file
        os.remove(temp_audio_path)

        # Return the transcription and duration
        return jsonify({
            'transcription': transcription,
            'duration': duration
        }), 200

if __name__ == '__main__':
    app.run(host='localhost', port=8001)
