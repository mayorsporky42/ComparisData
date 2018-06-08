import filecmp

f1 = open('carsip.txt')
f2 = open('dns.txt')
if filecmp.cmp(f1, f2, shallow=True):
    print('These files are the same.')
elif f1.read() != f2.read():
    f1_line = f1.readline()
    f2_line = f2.readline()
    print('Lines in 1file: ', len(f1), 'Lines in 2file: ', len(f2), '\n', 'These files are different')



    # with open('carsip.txt') as f1:
    #     with open('dns.txt') as f2:
    #         if f1.read() == f2.read():
    #             print('These files are the same.')
    #         elif f1.read() != f2.read():
    #             f1_line = f1.readline()
    #             f2_line = f2.readline()
    #             print('Lines in 1file: ', len(f1), 'Lines in 2file: ', len(f2), '\n', 'These files are different')