# NLTK
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print([lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in nltk.word_tokenize(text)])
#spacy
import spacy
nlp = spacy.load('en', disable=['parser', 'ner'])
doc = nlp(text)
print(" ".join([token.lemma_ for token in doc]))
# TextBlob
print(lemmatize_with_postag(text))
# Pattern
from pattern.en import lemma
print(" ".join([lemma(wd) for wd in sentence.split()]))