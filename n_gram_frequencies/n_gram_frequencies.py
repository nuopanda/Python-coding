class NgramFrequencies:
    def __init__(self, sentence, N):
        """given a integer N, and cleaned text, initialize the constructor"""
        self.sentence = sentence
        self.N = N
        self.count = 0
        self.gram_dict = {}
        self.N_grams_by_count = []
        self.gram_freq_dict = {}
        self.N_grams_by_freq = []

    def add_item(self):
        """add the n-gram into a dict """
        for sentence in self.sentence:
            word_list = sentence.split()
            word = []
            for i in range(len(word_list)-self.N+1):
                for n in range(self.N):
                    word.append(word_list[i+n])
                # print(word)
                N_grams = "_".join(word)
                word = []
                self.count += 1
                if N_grams in self.gram_dict.keys():
                    self.gram_dict[N_grams] += 1
                else:
                    self.gram_dict[N_grams] = 1
        # print(self.gram_dict)

    def top_n_counts(self,top_n):
        """sort the dict based on the count, print the top 10 element in the sorted list"""
        self.N_grams_by_count = sorted(
            self.gram_dict.items(),
            key=lambda x: x[1],
            reverse=True)
        for i in range(top_n):
            print("\t", self.N_grams_by_count[i])

    def top_n_freqs(self,top_n):
        """calculate the freq to have a freq-dict, print the top 10 element in the sorted list"""
        for word in self.gram_dict.keys():
            self.gram_freq_dict[word] = self.gram_dict[word]/(self.count)
        self.N_grams_by_freq = sorted(
            self.gram_freq_dict.items(),
            key=lambda x: x[1],
            reverse=True)
        for i in range(top_n):
            print("\t", self.N_grams_by_freq[i])

    def frequency(self, word):
        """given a n_gram word, print its frequency"""
        print(self.gram_freq_dict[word])
