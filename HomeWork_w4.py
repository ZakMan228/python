#Задание _1
def song_generator(row_count=3, la_count=3, end=0):
    list = []
    for i in range(0, la_count):
        list.append('la')
    line = '-'.join(list) + '\n'
    song = (line * row_count)[0:-1]
    if end == 0:
        song += '.'
    else:
        song +='!'
    return song
r_count = int(input('Enter row count: '))
l_count = int(input('Enter la count: '))
end = int(input('Ending value: '))

print (song_generator(r_count, l_count, end))
print('\n')
print('default call')
print(song_generator())


#Задание_2

def get_second_max(*args):
    arg_set = set(args)
    uniq_args = list(arg_set)
    uniq_args.sort()
    return uniq_args[1]
print(get_second_max(2, 6, 3, 4, 3))