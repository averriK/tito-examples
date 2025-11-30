# How to Identify the Same Earthquake in Both USGS and ISC Catalogs

I have two earthquake databases: USGS ComCat with 627K events and ISC Bulletin with 1.5M events. The same real-world earthquake appears in both databases but with completely different IDs. I need to figure out which events represent the same earthquake without making catastrophic mistakes like merging a mainshock with its aftershocks.

An AI tried this before and failed spectacularly by inventing arbitrary thresholds ("events within 50km and 60 seconds must be the same") that would have destroyed the database by merging thousands of different earthquakes. I need you to actually READ the documentation and find how professionals solve this problem.

Here's what I know: USGS has an API at https://earthquake.usgs.gov/fdsnws/event/1/query that returns events with fields like `id`, `ids`, `sources`, `time`, `latitude`, `longitude`, `mag`. ISC has an API at http://www.isc.ac.uk/cgi-bin/web-db-run that returns CSV with `EVENTID`, `AUTHOR`, `DATE`, `TIME`, `LAT`, `LON`, etc. Interestingly, ISC lists NEIC (which is part of USGS) as one of its contributing agencies.

What I need you to do is read the actual documentation at https://earthquake.usgs.gov/data/comcat/ and http://www.isc.ac.uk/iscbulletin/ to understand how these catalogs work. Specifically, I want to know if there's a way to definitively link events between the two databases - maybe USGS stores ISC IDs somewhere, or ISC stores USGS IDs, or there's some other cross-reference mechanism I'm missing.

If there's no direct cross-reference, then I need to know how seismologists actually solve this problem in practice. There must be published papers or established methods for matching earthquake events across different catalogs. Search for academic literature on earthquake catalog deduplication, event association, or catalog merging. Find out what distance and time thresholds are actually used in peer-reviewed work, and critically, how they avoid false positives like matching aftershocks or earthquake swarms.

Also check if tools like ObsPy (the Python seismology library) or repositories on GitHub have existing solutions for this problem. Someone must have solved this before.

Finally, test your understanding by querying both APIs for the same well-known earthquake (like the 2011 Japan M9.1) and seeing if you can find any connections between how USGS and ISC represent that event. Look at ALL the fields returned, not just the obvious ones.
