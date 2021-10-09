dct = {'красный': 'алый', 'тьма': 'много'}

strlol = input().split()

p = -1  # для нумерации слов в строке

for i in strlol:
    p += 1
    for j in dct.keys():
        if i == j:
            # i = dct.get(i)
            strlol[p] = dct[j]

for g in range(len(strlol)):
    print(strlol[g], end=' ')

# dct = {'очи': 'глаза', 'скупой': 'жадный', 'кидать': 'бросать'}
# stroka = input()
# stroka = stroka.split()
# k = -1
# for i in stroka:
#     k += 1
# for j in dct.keys():
#     if i == j:
#         stroka[k] = dct[j]
# for i in range(len(stroka)):
#     print(stroka[i], end=' ')
