import string
file = open('LICENSE')
A = {}
mytext = "test text for testing only text"
strng = file.read().split()
for i in range(len(strng)):
    strng[i] = strng[i].lower()
for i in range(len(strng)):
    tmp = ''
    for j in strng[i]:
        if j not in string.punctuation:
            tmp += j
        else:
            tmp += ' '
    strng[i] = tmp
tmp = ''
for i in strng:
    tmp += i + ' '
tmp = tmp.split()
strng = tmp
print(tmp)
for i in strng:
    if i not in A:
        A[i] = 1
    else:
        A[i] += 1
for i in A:
    print(i, ':', A[i])
index_max = 1
max_word = ''
for i in A:
    if A[i] > index_max:
        index_max = A[i]
        max_word = i
print('Max: ', max_word, '-', index_max)