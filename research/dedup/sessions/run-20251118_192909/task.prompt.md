# Earthquake Catalog Deduplication Task

## SLOTS

### SLOT 1: Understand database structure and fields
Read the actual documentation at https://earthquake.usgs.gov/data/comcat/ and http://www.isc.ac.uk/iscbulletin/ to understand how these catalogs work. Specifically, determine if there's a way to definitively link events between the two databases - maybe USGS stores ISC IDs somewhere, or ISC stores USGS IDs, or there's some other cross-reference mechanism.

Context: USGS API at https://earthquake.usgs.gov/fdsnws/event/1/query returns events with fields like `id`, `ids`, `sources`, `time`, `latitude`, `longitude`, `mag`. ISC API at http://www.isc.ac.uk/cgi-bin/web-db-run returns CSV with `EVENTID`, `AUTHOR`, `DATE`, `TIME`, `LAT`, `LON`, etc. ISC lists NEIC (which is part of USGS) as one of its contributing agencies.

### SLOT 2: Research established methods for catalog matching
If there's no direct cross-reference, determine how seismologists actually solve this problem in practice. Search for academic literature on earthquake catalog deduplication, event association, or catalog merging. Find out what distance and time thresholds are actually used in peer-reviewed work, and critically, how they avoid false positives like matching aftershocks or earthquake swarms.

### SLOT 3: Check existing tools and implementations
Check if tools like ObsPy (the Python seismology library) or repositories on GitHub have existing solutions for this problem.

### SLOT 4: Validate understanding with real example
Test understanding by querying both APIs for the same well-known earthquake (like the 2011 Japan M9.1) and seeing if you can find any connections between how USGS and ISC represent that event. Look at ALL the fields returned, not just the obvious ones.

## CONSTRAINTS

- Must read actual documentation rather than inventing arbitrary thresholds
- Must avoid catastrophic mistakes like merging mainshocks with aftershocks or merging distinct events in earthquake swarms
- Must base methods on peer-reviewed work or established professional practice
- Solutions must work with: USGS ComCat (627K events) and ISC Bulletin (1.5M events)
