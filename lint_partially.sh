# Full-scale pylint produces a blizzard of complaints.
# For now we are looking for a very limited set of messages:
# unused imports.

pylint --disable=all --enable=W0611 usaspending_api --ignore=migrations
