from n_gram_frequencies import NgramFrequencies


def test_n_gram_frequency():
    """test the constructor"""
    sentence = [
        "hi COMMA mr lee went to the park", " let's go"]
    n_gram_freq = NgramFrequencies(sentence, 2)
    assert n_gram_freq.N == 2
    assert n_gram_freq.count == 0
    assert n_gram_freq.gram_dict == {}
    assert n_gram_freq.N_grams_by_count == []
    assert n_gram_freq.gram_freq_dict == {}
    assert n_gram_freq.N_grams_by_freq == []


def test_add_item():
    """test the add_item method"""
    sentence = [
        "hi COMMA mr lee went to the park", " let's go"]
    n_gram_freq = NgramFrequencies(sentence, 2)
    n_gram_freq.add_item()
    dict = {'hi_COMMA': 1, 'COMMA_mr': 1, 'mr_lee': 1, 'lee_went': 1,
            'went_to': 1, 'to_the': 1, 'the_park': 1, "let's_go": 1}
    assert n_gram_freq.count == 8 
    assert n_gram_freq.gram_dict == dict


def test_top_n_counts():
    """test the top_n_counts method"""
    sentence = [
        "hi COMMA mr lee" , " let's go"]
    n_gram_freq = NgramFrequencies(sentence, 2)
    n_gram_freq.add_item()
    n_gram_freq.top_n_counts(2)
    list = [('hi_COMMA', 1), ('COMMA_mr', 1), ('mr_lee', 1), ("let's_go",1)]
    assert n_gram_freq.N_grams_by_count == list

def test_top_n_freqs():
    """test the top_n_freqs method"""
    sentence = [
        "hi COMMA mr lee" , " let's go"]
    n_gram_freq = NgramFrequencies(sentence, 2)
    n_gram_freq.add_item()
    n_gram_freq.top_n_freqs(2)
    list = [('hi_COMMA', 0.25), ('COMMA_mr', 0.25),
     ('mr_lee', 0.25), ("let's_go",0.25)]
    assert n_gram_freq.N_grams_by_freq == list

def test_frequency():
    """test the frequencey method"""
    sentence = [
        "hi COMMA mr lee" , " let's go"]
    n_gram_freq = NgramFrequencies(sentence, 2)
    n_gram_freq.add_item()
    n_gram_freq.top_n_freqs(2)
    n_gram_freq.frequency("hi_COMMA")
    assert n_gram_freq.gram_freq_dict["hi_COMMA"]==0.25