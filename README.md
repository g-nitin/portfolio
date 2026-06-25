# Static Portfolio Template

This repo is a cleaned static version of the exported portfolio mockup. It does
not require a bundler, package install, generated runtime, or client-side
framework.

## Files

- `index.html` - content, sections, contact links, and metadata.
- `assets/css/styles.css` - self-hosted font declarations and shared global/hover styles.
- `assets/fonts/` - local `.woff2` font files extracted from the export.
- `assets/profile.jpg` - optimized portrait image with metadata stripped.
- `404.html` - simple fallback redirect for static hosts.
- `.nojekyll` - disables GitHub Pages Jekyll processing.

## Editing

Update profile details, projects, publications, email address, and social
handles directly in `index.html`. Replace `assets/profile.jpg` with a new
optimized image when needed.

## Preview

Open `index.html` in a browser, or serve the folder locally:

```sh
python3 -m http.server 8000
```

Then visit `http://localhost:8000`.

## Deployment

Any static host can publish this from the repository root. For GitHub Pages,
set Pages to deploy from the main branch and root directory.
