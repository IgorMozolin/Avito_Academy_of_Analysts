from typing import List


class CountVectorizer:
    """
    Initialize an instance of CountVectorizer.

    This class is used to convert a collection
    of text documents to a matrix of token counts.

    Attributes:
        word_list (dict): A dictionary that maps unique words to their indices.
        vectors (list): A list of unique words (features) in the corpus.
    """
    def __init__(self) -> None:
        self.word_list = {}
        self.vectors = []

    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        """
        Fit the vectorizer to the corpus and transform it into a count matrix.

        Args:
            corpus (list): A list of text documents.

        Returns:
            list: A list of lists representing the count matrix.
            Each row corresponds to a document, and each column
            corresponds to a unique word in the corpus.
        """
        for phrase in corpus:
            words = phrase.split()
            for word in words:
                word = word.lower()
                if word not in self.word_list:
                    self.word_list[word] = len(self.word_list)
                    self.vectors.append(word)
        count_matrix = []
        for phrase in corpus:
            word_count = [0] * len(self.word_list)
            for word in phrase.split():
                word = word.lower()
                word_count[self.word_list[word]] += 1
            count_matrix.append(word_count)
        return count_matrix

    def get_feature_names(self) -> List[str]:
        """
        Get the feature names (unique words) in the corpus.

        Returns:
            list: A list of unique words (features) in the corpus.
        """
        return self.vectors


if __name__ == "__main__":
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
