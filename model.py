import re
import nltk
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


df = pd.read_csv("training.1600000.processed.noemoticon.csv", names=["rating", "index", "date", "category", "user", "tweet"])
df.drop(df.columns[[1, 2, 3, 4]], axis=1, inplace=True)
df["tweet"] = df["tweet"].astype('str') 

stop_words = stopwords.words('english')
lemmatizer = WordNetLemmatizer()

def clean_comment(comment: str):
    comment = re.sub('[^A-Za-z0-9]+', ' ', comment)
    comment = comment.lower()
    tokens = nltk.word_tokenize(comment)
    comment = [word for word in tokens if word not in stop_words]
    comment = [lemmatizer.lemmatize(word) for word in comment]
    return ' '.join(comment)
i = 0
for tweet in df["tweet"]:
    df.at[i, "tweet"] = clean_comment(tweet)
    i += 1

y = df["rating"]
X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.3, stratify=y)

vect = CountVectorizer(min_df=10)

X_train_review_bow = vect.fit_transform(X_train['tweet'])
X_test_review_bow = vect.transform(X_test['tweet'])

vectorizer = TfidfVectorizer(min_df=10)

X_train_review_tfidf = vectorizer.fit_transform(X_train['tweet'])
X_test_review_tfidf = vectorizer.transform(X_test['tweet'])

clf = MultinomialNB()
clf.fit(X_train_review_bow, y_train)

y_pred = clf.predict(X_test_review_bow) #prediction from model
print('Test Accuracy: ', accuracy_score(y_test, y_pred))

