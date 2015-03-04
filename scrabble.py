# imports sys module to allow for .argv to be used to gather rack data
import sys
# takes command line arguments when running file.
rack = sys.argv[1]
# creates empty list for confirmed words to be compared to dictionary words
confirm = []
# creates empty list for dictionary words
words = []

# predefined scoring for each letter
scores = {"A": 1, "C": 3, "B": 3, "E": 1, "D": 2, "G": 2,
          "F": 4, "I": 1, "H": 4, "K": 5, "J": 8, "M": 3,
          "L": 1, "O": 1, "N": 1, "Q": 10, "P": 3, "S": 1,
          "R": 1, "U": 1, "T": 1, "W": 4, "V": 4, "Y": 4,
          "X": 8, "Z": 10}

# crates the dict from opened sowpods.txt and makes it readable
dictionary = open("sowpods.txt", "r")
# for each line in the dictionary, strip trailing white space, and
# place into word list.
for line in dictionary:
    line = line.strip()
    words.append(line)

# for each entry in dictionary,
for word in words:
    # binds the rack letters to a list as individual string values
    letters = list(rack)
    # comparison set True so the loop continues to run after False return
    compare = True
    # for each letter in word entry,
    for letter in word:
        # return false and run next letter (does not add anything to confirm)
        if letter not in letters:
            compare = False
        # return true, and remove letter from rack list. Tally total score,
        # and append word and total to confirm list.
        else:
            letters.remove(letter)
            total = 0
            for letter in word:
                total = total + scores[letter]
            confirm.append([total, word])
# Sorts the confirm list
confirm.sort()
# Bind the first and second item (word and total) from confirm list, and
# print to terminal.
for item in confirm:
    score = item[0]
    word = item[1]
    print(str(score) + " " + word)
