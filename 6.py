dictionary = dict()
sl = open('en-ru_6.txt', encoding='utf-8')
slt = open('output.txt', 'w', encoding='utf-8')
s = sl.readline().rstrip()
while len(s) > 0:
    en_trans, ru_trans = list(s.split('\t-\t'))
    if ',' in ru_trans:
        for i in ru_trans.split(','):
            i = i.lstrip()
            if i in dictionary:
                dictionary[i] = dictionary[i]+', '+en_trans
            else:
                dictionary[i] = en_trans
    else:
        if ru_trans in dictionary:
            dictionary[ru_trans] = dictionary[ru_trans]+', '+en_trans
        else:
            dictionary[ru_trans] = en_trans

    s = sl.readline().rstrip()

key_sort = sorted(dictionary.keys())
for i in key_sort:
    print('\t-\t'.join((i, dictionary[i])), file=slt)
