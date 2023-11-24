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
        """
        example: word = cat
        c => char_tree_dict[c] ? next : char_tree_dict[c] = {}
        a => char_tree_dict[c][a] ? next : char_tree_dict[c][a] = {}
        t => char_tree_dict[c][a][t] ? next : char_tree_dict[c][a][t] = {}
        """

    def find_anagrams(self, word):
        """
        Returns a list with all anagrams
        of the input word
        """


def solution_tester():
    pass

test = Anagrams()
print(test.dict_content)
"""
I could convert the dictionary into
 a massive nested object
Where each nest-level corresponds with a
word index, and obj[a] is an object
of all letters that come after a and still can make up valid words

The goal is to cut down on
permutations time complexity;
This can be accomplished by disqualifying
a given permutation of a string
as soon as possible while we are calculating it
{
    a: {
        a: {
            b: {}
            c:
            d:
            ...
        },
        b:
        c:
        d:
        ...
    },
    b: {}
    c: {}
    d: {}
    ...
}
This might speed the
"""
