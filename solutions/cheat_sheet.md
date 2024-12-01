# Git & Codespaces Teaching Cheat Sheet

## 🚀 Getting Started
```bash
# Check current status
git status

# Stage and commit
git add filename     # Stage specific file
git add .            # Stage all files
git commit -m "message"

# Push and pull
git push            # Send to GitHub
git pull            # Get latest changes
```

## 🌿 Branching
```bash
# Create branches
git branch new-branch           # Create branch
git checkout -b new-branch      # Create and switch
git checkout branch-name        # Switch branches

# Update branches
git pull origin main           # Get updates from main
git merge main                 # Merge main into your branch
```

## 🔄 Syncing
```bash
# Add remote
git remote add origin URL
git remote -v                  # View remotes

# Push to remote
git push -u origin branch-name  # First push
git push                        # Subsequent pushes
```

## 🆘 Fixing Mistakes
```bash
# Undo uncommitted changes
git checkout -- filename       # Undo file changes
git restore filename          # New way to undo changes
git reset --hard             # Undo all changes

# Fix commits
git reset --soft HEAD~1      # Undo last commit, keep changes
git reset --hard HEAD~1      # Undo last commit, delete changes
git commit --amend          # Edit last commit message
```

## 🔀 Merge Conflicts
```bash
# When conflict occurs:
1. Open conflicted files
2. Look for <<<<<<< HEAD
3. Choose changes to keep
4. Remove conflict markers
5. git add .
6. git commit
```

## 👥 Common Student Issues & Fixes
```bash
# Wrong branch
git checkout -b new-branch    # Create new branch here
git checkout main            # Go back to main
git reset --hard HEAD~1      # Undo changes in main

# Lost changes
git reflog                   # See recent activity
git checkout HEAD@{1}        # Go back to previous state

# Mess up merge
git merge --abort           # Cancel merge
git reset --hard HEAD       # Start over
```

## 💻 Codespaces Tips
- Use Source Control panel (Ctrl/Cmd + Shift + G)
- Green "Sync Changes" button pushes and pulls
- Branch name shows in bottom left
- Terminal available with Ctrl/Cmd + `

## 📝 Best Practices for Teaching
1. Always create new branch for features
2. Commit often with clear messages
3. Pull before starting new work
4. Push regularly to backup work

## 🚫 Common Gotchas
- Can't push: Run `git push -u origin branch-name` first time
- Can't pull: Save/commit local changes first
- Wrong branch: Check bottom left of VS Code
- Merge conflict: Don't panic, check conflict markers

## 🔑 Key Commands for Teachers
```bash
# Setup
git clone URL                  # Get repository
git checkout -b student-work   # Create student branch

# Review
git log                        # View history
git diff                       # See changes
git blame filename            # Who changed what

# Cleanup
git branch -d branch-name     # Delete branch
git clean -fd                 # Remove untracked files
```

## 🆘 Emergency Fixes
```bash
# Reset to last known good state
git reset --hard origin/main

# Recover deleted branch
git reflog
git checkout -b recovered-branch HEAD@{1}

# Cancel merge
git merge --abort
```
