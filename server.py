from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Cho phép CORS để Swift có thể gọi API

@app.route('/get_transcript', methods=['GET'])
def get_transcript():
    video_id = request.args.get('video_id')

    if not video_id:
        return jsonify({'error': 'Missing video_id parameter'}), 400

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en', 'vi'])  # Ưu tiên tiếng Anh và Việt Nam
        return jsonify({'transcript': transcript})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

