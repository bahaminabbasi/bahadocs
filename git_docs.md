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


