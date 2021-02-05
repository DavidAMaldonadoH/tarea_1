n = int(input())
all_words = list()
for i in range(n):
   word = input()
   all_words.append(word)

times_repeated = list()

for word in all_words:
   x=all_words.count(word)
   times_repeated.append(x)

dic = dict()

for i in range(n):
   dic.setdefault(all_words[i], times_repeated[i])

values = dic.values()

print(len(values))

for value in values:
   print(value, end=" ")