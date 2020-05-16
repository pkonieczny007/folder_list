import os

exception = ['folder_list.py',
             'folder_list.txt']

with open('folder_list.txt', 'a') as f:
    
    for filename in os.listdir():
        if filename in exception:
            pass
        else:
            print(filename)
            filename += '\n'
            f.write(filename)
    end = '\n************\n'
    f.write(end)
        
