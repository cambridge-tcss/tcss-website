This is the GitHub page for TCSS' website since 2026.

An GitHub action is to be set up so that, to publish information about new events or blog posts, one create a markdown file in content/events or content/blogs, and it will be automatically compiled and published to the website upon completion of push request. 

Each article (event or blog) should contain a header metadata (to be included at the top of the article) for the program to correctly compile and publish the article. 

For events:

Title:         # **This is the name of the event**
EventType:     # **Talk, Panel Discussion, Quiz night...**
Speaker:       # Name of speaker, if applicable
Status:        # **IMPORTANT**: set to `published` to publish the article; otherwise it will not show
Date:          # **DATE MUST BE IN YYYY-MM-DD format**
Time:          # Preferably in 24 hour format
Location:      # Location 
EventID:       # Set to any arbitrary value (e.g. quantum-talk-2026). Blog posts with the same EventID as                     any article will be linked in the event page. 
