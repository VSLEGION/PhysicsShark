# PhysicsShark Team Creator

A buildless HTML/CSS/JS team-creator for GitHub Pages. One teammate enters the full aerospace startup team after the group discusses its approach. Students choose the AE 107 role for each member, select skill levels, nominate one Shark, and record the challenge card. The host dashboard shows submissions, creates room codes, stores a challenge prompt, and supports JSON export/import.

## Run on GitHub Pages

Upload `index.html`, `styles.css`, `app.js`, and `README.md` to a repository. In GitHub, open **Settings → Pages**, choose the branch and root folder, then share the published URL.

## Storage note

GitHub Pages is static hosting, so browser `localStorage` is the default and is private to each computer. For a real classroom-wide shared board, create a Firebase Realtime Database and set `FIREBASE_CONFIG` near the top of `app.js` to `{databaseURL:'https://YOUR-PROJECT-default-rtdb.firebaseio.com'}`. This app uses Firebase's REST endpoint, so no Firebase SDK is needed. Configure database rules appropriate to your class; the simplest classroom setup is temporary public read/write access while the activity is running, then lock it down afterward. The UI labels the storage mode and keeps JSON export/import as a backup.

After configuring the database, upload the updated files and click **New room** in the host dashboard to register a shared room. Give that one code to all sections. Teams can optionally enter their section. Shared submissions are written individually so simultaneous submissions do not overwrite the entire room. Public database rules allow anyone with access to read or modify student data; use suitable rules and avoid collecting sensitive information.
