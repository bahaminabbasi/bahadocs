# Git Commands and Tips



## Viewing Changes

### To view changes between the latest commit and the one before it:
    git diff <commit_hash_1>..<commit_hash_2>


## Viewing Changes in a Specific File

### To view changes in a specific file between the latest commit and the one before it:
    git diff HEAD~1..HEAD -- file_name.py
##### this can be like HEAD~5..HEAD , for showing 5th commit before lates

## Viewing Commit History

### To view the commit history with a one-line summary of each commit:
    git log --oneline



--------------------------------------------------------------------------------------------
git log -p 43dff46..58a0ad6
  You can display the commit logs and show the difference introduced at each commit using:

--------------------------------------------------------------------------------------------

git log --stat 43dff46..58a0ad6
  For a more concise summary that lists each commit with the changed files, you could use:
--------------------------------------------------------------------------------------------

git diff 43dff46..58a0ad6 -- accounts/models.py
  If you want to see the exact changes made to a specific file, use:
--------------------------------------------------------------------------------------------