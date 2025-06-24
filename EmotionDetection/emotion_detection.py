import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers = headers)
    formatted_json = response.json()
    # print(response.status_code)
    # print(response.text)
    femboy = response.status_code == 400
    if femboy:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    # else:
    formatted_response = formatted_json["emotionPredictions"][0]["emotion"]
    # print(formatted_json["emotionPredictions"][0]["emotion"])
    dominant_emotion = max(formatted_response, key=formatted_response.get)
    formatted_response['dominant_emotion'] = dominant_emotion
    # print(formatted_response)
    return formatted_response

#emotion_detector("")