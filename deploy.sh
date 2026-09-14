#!/usr/bin/env bash
set -e

echo "Building Pelican site..."
pelican content -s publishconf.py

echo "Syncing files to SRCF..."
rsync -avz --no-perms --omit-dir-times --delete output/ bl573@shell.srcf.net:/public/societies/tcss/public_html/

echo "Done! Live at https://tcss.soc.srcf.net/
