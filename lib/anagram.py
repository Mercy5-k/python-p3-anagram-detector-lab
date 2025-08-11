# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        # Turn the original word into a sorted list of letters
        sorted_word = sorted(self.word)

        # Empty list to collect matches
        matches = []

        # Loop through each word in the list
        for candidate in word_list:
            # Make sure we ignore the word if it's the same as the original
            if candidate.lower() != self.word:
                # Sort the candidate and compare
                if sorted(candidate.lower()) == sorted_word:
                    matches.append(candidate)

        return matches
