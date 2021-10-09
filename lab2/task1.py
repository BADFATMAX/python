strlol = input().lower()
strlist = list(strlol)
llist = []

for i in strlist:
    if i != ' ':
        llist.append(i)

strReversed = llist[::-1]

if llist == strReversed:
    print("Палиндром")
else:
    print("Не палиндром")
print(llist)
