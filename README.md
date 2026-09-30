This is the GitHub page for TCSS' website since 2026.

An GitHub action is to be set up so that, to publish information about new events or blog posts, one create a markdown file in content/events or content/blogs, and it will be automatically compiled and published to the website upon completion of push request. 

Each article (event or blog) should contain a header metadata (to be included at the top of the article) for the program to correctly compile and publish the article. 

For events:

Title:         # **This is the name of the event** <br>
EventType:     # **Talk, Panel Discussion, Quiz night...** <br>
Speaker:       # Name of speaker, if applicable <br>
Status:        # **IMPORTANT**: set to `published` to publish the article; otherwise it will not show<br>
Date:          # **DATE MUST BE IN YYYY-MM-DD format**<br>
Time:          # Preferably in 24 hour format<br>
Location:      # Location <br>
EventID:       # Set to any arbitrary value (e.g. quantum-talk-2026). Blog posts with the same EventID as<br>                     any article will be linked in the event page.<br>

## Sponsors

Edit `data/sponsors.csv` to update the sponsors shown on the homepage. Add one row per sponsor using the columns `name`, `logo_path`, and `website_url`; the website URL may be left blank. Put logo files in `content/static/sponsor_logos/` and set `logo_path` to a path such as `static/images/sponsor-logo.png`. The sponsor section is hidden automatically when there are no sponsor rows.
