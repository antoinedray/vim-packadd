mkdir ~/.scripts
chmod u+x packadd.sh
cp packadd.sh ~/.scripts
alias packadd="/bin/sh ~/.scripts/packadd.sh" >> ~/.bashrc
alias packadd="/bin/sh ~/.scripts/packadd.sh" >> ~/.bash_profile
