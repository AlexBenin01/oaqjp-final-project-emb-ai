"""
Server Flask per l'applicazione di rilevamento delle emozioni.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask(__name__)


@app.route("/")
def index():
    """
    Mostra la pagina principale dell'applicazione.
    """
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Riceve il testo dall'utente, lo analizza e restituisce il risultato.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Testo non valido! Per favore riprova!"

    return (
        "Per la dichiarazione fornita, la risposta del sistema è "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} e "
        f"'sadness': {response['sadness']}. "
        f"L'emozione dominante è {response['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="localhost", port=5000)