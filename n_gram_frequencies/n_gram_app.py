from text_cleaner import TextCleaner
from n_gram_frequencies import NgramFrequencies


def main():
    """collect n-gram frequencies and print the top 10 of eacy type out"""
    text_cleaner = TextCleaner("corpse_bride.txt")
    clean_text(text_cleaner)
    print("Top 10 unigrams: ")
    n_gram_1 = NgramFrequencies(text_cleaner.sentence, 1)
    top_n_count(n_gram_1)
    print("Top 10 bigrams: ")
    n_gram_2 = NgramFrequencies(text_cleaner.sentence, 2)
    top_n_count(n_gram_2)
    print("Top 10 trigrams: ")
    n_gram_3 = NgramFrequencies(text_cleaner.sentence, 3)
    top_n_count(n_gram_3)
    print("Check frequency for N-gram word:")
    gram_input = input("Enter unigram/bigram/trigram: ")
    if gram_input == "unigram":
        check_freq(n_gram_1)
    elif gram_input == "bigram":
        check_freq(n_gram_2)
    elif gram_input == "trigram":
        check_freq(n_gram_3)


def clean_text(text_cleaner):
    """call method of text_cleaner, have the text_cleaner.sentence"""
    text_cleaner.clean_text()


def top_n_count(n_gram):
    """call methods of n_gram,print the top 10 n_gram based on freq"""
    n_gram.add_item()
    # n_gram.top_n_counts(10)
    n_gram.top_n_freqs(10)


def check_freq(n_gram):
    """call method of n_gram, print the frequency of input n_gram word"""
    word = input("Please enter the input: ")
    n_gram.frequency(word)


main()
