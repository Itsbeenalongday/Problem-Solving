echo "###############################################################"
echo "#                                                             #"
echo "#                                                             #"
echo "#                                                             #"
echo "#                                                             #"
echo "#    fork repository synchronization  auto script ver 1.0     #"
echo "#                                                             #"
echo "#                                                             #"
echo "#                 written by sungminyou                       #"
echo "#                                                             #"
echo "###############################################################"
echo -e "\n"
echo "*** check remote repository ***"
echo -e "\n"
git remote -v
echo -e "\n"
while true; do
    read -p "add remote repository? [y/n] >> " option
    if [ "$option" == "y" ] || [ "$option" == "n" ]; then
        break
    else
        echo "Invaild input please enter y or n"
        continue
    fi 
done
if [ $option == "y" ]; then
    git remote remove upstream
    echo -en "please type remote repository url >>> "
    read url
    git remote add upstream "$url"
    echo -e "\n"
    echo "*** check remote repository ***"
    echo -e "\n"
    git remote -v
    echo -e "\n"
    echo "*** fetch remote repository ***"
    echo -e "\n"
    git fetch upstream
    echo -e "\n"
    echo "*** merge remote/local repository ***"
    echo -e "\n"
    git merge upstream/master
    echo -e "\n"
    echo "*** push ***"
    echo -e "\n"
    git push origin master
    echo -e "\n"
    echo "*** pushing successfully done ***"
    echo -e "\n"
elif [ $option == "n" ]; then
    echo "*** fetch remote repository ***"
    echo -e "\n"
    git fetch upstream
    echo -e "\n"
    echo "*** merge remote/local repository ***"
    echo -e "\n"
    git merge upstream/master
    echo -e "\n"
    echo "*** push ***"
    echo -e "\n"
    git push origin master
    echo -e "\n"
    echo "*** pushing successfully done ***"
    echo -e "\n"
fi