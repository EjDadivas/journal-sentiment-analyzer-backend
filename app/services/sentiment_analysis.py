from transformers import RobertaTokenizerFast, TFRobertaForSequenceClassification, pipeline

hf_token = "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"

model_name = "arpanghoshal/EmoRoBERTa"

tokenizer = RobertaTokenizerFast.from_pretrained(model_name, token=hf_token)
model = TFRobertaForSequenceClassification.from_pretrained(model_name, token=hf_token)

emotion = pipeline('sentiment-analysis', 
                   model=model_name, 
                   return_all_scores=True, 
                   tokenizer=tokenizer,
                   token=hf_token)


def sentiment_analysis(text: str):
    emotion_labels = emotion(text)    
    return emotion_labels[0]