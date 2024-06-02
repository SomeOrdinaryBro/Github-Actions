#!/bin/bash

echo "#=============----------------=============#"

git config --global user.name "${INPUT_COMMITTER_NAME}"
git config --global user.email "${INPUT_COMMITTER_EMAIL}"
git config --global --add safe.directory /github/workspace

python3 /usr/bin/feed.py

git add -A && git commit -m "Update Feed"
git push --set-upstream origin main

echo "#=============----------------=============#"
