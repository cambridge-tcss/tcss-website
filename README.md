# Trinity College Science Society (TCSS) Website

This repository hosts the source code and content for the Trinity College Science Society website (since 2026). The site is built with [Pelican](https://getpelican.com/) and automatically compiled and deployed via GitHub Actions daily and whenever changes are saved in the CMS or pushed to `main`.

---

## Editing Website Content (CMS)

Committee members do not need to edit Markdown files manually or install local development tools. All events, blog posts, pages, and location guides are managed through **Pages CMS**:

1. **Request Access:** Ask the current webmaster or committee to invite your email address via the CMS collaborator settings (no GitHub account is required to edit content).
2. **Open the Editor:** Go to `/admin` on the TCSS website (which redirects to [`app.pagescms.org`](https://app.pagescms.org)) and sign in with your invited email address.
3. **Publish Changes:** Clicking **Save** in the CMS commits your changes directly to this repository and triggers a GitHub Actions build. Updates typically go live within 1–2 minutes.

### Content Sections
* **Events (`content/events/`):** Manage talks, panels, socials, and other society events.
  * **Status:** Set to `published` for the event to appear on the site, or `draft` to hide it.
  * **Event date & time:** Enter dates in `YYYY-MM-DD` format and times in 24-hour format (e.g. `18:30-19:30`).
  * **Event type & Location:** Choose from the dropdown menus (venues with location guides link automatically), or select **Other** and fill in the custom field directly below.
  * **Event ID:** Optional. Set an arbitrary identifier (e.g. `quantum-talk-MT-2026`). Any blog post with a matching **Related event ID** will automatically be linked to from the event page.
* **Blog posts (`content/blog/`):** Publish write-ups, recaps, and announcements, optionally linked to an event via **Related event ID**.
* **Pages (`content/pages/`):** Edit core society pages. Routing fields (`Template`, `URL`, `Save as`) are locked to prevent broken links.
* **Location Guides (`content/pages/location_guides/`):** Update venue directions and paste a Google Maps embed `src` URL into **Google Maps Embed URL** to display an interactive map at the bottom of the page.

---

## Sponsors

Edit `data/sponsors.csv` on GitHub to update the sponsors shown on the homepage:
* Add one row per sponsor using the columns `name`, `logo_file_name`, and `website_url` (`website_url` may be left blank).
* Upload each logo to `content/static/sponsor_logos/` (or via **Media → Sponsor Logos** in the CMS) and enter **only the filename** in the CSV (e.g. `jane_street.png`, not the folder path).
* The sponsor section is hidden automatically when there are no sponsor rows.

---

## Social Media

Edit `data/social_links.csv` on GitHub to update the social media icons shown in the site footer:
* Add one row per account using the columns `name`, `icon_file_name`, and `url`.
* Upload each icon to `content/static/social_logos/` (or via **Media → Social Logos** in the CMS) and enter **only the filename** in the CSV.
* The social media section is hidden automatically when there are no rows.

---

## Annual Committee Handover

When handing over website administration to the incoming committee:
1. **Transfer GitHub Admin Access:** Add the incoming webmaster/president as an **Admin** (or Owner) of this GitHub repository under **Settings → Collaborators**.
2. **Update CMS Collaborators:** Have an admin sign into [`app.pagescms.org`](https://app.pagescms.org) with GitHub, open **Collaborators** for this repository, invite the incoming committee's email addresses, and remove outgoing editors.
