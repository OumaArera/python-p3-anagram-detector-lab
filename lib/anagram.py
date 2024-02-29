# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, possible_anagrams):
        matches = []
        sorted_word = sorted(self.word)
        for anagram in possible_anagrams:
            if len(anagram) == len(self.word) and sorted(anagram.lower()) == sorted_word:
                matches.append(anagram)
        return matches
