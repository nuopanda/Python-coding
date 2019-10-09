from word_ladder import WordLadder


def test_word_ladder():
    """test WordLadder constructor"""
    wordlist = []
    world_ladder = WordLadder("cat", "hat", wordlist)
    assert world_ladder.alphabet == [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
        'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
        's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def test_make_ladder():
    """test make_ladder method of WordLadder class"""
    wordlist = ["love", "hove", "have", "hate",
                "lone", "hone", "hale", "bate", "life"]
    world_ladder = WordLadder("love", "hate", wordlist)
    res = world_ladder.make_ladder()
    assert res == "love\thove\thave\thate\t"
