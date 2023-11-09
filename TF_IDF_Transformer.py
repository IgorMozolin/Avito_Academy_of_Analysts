from typing import List
from math import log


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

    def fit_transform_initial(self, corpus: List[str]) -> List[List[int]]:
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


class TfidfTransformer():
    """
    A class for transforming count matrices into TF-IDF matrices.
    """
    def __init__(self) -> None:
        pass

    def tf_matrix(self, count_matrix):
        """
        Calculate the TF (Term Frequency) matrix from a count matrix.

        Args:
            count_matrix (list): A list of lists representing the count matrix.

        Returns:
            list: A list of lists representing the TF matrix.
        """
        tf_matrix = []
        for lst in count_matrix:
            tf_m = []
            for i in lst:
                tf_m.append(round(i / sum(lst), 3))
            tf_matrix.append(tf_m)
        return tf_matrix

    def idf_matrix(self, count_matrix):
        """
        Calculate the IDF (Inverse Document Frequency)
        matrix from a count matrix.

        Args:
            count_matrix (list): A list of lists representing the count matrix.

        Returns:
            list: A list representing the IDF matrix.
        """
        idf_matrix = []
        n = len(count_matrix[0])
        idf = [0] * n
        for lst in count_matrix:
            for i in range(n):
                if lst[i] != 0:
                    idf[i] += 1
        for i in range(n):
            idf_matrix.append(round(1+log((len(count_matrix)+1)/(idf[i]+1)),
                                    3))
        return idf_matrix

    def fit_transform(self, count_matrix):
        """
        Transform a count matrix into a TF-IDF matrix.

        Args:
            count_matrix (list): A list of lists representing the count matrix.

        Returns:
            list: A list of lists representing the TF-IDF matrix.
        """
        tf_matrix = self.tf_matrix(count_matrix)
        idf_matrix = self.idf_matrix(count_matrix)
        tfidf_matrix = [[round(tf * idf, 3) for tf, idf
                         in zip(tf_row, idf_matrix)] for tf_row in tf_matrix]

        return tfidf_matrix


class TfidfVectorizer(CountVectorizer):
    """
    Initialize an instance of TfidfVectorizer, inheriting from CountVectorizer.

    This class is used to convert a collection of
    text documents to a TF-IDF matrix.

    Attributes:
        word_list (dict): A dictionary that maps unique words to their indices.
        vectors (list): A list of unique words (features) in the corpus.
        tf_idf (TfidfTransformer): An instance of TfidfTransformer
        for transforming count matrices into TF-IDF matrices.
    """
    def __init__(self):
        super().__init__()
        self.tf_idf = TfidfTransformer()

    def fit_transform(self, corpus):
        """
        Fit the vectorizer to the corpus and transform it into a TF-IDF matrix.

        Args:
            corpus (list): A list of text documents.

        Returns:
            list: A list of lists representing the TF-IDF matrix.
        """
        count_matrix = super().fit_transform_initial(corpus)
        return self.tf_idf.fit_transform(count_matrix)


if __name__ == "__main__":
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(tfidf_matrix)
