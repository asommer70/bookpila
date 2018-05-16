#!/usr/bin/env bash
#
#

fswatch -0 scss/ | while IFS= read -r -d "" path
echo $path
do
  echo "Re-building CSS (due to change in ${path})"
  /usr/local/bin/sassc -m auto -t compressed scss/main.scss ../assets/css/main.css
done
