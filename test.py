
words = [word.split()[0] for word in open("wordlist.txt")]

for word in words:
    if len(word) == 7:
        if "a" in word and "e" in word and "i" in word and "s" in word and "r" in word and "o" in word and "t" in word:
            print(word)



'''
for word in open("wordlist.txt"):
    word = word.split()[0]
    if len(word) == 3:
        if word[0] == 't':
            if word[2] == 'a':
                print(word)
'''