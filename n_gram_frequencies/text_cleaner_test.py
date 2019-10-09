from text_cleaner import TextCleaner


def test_text_cleaner():
    """test the constructor"""
    text_cleaner = TextCleaner("corpse_bride.txt")
    assert text_cleaner.sentence == []


def test_open_file():
    """test open file"""
    text_cleaner = TextCleaner("corpse_bride.txt")
    text_f = open("corpse_bride.txt")
    text_f.readline()
    text_f.readline()
    text = text_f.read()
    assert text == text_cleaner.text
    text_cleaner=TextCleaner("corpse.txt")


def test_clean_text():
    """test text_clean"""
    text_cleaner = TextCleaner("corpse_bride.txt")
    text_cleaner.text = "Hi, Mr.Lee -went to the park. Let's go"
    text_cleaner.clean_text()
    assert text_cleaner.sentence == [
        "hi COMMA mr lee went to the park", " let's go"]


