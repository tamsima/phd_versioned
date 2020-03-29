# This script explains how to version control other codes
# Initial set up
git config --global user.name "Tamara Mathys"

git config --global user.e-mail "tamara.mathys@unifr.ch"

git config --global core.editor "nano"

# Creating a Version-Controlled Directory: Create a directory, then tell Git to track
# versions of files in this directory using the command git init
# Important: You have to cd to the directory first!
git init

# AddingFiles to be versioned
 git status # checks what Git "knows" about the file

 git add filename.extension 

 # Committing Changes:
 git status
 git commmit -a 

 # This will open the text editor where you can add a commit message

 git status # to see what has changed

 # Pushing to the cloud:
 git checkout master
 ls -a 

 git remote add origin https://gitbhub.com/tamsima/phd_versioned

 git push -u origin master

 git push