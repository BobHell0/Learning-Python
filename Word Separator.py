#Word Separator 
phrase = input("Enter Phrase: ")

num_spaces = phrase.count(" ")

for a in range(num_spaces):
    pos_space = phrase.find(" ")
    phrase_sub = phrase[0:pos_space]
    print(phrase_sub)
    phrase = phrase[pos_space + 1 : len(phrase)]
print(phrase)









