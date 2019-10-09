import re
import string


class TextCleaner:
    def __init__(self, file_name):
        """given a file_name, initialize the constructor"""
        self.sentence = []
        self.open_file(file_name)

    def open_file(self, file_name):
        """given a file name, open the file"""
        try:
            self.f = open(file_name)
            self.f.readline()
            self.f.readline()
            self.text = self.f.read()
        except:
            print("Can't open", file_name)
            return

    def clean_text(self):
        """clean text: lowercase, replace comma, remove punctuations,split with period,"""
        self.new_text = self.text.lower()
        self.new_text = self.new_text.replace("mr.", "mr ")
        self.new_text = self.new_text.replace("dr.", "dr ")
        self.new_text = re.sub(r"[\,]", " COMMA", self.new_text)
        # self.new_text = re.sub(r"[^a-zA-Z\.\'\-]+", " ", self.new_text)
        # self.new_text = re.sub(r"\-", "", self.new_text)
        self.new_text= re.sub(r'\(|\)|\-|\"',"",self.new_text)
        self.sentence = self.new_text.split(".")
        for sentence in self.sentence:
            print(sentence)
            print()
