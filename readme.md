5. Commit your code and push
powershell
git add .
git status
git commit -m "Add my MERN code"
git push -u origin main

git status is worth checking before committing, so you can confirm node_modules and .env aren't listed. On the first push, a browser window should pop up asking you to sign in to GitHub. Approve it and the push will continue.

6. Your daily routine

Every day, from E:\WEBDEV:

powershell
git add .
git commit -m "Describe what you did today"
git push

If you work on more than one computer, run git pull before you start working.

7. Optional: automate the daily push


