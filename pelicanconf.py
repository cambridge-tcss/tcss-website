import csv
from datetime import datetime, timezone
from pathlib import Path

from pelican import signals


def load_sponsors():
    sponsors_file = Path(__file__).parent / "data" / "sponsors.csv"
    with sponsors_file.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        required_fields = {"name", "logo_file_name", "website_url"}
        missing_fields = required_fields.difference(reader.fieldnames or [])
        if missing_fields:
            raise ValueError(
                f"{sponsors_file} is missing CSV columns: {', '.join(sorted(missing_fields))}"
            )

        sponsors = []
        for row_number, row in enumerate(reader, start=2):
            name = (row.get("name") or "").strip()
            if not name:
                continue

            logo_file_name = (row.get("logo_file_name") or "").strip()
            if not logo_file_name:
                raise ValueError(
                    f"Missing logo_file_name for sponsor on row {row_number} of {sponsors_file}"
                )

            sponsors.append(
                {
                    "name": name,
                    "logo": Path("static/sponsor_logos") / logo_file_name,
                    "url": (row.get("website_url") or "").strip(),
                }
            )

        return sponsors


def load_social_links():
    social_links_file = Path(__file__).parent / "data" / "social_links.csv"
    with social_links_file.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        required_fields = {"name", "icon_file_name", "url"}
        missing_fields = required_fields.difference(reader.fieldnames or [])
        if missing_fields:
            raise ValueError(
                f"{social_links_file} is missing CSV columns: {', '.join(sorted(missing_fields))}"
            )

        social_links = []
        for row_number, row in enumerate(reader, start=2):
            name = (row.get("name") or "").strip()
            if not name:
                continue

            url = (row.get("url") or "").strip()
            if not url:
                raise ValueError(
                    f"Missing url for social link on row {row_number} of {social_links_file}"
                )

            icon_file_name = (row.get("icon_file_name") or "").strip()
            if not icon_file_name:
                raise ValueError(
                    f"Missing icon_file_name for social link on row {row_number} of {social_links_file}"
                )

            social_links.append(
                {
                    "name": name,
                    "icon": Path("static/social_logos") / icon_file_name,
                    "url": url,
                }
            )

        return social_links


def add_event_status(generator):
    """Dynamically set article.isupcoming based on build time (UTC aware)."""
    now = datetime.now(timezone.utc)

    for article in generator.articles:
        # 1. Guard clause: Ignore non-events
        if str(article.category).lower() != "events":
            continue

        # 2. Guard clause: Handle missing or invalid dates
        if not (hasattr(article, "date") and article.date):
            article.isupcoming = False
            article.istoday = False
            continue

        # 3. Ensure event date is timezone-aware for comparison
        event_date = article.date
        if event_date.tzinfo is None:
            event_date = event_date.replace(tzinfo=timezone.utc)

        # Compare dates in the event's timezone so date-only events stay upcoming all day.
        today = now.astimezone(event_date.tzinfo).date()
        article.isupcoming = event_date.date() >= today
        article.istoday = event_date.date() == today


def register():
    signals.article_generator_finalized.connect(add_event_status)


register()

AUTHOR = "Max Lian"
SITENAME = "Trinity College Science Society"
SITEURL = ""
SPONSORS = load_sponsors()
SOCIAL_LINKS = load_social_links()

PATH = "content"

TIMEZONE = "Europe/London"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = [
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
]

# Social widget
SOCIAL = [
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
]

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Generate site map
PLUGINS = ["sitemap"]

SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.7, "indexes": 0.5, "pages": 0.9},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}

# ----------------------------------------------------------------------
# Additional settings by Max following Al Sweigart's blog
# https://inventwithpython.com/blog/pelican-tutorial.html#:~:text=(%20Y%2Fn)%20Y%20%3E%20Do%20you%20want,your%20website%20using%20Rackspace%20Cloud%20Files%3F%20(

LOAD_CONTENT_CACHE = False  # default was True
DELETE_OUTPUT_DIRECTORY = True  # default was False
INDEX_SAVE_AS = "index.html"  # default was 'index.html'
THEME = "theme"

# ----------------------------------------------------------------------
# URL & Directory Structure Rules
# ----------------------------------------------------------------------
# This determines folder structure (directory structure) in output

PATH = "content"

# Tells Pelican where to find content (and google verification HTML)
PAGE_PATHS = ["pages"]
ARTICLE_PATHS = ["events", "blog"]
STATIC_PATHS = ["static", "extra/googlec08cdfc542823a7d.html"]
EXTRA_PATH_METADATA = {
    "extra/googlec08cdfc542823a7d.html": {"path": "googlec08cdfc542823a7d.html"},
}

# Organize static pages into /pages/
PAGE_URL = "pages/{slug}.html"
PAGE_SAVE_AS = "pages/{slug}.html"

# Dynamically route articles by category (creates /events/ and /blog/ output folders)
ARTICLE_URL = "{category}/{slug}.html"
ARTICLE_SAVE_AS = "{category}/{slug}.html"


"""
# Generate Category Archive Pages (e.g., a page listing ALL blog posts or ALL events)
CATEGORY_URL = '{slug}/index.html'
CATEGORY_SAVE_AS = '{slug}/index.html'
"""


# Disable unused auto-generated pages to keep output clean
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
ARCHIVES_SAVE_AS = ""
TAG_SAVE_AS = ""
TAGS_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""  # Disables the generic multi-category overview page
