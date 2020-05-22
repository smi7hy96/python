def load_file(filename):
    file = open(filename, 'r').readlines()
    names_list = [line.rstrip('\n') for line in file]
    return names_list

print(sorted(load_file('../GroupRandomiser/names.txt')))