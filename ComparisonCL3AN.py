# Imports

# Variables

# Definitions


def split2words(line):

    try:
        words = line.split('\t', 1)
        if len(words) != 2:
            words.append('')
    except ValueError:
        words = ['', '']
    return words


def compare(first, second):
    sharedkeys = set(first.keys()).intersection(second.keys())
    for key in sharedkeys:
        if first[key] != second[key]:
            print('Hostname: {}, \t IP Address 1: {}, \t IP Address 2: {}'.format(key, first[key], second[key]))


# Program

reset = 'y'

    while reset == 'y':
        filecomparison(

        print("Please input the files you wish to compare")
        print("Example: somedata.txt - or - datasome.csv")
        print("-----------------------------------------")

        fname1 = input("First File: ")
        fname2 = input("Second File: ")

        f1 = open(fname1)
        f2 = open(fname2)

        text1 = f1.readlines()
        text2 = f2.readlines()

        print('\n', '...', '\n', 'files opened', '\n', '...')

        print('\n')
        print("-----------------------------------------")
        print("Comparing files: " " f1> " + fname1, " f2< " + fname2, sep=',')
        print("-----------------------------------------")

        # dictionary of file 1

        dict_1 = {}

        for line in text1:
            k, v = split2words(line)
        k = k.upper()
        dict_1.setdefault(k, [])

        if k in dict_1.keys():
            dict_1[k].extend([v.strip('\t\n')])
        else:
            dict_1[k] = [v]

        # -------------------------- #

        # dictionary of file 2

        dict_2 = {}

        for line in text2:
            l, w = split2words(line)
        l = l.upper()
        dict_2.setdefault(l, [])

        if l in dict_2.keys():
            dict_2[l].extend([w.strip('\t\n')])
        else:
            dict_2[l] = [w]

        # ordered by hostname
        # Dict 1 printed 'nicely'
        for k, v in sorted(dict_1.items()):
            print(k, '\t', v)

        # Break
        print('\t', '\n', '\t')
        print('\t', '#================#', '\t')
        print('\t', '\n', '\t')

        # Dict 2 printed 'nicely'
        for l, w in sorted(dict_2.items()):
            print(l, '\t', w)

        print('\n\t', 'Lines in file 1: ', len(dict_1) - 1, '\n\t', 'Lines in file 2: ', len(dict_2) - 1)

        print('\t', '\n', '\t')
        print('\t', '#================#', '\t')
        print('\t', '\n', '\t')

        # prints hosts who have 'blank' IPs
        print('\n', "File 1:", '\n')
        for k, v in sorted(dict_1.items()):
            if
        v == ['']:
        print('Hosts without IPs: ', k, '\t', v)
        '\n'
        print("File 2:", '\n')
        for l, w in sorted(dict_2.items()):
            if
        w == ['']:
        print('Hosts without IPs: ', l, '\t', w)

        print('\t', '\n', '\t')
        print('\t', '#================#', '\t')
        print('\t', '\n', '\t')

        compare(dict_1, dict_2)


        )
    reset = input('Run script again? (y/n):   ')

return