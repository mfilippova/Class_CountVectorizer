class CountVectorizer():
    """Class CountVectorizer for encode texts"""

    def __init__(self, lowercase=True):
        self.lowercase = lowercase

    def fit_transform(self, corpus):
        splitted_corpus = [doc.lower().split() for doc in corpus]
        bag_of_words = {word for doc in splitted_corpus for word in doc}
        vectors = [[doc.count(word) for word in bag_of_words] for doc in splitted_corpus]
        return vectors


if __name__ == "__main__":
    corpus = ['Crock Pot Pasta Never boil pasta again',
              'Pasta Pomodoro Fresh ingredients Parmesan to taste']
    vectorizer = CountVectorizer()
    print(vectorizer.fit_transform(corpus))
