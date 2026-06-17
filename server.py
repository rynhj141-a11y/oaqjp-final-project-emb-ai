"""
Server module for the Emotion Detection application.
Provides routes to render the user interface and analyze text for emotions.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# pylint: disable=invalid-name, consider-using-f-string
app = Flask(__name__)

@app.route("/emotionDetector")
def detector():
    """
    Analyzes the provided query parameter text for emotions.
    Returns a formatted string response or an error if invalid.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."

    return (
        "For the given statement, the system response is "
        "'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. "
        "The dominant emotion is {}."
    ).format(
        response['anger'],
        response['disgust'],
        response['fear'],
        response['joy'],
        response['sadness'],
        response['dominant_emotion']
    )

@app.route("/")
def render_index_page():
    """
    Renders the entry point index HTML page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Deploy the application on localhost:5000
    app.run(host="0.0.0.0", port=5000)
    