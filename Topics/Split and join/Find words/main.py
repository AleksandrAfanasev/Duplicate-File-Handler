s = input()
word_list = list(s.split(' '))
new_words = [word for word in word_list if word.endswith('s')]
s = '_'.join(new_words)
print(s)