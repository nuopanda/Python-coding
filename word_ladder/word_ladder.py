from queue import Queue
from stack import Stack

import time


class WordLadder:
    """A class providing functionality to create word ladders"""
    # Implement whatever functionality is necessary to generate a
    # stack representing the word ladder based on the parameters
    # passed to the constructor.

    def __init__(self, w1, w2, wordlist):
        """given the two input words and wordlist,
        initialize the constructor"""
        self.wordlist = wordlist
        self.queue = Queue()
        self.w1 = w1
        self.w2 = w2
        # create alphabet list with letter a-z
        self.alphabet = []
        for letter in range(97, 123):
            self.alphabet.append(chr(letter))
        self.visited_words = set()

    def make_ladder(self):
        """return the __str__ of the stack result"""
        start_time = time.time()
        # init the queue with a stack that contains w1
        if self.queue.isEmpty():
            stack = Stack()
            stack.push(self.w1)
            self.queue.enqueue(stack)
        while not self.queue.isEmpty():
            current_stack = self.queue.dequeue()
            word = current_stack.peek()
            for i in range(len(word)):
                for letter in self.alphabet:
                    if letter != word[i]:
                        new_word_list = list(word)
                        new_word_list[i] = letter
                        new_word = "".join(new_word_list)
                        if (new_word in self.wordlist and
                                new_word not in self.visited_words):
                            self.visited_words.add(new_word)
                            if new_word == self.w2:
                                current_stack.push(new_word)
                                return current_stack.__str__()
                            else:
                                new_stack = current_stack.copy()
                                new_stack.push(new_word)
                                self.queue.enqueue(new_stack)
        return None
