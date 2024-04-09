from django.http import JsonResponse
from transformers import pipeline
import nltk
nltk.download('punkt')

# classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)
# sentences = ["I want to stab him with a knife", "Im very happy today"]
# model_outputs = classifier(sentences)
# print(model_outputs)

def getEmotion(thoughts):
    # classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)
    # sentences = nltk.sent_tokenize(text)
    # model_outputs = classifier(sentences)
    # return model_outputs
    classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)
    model_outputs = classifier(thoughts)
    return model_outputs[0]