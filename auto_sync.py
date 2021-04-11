#########################################################################################################
#                                                                                                       #
#       This program allows you to automatically synchronize all forked submodules with upstream        #
#                                                                                                       #
#                                    written by sungminyou                                              #
#                                                                                                       #
#########################################################################################################
import os
import subprocess
def traverse_subdir():
    path = os.getcwd()
    subdirs = [subdir.name for subdir in os.scandir(path) if not subdir.name.startswith('.')]
    subdirs = [subdir for subdir in subdirs if os.path.isdir(os.path.join(path, subdir))]
    total_works = len(subdirs)
    count = 0
    for subdir in subdirs:
        count += 1
        print('진행도 : {count} / {total}'.format(count=count, total=total_works))
        print(f'{subdir} 디렉토리의 싱크를 맞춥니다.')
        print('계속 진행하시겠습니까?')
        option = input('[y/n] >>> ')
        if(option == 'n'): continue
        subdir_path = os.path.join(path,subdir)
        os.chdir(subdir_path)
        origin_url = subprocess.getoutput("git remote get-url --push origin")
        if not "Itsbeenalongday@" in origin_url:
            print("origin remote push 권한 부여")
            origin_url = origin_url[:8] + "Itsbeenalongday@" + origin_url[8:]
            os.system(f"git remote set-url origin {origin_url}")
        if os.path.exists('git.sh'):
            os.system('sh git.sh')
        else:
            print(f"{subdir}디렉토리에 git.sh가 존재하지 않습니다. 상위 디렉토리에서 복사합니다.")
            os.system('cp ../git.sh .')
            os.system('sh git.sh')
        os.chdir(path)
    os.system('sh git.sh')

traverse_subdir()

# local 계정 변경
# os.system("git config --local user.name 'Itsbeenalongday'")
# os.system("git config --local user.email 'dbtjdals1771@ajou.ac.kr'")
