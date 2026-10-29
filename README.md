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

Edit `data/sponsors.csv` to update the sponsors shown on the homepage. Add one row per sponsor using the columns `name`, `logo_file_name`, and `website_url`; the website URL may be left blank. Put each logo in `content/static/sponsor_logos/` and enter only its filename in the CSV, for example `jane_street.png` (not the folder path). The sponsor section is hidden automatically when there are no sponsor rows.

## Social Media

Edit `data/social_links.csv` to update the social media icons shown in the site footer. Add one row per account using the columns `name`, `icon_file_name`, and `url`. Put each icon in `content/static/social_logos/` and enter only its filename in the CSV. The section is hidden automatically when there are no social link rows.

## Reverse Proxy
If tcss.soc.srcf.net ever drops its reverse proxy, SSH into shell.srcf.net, open /public/societies/tcss/.htaccess, and paste the contents of srcf.htaccess.