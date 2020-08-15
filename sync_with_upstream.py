#########################################################################################################
#                                                                                                       #
#       This program allows you to automatically synchronize all forked submodules with upstream        #
#                                                                                                       #
#                                    written by sungminyou                                              #
#                                                                                                       #
#########################################################################################################
import os
import subprocess
count = 0
def traverse_subdir(root_dir):
    global count
    files = os.listdir(root_dir)
    total = len(files)
    print(files)
    for file in files:
        if os.path.isdir(file):
            print('\nstart refresh ' + '** ' + file + ' **'+ ' repository')
            print('Do you want to refresh the repository where you are currently located?')
            option = input('[y/n] >>> ')
            if(option == 'n'): continue
            count += 1
            print('진행도 : ' + str(count) + '/' + str(total))
            print()
            path = root_dir + '\\'
            path += file
            os.chdir(path)
            os.system('sh ../sync.sh')
            print()
            print(file +' repository successfully refresh')
            os.chdir(root_dir)
        else:
            total -= 1
root_dir = "D:\git\Problem-Solving"
traverse_subdir(root_dir)