import os

'''The program checking and write file in his folder'''

#wyjątki
exception = ['folder_list.py',
             'folder_list.txt'] 

#counter start
counter = 0

with open('folder_list.txt', 'a') as f:
    
    for filename in os.listdir():
        if filename in exception:
            pass
        else:
            print(filename)
            counter += 1
            filename += '\n'
            f.write(filename)
            
    counter = str(counter) + ": files in folder"
    f.write(counter)
    end = '\n************\n'
    
    f.write(end)
    


