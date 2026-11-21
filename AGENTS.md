# Contributor guidance

- The site builds with Pelican and `pelican-yaml-metadata`, deploys through GitHub Actions to GitHub Pages, and is fronted by an SRCF redirect. Pages CMS configuration lives in `.pages.yml`.
- Keep `.pages.yml` field definitions synchronized with metadata keys used by the theme templates.
- Keep `content/admin/index.html` excluded from Pelican content parsing so it is copied as a static file.
- Never commit secrets or SSH keys.
