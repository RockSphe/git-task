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

8. git log -n 8 Shows me the past 8 commits in the repository.

commit 3049bf6c3cbe4437ec332addc896a02324eb79f1
Author: Siphesihle Khumalo <siphesihlekhumalo@Siphesihles-MacBook-Pro.local>
Date:   Sat Oct 3 10:30:07 2026 +0200

    txt file answers - git

commit 9bb2482b51bce7b75f90af38917eb5b31c9d800a
Author: Siphesihle Khumalo <siphesihlekhumalo@Siphesihles-MacBook-Pro.local>
Date:   Sat Oct 3 10:15:32 2026 +0200

    Corrected output message to Create task_folder_1, task_folder_2, task_folder_3

commit f4bff9eff98d1cb4ad72b8ce91fcf16fa19579b2
Author: Siphesihle Khumalo <siphesihlekhumalo@Siphesihles-MacBook-Pro.local>
Date:   Fri Oct 2 17:27:49 2026 +0200

(base) siphesihlekhumalo@Siphesihles-MacBook-Pro M03T09 – Version Control and Git Basics % clear
(base) siphesihlekhumalo@Siphesihles-MacBook-Pro M03T09 – Version Control and Git Basics % git log -n 8
commit 2927938287aa5eaf8a41478e80892a64d5979476 (HEAD -> main)
Author: Siphesihle Khumalo <siphesihlekhumalo@Siphesihles-MacBook-Pro.local>
Date:   Wed Oct 14 08:04:39 2026 +0200

    Commiting outdated changes

commit a568481ebcdac55d305dc274016c11bda5f3330b (origin/main, origin/HEAD)
Author: Siphesihle Khumalo <siphesihlekhumalo@Siphesihles-MacBook-Pro.local>
Date:   Thu Oct 8 14:34:13 2026 +0200

    Re-submission My Database Theory

commit d7c9aba6e7727e6bed5357ef7b1525357dd09305
Author: Siphesihle Khumalo <siphesihlekhumalo@Siphesihles-MacBook-Pro.local>
Date:   Tue Oct 6 16:18:17 2026 +0200

    Submission MyDatabaseTheory

commit f4f14b1ce7c134867b09e31696dd513552d16a3b
Author: Siphesihle Khumalo <siphesihlekhumalo@Siphesihles-MacBook-Pro.local>
Date:   Mon Oct 5 06:07:59 2026 +0200

    Task manager - project submission

commit 3049bf6c3cbe4437ec332addc896a02324eb79f1
Author: Siphesihle Khumalo <siphesihlekhumalo@Siphesihles-MacBook-Pro.local>
Date:   Sat Oct 3 10:30:07 2026 +0200

    txt file answers - git

commit 9bb2482b51bce7b75f90af38917eb5b31c9d800a
Author: Siphesihle Khumalo <siphesihlekhumalo@Siphesihles-MacBook-Pro.local>
Date:   Sat Oct 3 10:15:32 2026 +0200

    Corrected output message to Create task_folder_1, task_folder_2, task_folder_3

commit f4bff9eff98d1cb4ad72b8ce91fcf16fa19579b2
Author: Siphesihle Khumalo <siphesihlekhumalo@Siphesihles-MacBook-Pro.local>
Date:   Fri Oct 2 17:27:49 2026 +0200

    Submission shell script 2

commit 49f4b4e70739868ea59ebbb5f767367d14e88e90
Author: Siphesihle Khumalo <siphesihlekhumalo@Siphesihles-MacBook-Pro.local>
Date:   Fri Oct 2 17:19:49 2026 +0200

    submission Shell script 1
    
9. Screenshot of the git log command output uploaded.

"""