# Nitin Gupta Portfolio

This repo contains a static single-page portfolio. It does not
require a bundler, package install, generated runtime, or client-side framework.

## Files

- `index.html` - portfolio content, sections, contact links, and metadata.
- `assets/css/styles.css` - self-hosted font declarations and shared global/hover styles.
- `assets/fonts/` - local `.woff2` font files extracted from the export.
- `assets/profile.jpg` - optimized portrait image with metadata stripped.
- `assets/projects/` - project preview screenshots used by the portfolio cards.
- `404.html` - simple fallback redirect for static hosts.
- `.nojekyll` - disables GitHub Pages Jekyll processing.

## Preview

Open `index.html` in a browser, or serve the folder locally:

```sh
python3 -m http.server 8000
```

Then visit `http://localhost:8000`.
