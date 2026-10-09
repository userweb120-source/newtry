# Raafat Agha — unofficial reconstruction (English)

Static, dependency-free reconstruction of https://www.raafat.ninja/ (single page). No build step, no `package.json`: plain HTML/CSS/JS.

## Run locally
```bash
python3 scripts/check.py        # static checks
python3 -m http.server 8000     # open http://localhost:8000
```

## Images (optional)
Add your own files (the page falls back to placeholders if missing):
`assets/me.jpeg`, `assets/projects/{systemscart,jamrtech,soviez,hostingcart,aqrmenu}.jpg`

## Deploy to GitHub Pages
1. Push to `main` (commands below).
2. Repo → **Settings → Pages → Source: GitHub Actions**.
3. The workflow in `.github/workflows/pages.yml` runs the checks and publishes. URL: `https://<USERNAME>.github.io/<REPO>/`.
4. Update later: edit, `git add -A && git commit -m "msg" && git push`.

All paths are relative, so it works under the `/<REPO>/` subpath. Single page, so no client-side routing is needed.

## Upload
```bash
git init -b main
git add -A
git commit -m "Initial commit"
git remote add origin https://github.com/<USERNAME>/<REPO>.git
git push -u origin main
```

## Verified vs not
Verified: static link/asset check, JS syntax check, local server returns 200 for `/`, `/404.html`, 404 for unknown paths.
Not verified: rendering in a real browser, interactions, screenshots, responsive layouts, Pages workflow run.

## Limitations
English only (the original also has `/ar/index.html`, not built). Colors, fonts and spacing are estimates, not measured. Domain lookup, email reveal and contact form are demos; nothing is sent. The original `/notes/` link returns 404 and is not reproduced. Content belongs to its author; use only if the site is yours or you have permission.
