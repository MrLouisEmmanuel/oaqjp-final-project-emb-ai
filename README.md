# Final Project: Emotion Detector (oaqjp-final-project-emb-ai)

Final project for the Coursera course **Developing AI Applications with Python and Flask**
(IBM Generative AI Professional Certificate).

An AI-based web application that detects the emotions (anger, disgust, fear, joy, sadness)
expressed in a piece of text using the **Watson NLP** Emotion Predict service, and
deploys it with **Flask**.

## Project structure

```
oaqjp-final-project-emb-ai/
├── EmotionDetection/
│   ├── __init__.py              # package initializer
│   └── emotion_detection.py     # emotion_detector() function (Watson NLP)
├── static/mywebscript.js        # front-end script calling /emotionDetector
├── templates/index.html         # web interface
├── server.py                    # Flask web server
├── test_emotion_detection.py    # unit tests
└── README.md
```

## Run

```bash
python3.11 -m pip install flask requests pylint
python3.11 test_emotion_detection.py   # unit tests
python3.11 server.py                   # http://localhost:5000
pylint server.py                       # static code analysis
```

> Note: the Watson NLP endpoint (`sn-watson-emotion.labs.skills.network`) is only reachable
> from inside the IBM Skills Network lab environment.
