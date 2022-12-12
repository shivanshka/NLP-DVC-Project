from sklearn.feature_extraction.text import CountVectorizer

corpus = [
    "applle ball cat",
    "ball cat dog elephant"
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)

#print (X.toarray())
#print(vectorizer.get_feature_names_out())

max_features = 4
ngrams = 2 # tri grams

vectorizer = CountVectorizer(max_features=max_features, ngram_range=(1,ngrams))
X = vectorizer.fit_transform(corpus)

print (X.toarray())
print(vectorizer.get_feature_names_out())