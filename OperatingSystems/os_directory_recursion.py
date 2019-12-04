import os


def list_directories(s):
    def dir_list(d):
        nonlocal tab_stop
        files_ = os.listdir(d)
        for f in files_:
            current_dir = os.path.join(d, f)
            if os.path.isdir(current_dir):
                print('\t' * tab_stop + 'Directory ' + f)
                tab_stop += 1
                dir_list(current_dir)
                tab_stop -= 1
            else:
                print('\t' * tab_stop + f)

    tab_stop = 0
    if os.path.exists(s):
        print('Directory listing of ' + s)
        dir_list(s)
    else:
        print(s + ' does not exist')


print('\nMETHOD #1\n')
listing = os.walk('.')

for root, directories, files in listing:
    print(root)
    for di in directories:
        print(di)
    for file in files:
        print(file)

print('\nMETHOD #2\n')
list_directories('.')
