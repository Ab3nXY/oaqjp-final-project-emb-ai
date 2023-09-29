"""
Emotion Detection Flask Application
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emo_detector():
    """
    Emotion Detection Route
    Analyzes text input using an emotion detection module and returns emotional analysis results.
    Returns:
        str: A formatted string containing emotional analysis results.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid input ! Try again."
    return (
            f"For the given statement, the system response is "
            f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
            f"'joy': {joy} and 'sadness': {sadness}. The dominant emotion "
            f"is {dominant_emotion}."
        )

@app.route("/")
def render_index_page():
    """
    Index Page Route
    Renders an HTML page for user interaction.
    Returns:
        rendered_template: The HTML template for the application's user interface.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
