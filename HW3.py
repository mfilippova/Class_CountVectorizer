class CountVectorizer():
    """Class CountVectorizer for encoding texts"""

    def __init__(self, lowercase=True):
        self.lowercase = lowercase
        self._vocabulary = []

    def get_feature_names(self):
        return self._vocabulary

    def fit_transform(self, corpus):
        if self.lowercase:
            splitted_corpus = [doc.lower().split() for doc in corpus]
        else:
            splitted_corpus = [doc.split() for doc in corpus]

        bag_of_words = set()
        for doc in splitted_corpus:
            for word in doc:
                if word not in bag_of_words:
                    bag_of_words.add(word)
                    self._vocabulary.append(word)

        vectors = [[doc.count(word) for word in self._vocabulary]
                   for doc in splitted_corpus]
        return vectors


if __name__ == "__main__":
    corpus = ['Crock Pot Pasta Never boil pasta again',
              'Pasta Pomodoro Fresh ingredients Parmesan to taste']
    vectorizer = CountVectorizer()
    print(vectorizer.fit_transform(corpus))
    print(vectorizer.get_feature_names())
