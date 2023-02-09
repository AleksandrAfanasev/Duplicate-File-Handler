text = input()
words = text.split()
for word in words:
    if word.startswith('www.', 0) or word.startswith('https://', 0) or word.startswith('http://', 0):
        print(word)
    elif word.startswith('WWW.', 0):
        print(word)
    else:
        continue