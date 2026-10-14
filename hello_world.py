print("Git is awesome!")

"""
1. The Git Status command output.
git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   hello_world.py

no changes added to commit (use "git add" and/or "git commit -a")  

2. git add command after git status command.
git add hello_world.py

3. git status command after git add command.
git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   hello_world.py

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   hello_world.py
        
4. Changed Hello World to Git is awesome!

5. git status again
git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   hello_world.py

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   hello_world.py
        
6. git add to stage the changes
git add hello_world.py

7. git commit -m "Changed Hello World to Git is awesome!"
[master 1a2b3c4] Changed Hello World to Git is awesome!

"""