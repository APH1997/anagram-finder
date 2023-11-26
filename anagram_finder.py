class Anagrams:
    def __init__(self, scrabble_dict_path="./scrabble_dictionary.txt"):
        """
        Reads local scrabble file; converts to list,
        then converts to super object
        """
        self.dict_content = []
        with open(scrabble_dict_path, "r") as file:
            for line in file:
                self.dict_content.append(line.replace('\n', ''))

        char_tree_dict = {}
        # iterate through self.dict_content
        # iterate through the letter of each word
        # scaffold the letters through the object
        for word in self.dict_content:
            curr_sub_obj = char_tree_dict
            for char in word:
                if char not in curr_sub_obj:
                    curr_sub_obj[char] = {}
                    curr_sub_obj = curr_sub_obj[char]
                else:
                    curr_sub_obj = curr_sub_obj[char]

        self.dictionary_obj = char_tree_dict


    def find_anagrams(self, word, r = None):
        """
        Returns a list with all anagrams
        of the input word

        bath
        btah
        btha
        baht
        tabh
        tahb

        need to figure this out lmao
        """
        if len(word) <= 1:
            return [word]

        # Grab first char, hold constant well shuffling all others
        for i in range(len(word)):
            stationary_char = word[i]
            for index, char in enumerate(word):
                if





def solution_tester():
    pass

test = Anagrams()
print(test.find_anagrams('bat'))
