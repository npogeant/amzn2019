#The library
!pip install transformers

from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline

#The model from HuggingFace
model_name = "ProsusAI/finbert"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
classifier = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)

#A loop that will create the labels
df = (
    df
    .assign(sentiment = lambda x: x['content_modified'].apply(lambda s: classifier(s)))
    .assign(
         label = lambda x: x['sentiment'].apply(lambda s: (s[0]['label'])),
         score = lambda x: x['sentiment'].apply(lambda s: (s[0]['score']))
    )
)
#https://huggingface.co/transformers/quicktour.html
#https://huggingface.co/transformers/usage.html
#https://github.com/ProsusAI/finBERT
