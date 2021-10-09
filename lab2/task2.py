strlol = input()
listlol = list(strlol.split())
maxx = 0
word = ""
for i in listlol:
    if len(i) > maxx:
        maxx = len(i)
        word = i
print(maxx)
print(word)
