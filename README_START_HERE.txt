CAMPUSCONNECT — READY PACK (Windows + GitHub + Web + Android install)
=====================================================================

1) LOCAL WEBSITE (Windows)
- Extract this ZIP using Extract All.
- Open the extracted campusconnect folder in VS Code (the folder containing manage.py).
- Double-click RUN_CAMPUSCONNECT.bat. First run needs internet and Python 3.10+.
- Open http://127.0.0.1:8000/ in your browser.
- Admin: http://127.0.0.1:8000/admin/
- If you need an admin user, keep the server open, open a second VS Code terminal and run:
  .\venv\Scripts\python.exe manage.py createsuperuser

2) GITHUB (your repository already exists)
- This ZIP intentionally excludes db.sqlite3, uploaded media, virtualenv and secrets.
- Do NOT upload your old project database or .env file.
- Easiest safe method: install GitHub Desktop from https://desktop.github.com/
  then File > Add Local Repository > choose this extracted folder.
  If it says it is not a repository, choose Create a Repository there.
  Review changes; ensure db.sqlite3, venv, media and .env are NOT listed.
  Commit to main, then Publish repository / Push origin to your existing GitHub repo.
- If you prefer command line, use the separate PUSH_TO_GITHUB_GUIDE_MARATHI.txt.

3) PUBLIC WEBSITE (Render)
- render.yaml is included as a starting blueprint. Push code to GitHub first.
- Sign in at https://render.com/ and create a new Blueprint from the repository.
- Review the database/service plan and availability shown in your account before creating.
- Free plans/limits can change; a free web service may sleep.
- After deployment, create admin with Render Shell: python manage.py createsuperuser
- Uploaded images need persistent/object storage for a production launch; this starter does not configure that.
  Do not advertise it widely until you verify signup, login, posting, claiming, admin, backups and image uploads.

4) ANDROID APP (installable web app / PWA)
- Once the public website works over HTTPS, open its URL in Chrome on Android.
- Chrome menu (three dots) > Install app or Add to Home screen.
- This creates an installable app shortcut using the website. It is NOT an APK and is not yet on Google Play.
- Publishing a Play Store APK/AAB is a separate packaging and developer-account step.

IMPORTANT
- No ZIP can guarantee zero errors on every computer. Python and internet access are required on first local run.
- This ZIP does not contain your old database/users, to avoid accidentally sharing private data. Create a new admin if needed.
- Keep a backup of your current working folder before replacing anything.
