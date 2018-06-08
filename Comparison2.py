# File Comparison Script #
# When comparing files, export the files as .txt or .csv files #
# The output will be in the format of ">" for any files in first document, "<" for any files in second document #
# The files should be sorted within the program so that the contents of the files match up by line.. #
# ..or at least alphabetically #

import xlsxwriter

print("Please input the files you wish to compare", "\n",
      "Example: somedata.txt - or - datasome.csv", "\n",
      "..............................................")

# user generated input of file names

fname1 = input("First File: ")
fname2 = input("Second File: ")


f1 = open(fname1)
f2 = open(fname2)


text1 = f1.readlines()
text2 = f2.readlines()


# Show what files are being opened/compared
print('\n', '...', '\n', 'files opened', '\n', '...')

print('\n')
print("-----------------------------------------")
print("Comparing files: " " f1> " + fname1, " f2< " + fname2, sep=',')
print("-----------------------------------------")


# Definition to get a key and value from each file
# Will append a blank value in dictionary for any blank values


def split2words(line):

    try:
        words = line.split('\t', 1)
        if len(words) != 2:
            words.append('')
    except ValueError:
        words = ['', '']
    return words


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


# printed 2-column lists dict 1 and 2

# ordered by hostname
# Dict 1 printed 'nicely'
# for k, v in sorted(dict_1.items()):
#     print(k, '\t', v)


# print('\t', '\n', '\t', '#==================================================#', '\t', '\n', '\t')


# Dict 2 printed 'nicely'
# for l, w in sorted(dict_2.items()):
#     print(l, '\t', w)

print('\t', '\n', '\t', '#==================================================#', '\t', '\n', '\t')


# prints the length of each
print('\n\t', 'Lines in file 1: ', len(dict_1)-1, '\n\t', 'Lines in file 2: ', len(dict_2)-1)
print('\n\t', 'Difference: ', len(dict_1)-len(dict_2)-4)

print('\t', '\n', '\t', '#==================================================#', '\t', '\n', '\t')


print("This section identifies Hosts that do not have IP addresses: ", '\n')

# prints hosts who have 'blank' IPs
print('\n', '\t', f1.name, ":", '\n')
for k, v in sorted(dict_1.items()):
    if v == ['']:
        print('Host without IPs: ', k, '\t', v)
    elif v != ['']:
        continue

print('\n', '\t', f2.name, ":", '\n')
for l, w in sorted(dict_2.items()):
    if w == ['']:
        print('Host without IPs: ', l, '\t', w)
    elif w != ['']:
        continue


print('\t', '\n', '\t', '#==================================================#', '\t', '\n', '\t')

print("This section identifies Hostnames with multiple or conflicting ip addresses:", '\n')


def compare(first, second):
    sharedkeys = set(first.keys()).intersection(second.keys())
    for key in sharedkeys:
        if first[key] != second[key]:
            print('Hostname: {}, \t IP Address 1: {}, \t IP Address 2: {}'.format(key, first[key], second[key]), '\n')


compare(dict_1, dict_2)
compare(dict_1, dict_1)
compare(dict_2, dict_2)

print('\t', '\n', '\t', '#==================================================#', '\t', '\n', '\t')

print('This section lists Hosts that are in only one file and not the other:', '\n')

dict_3 = {}

difference = {k: dict_2[k] for k in set(dict_2) - set(dict_1)}


print(difference)

# for line in text1:
#     k, v = split2words(line)
#     k = k.upper()
#     dict_1.setdefault(k, [])
#
#     if k in dict_1.keys():
#         dict_1[k].extend([v.strip('\t\n')])
#     else:
#         dict_1[k] = [v]
#
# for k in dict_3:
#     if k in dict_3.keys():
#         dict_3[v].extend([v.strip('\t\n')])
#     else:
#         dict_3[k] = [v]
#     print(k, '\t', v)


print('\t', '\n', '\t', '#==================================================#', '\t', '\n', '\t')

# Writing to an Excel file:
# workbook = xlsxwriter.Workbook('compare1.xlsx')
# worksheet = workbook.add_worksheet()
#
# Add a bold format to use the highlight cells
# bold = workbook.add_format({'bold': True})
#
# Add a number format for the cells with numbers
# IP addresses = workbook.add_format({'num_format': '###.###.###.###'})
#
# Data Headers
# worksheet.write('A1', 'Hostname', bold)
# worksheet.write('B1', 'IP Address', bold)
#
# worksheet.write('A1', 'Hello world')
#
# workbook.close()

# Writing to a txt/csv file:
# with open(f1) as file1:
#     with open(f2) as file2:
#         same = set(file1).intersection(file2)
#
# same.discard('\n')
#
# with open('some_output_file.txt', 'w') as file_out:
#     for line in same:
#         file_out.write(line)
#
#
# # Makes a new file in the folder with a name given by the user #
# print('\n', "~~ Please input a valid destination file name below ~~", '\n\t')
# fname3 = input("Destination file: ")
# with open(fname3, "a+") as f:
#     f.write("comparison2")
# print("Comparison Destination: " + fname3)

f1.close()
f2.close()
