#The library
!pip install transformers

from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline

#The model from HuggingFace
model_name = "ProsusAI/finbert"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
classifier = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)

#An example to use the classifier
classifier('A strong second-half of the year for dealmaking has bankers optimistic for 2021')

#https://huggingface.co/transformers/quicktour.html
#https://huggingface.co/transformers/usage.html
#https://github.com/ProsusAI/finBERT
