from flask import Flask, jsonify, request
from flask_cors import CORS
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)
CORS(app)

# Proxy miễn phí (thay thế bằng proxy hợp lệ)
proxies = {
    "http": "http://65.49.14.150:3128",
    "https": "http://65.49.14.150:3128"
}

@app.route('/transcript', methods=['GET'])
def get_transcript():
    video_id = request.args.get('video_id')
    if not video_id:
        return jsonify({"error": "Missing video_id parameter"}), 400

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, proxies=proxies)
        return jsonify({"transcript": transcript})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

