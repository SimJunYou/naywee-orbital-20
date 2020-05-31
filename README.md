# naywee-orbital-20
Team Naywee's Orbital 20 Project

## OVERALL

There are 2 main branches: `master` and `website`. `master` is really the Telegram bot branch, and the `website` branch holds both the React frontend and the Express backend.

We are using Heroku as the deployment platform for our project. 2 separate Heroku apps are used, one for the bot and one for the website front/backend. We have also provisioned a Postgres database addon for the website app, making the Express backend serve as a RESTful API server for it.

## TELEGRAM BOT BRANCH

### Structure

This branch is for the Telegram bot. Heroku will deploy the latest commit of this branch.

### Deploying

The only file that needs to be run in here is `main.py`. Hence, in `Procfile` (used by Heroku to determine what to run), we just put `python main.py`. The `Pipfile` stores the `pip` requirements for our bot (like `package.json` and `npm` for Node). Heroku installs everything needed as stated in `Pipfile` and then runs `main.py`.

## WORKFLOW

Some basic Git references below.

### Setting up workspace

* After you cloned this repo, everything should be up to date. You will have a `master` branch locally and your remote branches will be there too.
   * You can do `git remote show` to check your remote branches.
   * To make the local versions of remote branches, just do `git checkout <branch>`. Git will automatically turn it into a local branch that tracks that remote branch with the same name.

### Pulling before each work session

* Do a `git pull origin master` before you start working each time. This keeps the other branches updated too... just in case.
* `git branch` to ensure you're in your own branch before you start working.

### Pushing after each work session

* First, `git add .` if you want to stage all files or `git add <path/to/file>` if you want to add specific files.
* `git commit -m 'commit message here'` followed by `git push origin <branch>:<branch>` or just `git push origin master` (only if you know what you're doing!)

### Rolling back

* Undoing a local commit: Do `git revert HEAD`. `git revert` works by bringing your previous commit in as a new commit to undo what you did so far.
   * `HEAD` refers to your current commit (which is the one you wanna undo).
   * If you want to revert back to BEFORE a specific commit, use `git log` and find the commit hash (a long string of characters) and do `git revert <hash>`
* Undoing a push to remote: Do `git push -f origin <hash>:<branch>`.
   * This forces a push of the `<hash>` commit, which is the one you want to revert to, to the specified remote
 branch in `<branch>`. Use `git log` to find the hash.
   * You can undo the local commit first, then `git push -f origin master:<branch>` instead of finding a specific commit.
* Hard reset:
   * First, try doing `git fetch` then `git reset --hard origin/<branch>`.
   * If that doesn't work, delete everything in your repo except the .git folder, download from the Github repo page (green button on top right of file window), put everything in the same folder, then `git add *`, `git commit`.
