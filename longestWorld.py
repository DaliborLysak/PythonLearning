txt = input()
length = 0
words = txt.split()
maxWorld = ""
for word in words:
  if len(word) > length:
    length = len(word)
    maxWorld = word
print(maxWorld)