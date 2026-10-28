"""Emotion detection module using the Watson NLP EmotionPredict service."""
import json

import requests

URL = (
    "https://sn-watson-emotion.labs.skills.network/v1/"
    "watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
EMOTIONS = ("anger", "disgust", "fear", "joy", "sadness")


def emotion_detector(text_to_analyze):
    """Analyze the given text with Watson NLP and return emotion scores.

    Returns a dictionary with the scores for anger, disgust, fear, joy and
    sadness, plus the name of the dominant emotion. If the service responds
    with status code 400 (e.g. blank input), every value is None.
    """
    input_json = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(URL, json=input_json, headers=HEADERS, timeout=30)

    # Task 7: error handling for blank / invalid input
    if response.status_code == 400:
        result = {emotion: None for emotion in EMOTIONS}
        result["dominant_emotion"] = None
        return result

    # Task 3: format the output
    formatted_response = json.loads(response.text)
    emotions = formatted_response["emotionPredictions"][0]["emotion"]

    result = {emotion: emotions[emotion] for emotion in EMOTIONS}
    result["dominant_emotion"] = max(result, key=result.get)
    return result
