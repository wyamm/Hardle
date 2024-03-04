from nltk.corpus import words
import string
from english_words import get_english_words_set
UPPERCASE = list(string.ascii_uppercase)
word_list = get_english_words_set(['web2'], lower=True)
# word_list = words.words()

op = set()

for i, word in enumerate(word_list):
    if len(word) == 5 and word[0] not in UPPERCASE:
        lenop1 = len(op)
        op.add(word)
        lenop2 = len(op)
        if lenop1 != lenop2:
            flw_file = open("five_letter_words_list.txt", 'a')
            flw_file.write(word+", ")
            if lenop2%10 == 0:
                flw_file.write('\n')
            flw_file.close()
