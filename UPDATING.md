# Updating Daniel Ershov's Website

The site is a Hugo website in `hugo-site/`. Most updates are ordinary Markdown edits.

## Add a Paper

Copy an existing folder under `hugo-site/content/publication/`, rename the folder with a stable slug, and edit `index.md`. Keep the front matter fields `title`, `date`, `authors`, `publication_types`, `publication`, `status`, `areas`, `tags`, `abstract`, and `links`.

Use `status: "published"` for journal articles, `status: "working_paper"` for active working papers, `status: "policy"` or `status: "cepr_contribution"` for policy writing, and `status: "resting"` for resting papers. The Research page tabs are generated from this field.

## Update the C.V.

Replace `hugo-site/static/files/DErshov_CV_SES_2026.pdf` with the new PDF and keep the filename stable, or update the links in `hugo-site/data/profile.json` and `hugo-site/content/bio/_index.md`.

## Update Research Areas

Edit `hugo-site/data/research_areas.json`. The homepage accordions and the Research page area filter read this file.

## People Page

The People page has separate coauthor and PhD student sections. Coauthors are auto-populated from publication front matter, with external links stored in `hugo-site/data/coauthors.json`. PhD students are stored in `hugo-site/data/phd_students.json`.

## Preview Locally

From `hugo-site/`, run:

```bash
hugo server --buildDrafts --disableFastRender
```

The local preview is private to your machine. Nothing goes public until changes are pushed to GitHub and the Pages workflow runs.
