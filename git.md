# Git & Github

## Basic Commands

<pre>
$ git init          Initialize Local Git Repository
$ git add {file}    Add File(s) To Index
$ git status        Check Status Of Working Tree
$ git commit        Commit Changed in Index
$ git push          Push To Remote Repository
$ git pull          Pull Latest From Remote Repository
</pre>


## Example

<pre>
$ git --version     Check Version

Create File within Git Bash
$ touch index.html

Initialize
$ git init

$ git config --global user.name 'Surname Lastname'
$ git congig --global user.email 'email@domain.ch'

Add file
$ git add index.html

Add all files
$ git add .

Add all html files
$ git add *.html

Check cached files
$ git status

Remove cached files
$ git rm --cached index.html

Validate files and commit
$ git commit -m 'Comment'
</pre>

## .gitignore

<pre>
Create .gitignore
$ touch .gitignore

You can add filename or folders in the gitignore file.
log.txt             Normal file
/dir2               Folders

Those files won't be added and comitted.
</pre>

## Create a Branch

<pre>
Create a branch called login
$ git branch login

Switch to branch
$ git checkout login

Create a file in branch login and commit it
$ touch login.html
$ git add .
$ git commit -m 'login form'

Switch back to master
$ git checkout master

Merge Branch with Master
$ git merge login
</pre>

## Push to Github Repo

<pre>
Create a new Repository on Github
Copy and Paste Github setup for the Repo
$ git remote add origin https://github.com/githubUsername/Reponame.git

$ git push -u origin master
</pre>
