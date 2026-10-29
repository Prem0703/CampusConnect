# CampusConnect — Lost & Found

A Django campus lost-and-found website with signup/login, reports, item claims, and a mobile-installable PWA shell.

## Run locally

1. Extract ZIP and open the folder containing `manage.py`.
2. Run `RUN_CAMPUSCONNECT.bat` on Windows.
3. Visit http://127.0.0.1:8000/.

## GitHub safety

`.gitignore` excludes local SQLite databases, media uploads, virtual environments, and `.env` secrets. Never commit production secrets or private user data.

## Deployment

A starting `render.yaml` is included. Review the hosting plan and settings before deployment. Persistent image storage is not configured in this starter.

## Android

After HTTPS deployment, open the website in Android Chrome and use **Install app / Add to Home screen**. This is a PWA install, not a Play Store APK.

Created by ®_prem
