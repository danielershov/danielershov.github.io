# Website Principles

This site is designed as a maintainable academic website rather than a marketing page. The Research page is the main archival surface: dense citation rows, client-side filters, stable slugs, and BibTeX export.

The repository keeps source content in Markdown, reusable site data in `hugo-site/data/`, static files in `hugo-site/static/`, and template behavior in `hugo-site/layouts/`. URLs should remain stable after publication; change titles in front matter rather than renaming content folders.

The visual system uses UCL's official purple-led palette with off-white surfaces and dense typography for academic browsing. The site forces light mode, includes keyboard-visible focus states, and uses Pagefind for static search.

Deployment is handled by GitHub Actions. Pushing to `main` will build Hugo, build the Pagefind index, and deploy to GitHub Pages. Review locally before pushing.
