import tensorflow as tf
from transformers import TFAutoModelForSequenceClassification
from transformers import pipeline
from transformers import AutoTokenizer

id2label = {0: "Not Spam", 1: "Spam"}
label2id = {"Not Spam": 0, "Spam": 1}

def load_model():
    loaded_model = TFAutoModelForSequenceClassification.from_pretrained("NotShrirang/albert-spam-filter", num_labels=2, id2label=id2label, label2id=label2id)
    loaded_tokenizer = AutoTokenizer.from_pretrained("albert-base-v2")

    return loaded_model, loaded_tokenizer

def create_pipeline(model, tokenizer):
    classifier = pipeline('sentiment-analysis',
                      model=model,
                      tokenizer=tokenizer
             )
    
    return classifier

def predict(classifier, text):
    prediction = classifier(text)[0]
    return prediction