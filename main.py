import typing


def specialsort(inputelem):
    return inputelem[1]


import re
print('hi')

fr: typing.TextIO = open('D:/testtext.txt', 'r')
fw: typing.TextIO = open('D:/output.txt', 'w')
words = []

for line in fr:
    words.extend(re.findall(r'\b\w+\b', line))
print(words)

words1: list[list[typing.Union[int, typing.Any]]] = []

i = 0
while words:
    abc = words[0]
    words1.append([abc, 0])
    for word in words:
        if word == abc:
            (words1[i])[1] += 1
            words.remove(word)
    print(words)
    i += 1
words1.sort(key=specialsort, reverse=True)
print(words1)
quantity = int(input('\nВведите количество: '))
for i in range(quantity):
    fw.write(words1[i][0]+"\t"+str(words1[i][1])+"\n")
fr.close()
fw.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
