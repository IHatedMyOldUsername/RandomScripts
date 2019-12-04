from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer

categories = ['alt.atheism, 'soc.religion.christian',comp.graphics', 'sci.med']
twenty_train = fetch_20newsgroups(subset='train', categroies=categories, shuffle=True, random_state=42)

count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)

