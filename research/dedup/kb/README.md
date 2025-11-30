# Earthquake Catalog Cross-Reference Documentation

**Research Date:** 2025-11-13

**Purpose:** Transcription of official USGS ComCat and ISC Bulletin API documentation

## Contents

1. [USGS ComCat API Documentation](01_usgs_comcat_api.md)
2. [ISC Bulletin API Documentation](02_isc_bulletin_api.md)
3. [Cross-Reference Findings](03_cross_reference_findings.md)

## Main Finding

No explicit cross-reference mechanism between USGS ComCat event IDs and ISC Bulletin event IDs was found in official documentation.

## USGS ComCat ID Structure

From documentation:

- **id:** "A unique identifier for the event. This is the current preferred id for the event, and may change over time."
- **ids:** "A comma-separated list of event ids that are associated to an event."
- **sources:** "A comma-separated list of network contributors."

Example: `us6000m0xl` with `ids` containing `",pt24001001,at00s6kml3,us6000m0xl,"`

## ISC Bulletin ID Structure

From documentation:

- **EVENTID:** Numeric identifier assigned by ISC (8 or 11 digits)
- **AUTHOR:** Agency that computed the solution (9 characters)

Example: EVENTID `600000001` with AUTHOR `NEIC`

## Documented Relationships

From official sources:

1. "The ISC Bulletin is considered the final global archive of parametric earthquake data"
2. "NEIC PDE program contributes about one-third of all data used by the ISC"
3. "ISF files are created to share data with the International Seismological Centre"
4. ISC review published "typically 24 months behind real-time operations"

## Data Fields Comparison

### USGS ComCat (GeoJSON)
```json
{
  "id": "us6000m0xl",
  "properties": {
    "ids": ",pt24001001,at00s6kml3,us6000m0xl,",
    "sources": ",pt,at,us,",
    "time": 1234567890000,
    "latitude": 35.123,
    "longitude": -117.456,
    "depth": 10.0,
    "mag": 7.8,
    "magType": "mww"
  }
}
```

### ISC Bulletin (CSV)
```csv
EVENTID,AUTHOR,DATE,TIME,LAT,LON,DEPTH,MAGNITUDE
600000001,ISC,2023/01/15,08:24:53.10,35.123,-117.456,10.0,7.8
```

## API Endpoints

**USGS ComCat:**
```
https://earthquake.usgs.gov/fdsnws/event/1/query
```

**ISC FDSN:**
```
http://www.isc.ac.uk/fdsnws/event/1/query
```

## Multiple Origins in ISC

From ISF documentation:
"Different agencies' solutions for the same event appear as separate origin blocks within a single ISC bulletin event."

Keywords: `PRIME` (preferred origin), `CENTROID` (moment tensor solution)

## Query Parameters

### USGS
- `eventid` - Data center-specific identifier
- `starttime`, `endtime` - ISO8601 format
- `minmagnitude`, `maxmagnitude`
- `minlatitude`, `maxlatitude`, `minlongitude`, `maxlongitude`
- `limit` (max 20,000)

### ISC
- `eventid` - ISC event identifier
- `starttime`, `endtime` - Format: `YYYY-MM-DDThh:mm:ss`
- `minmagnitude`, `maxmagnitude`, `magnitudetype`
- Geographic: Box or radial search
- `includeallorigins` - Include secondary origins (default: false)
- `contributor` - Filter by agency (automatically sets `includeallorigins=true`)

## Source Documentation

### USGS
- https://earthquake.usgs.gov/data/comcat/
- https://earthquake.usgs.gov/fdsnws/event/1/
- https://earthquake.usgs.gov/data/comcat/index.php
- https://earthquake.usgs.gov/data/comcat/catalog/us/
- https://github.com/usgs/libcomcat

### ISC
- http://www.isc.ac.uk/iscbulletin/
- http://www.isc.ac.uk/fdsnws/event/1/
- http://www.isc.ac.uk/iscbulletin/search/webservices/
- http://www.isc.ac.uk/standards/isf/
- http://www.isc.ac.uk/iscbulletin/agencies/
- http://www.isc.ac.uk/iscbulletin/review/

### Research Papers
- Storchak et al. (2020): "Rebuild of the Bulletin of the International Seismological Centre (ISC)—part 2: 1980–2010"
  https://geoscienceletters.springeropen.com/articles/10.1186/s40562-020-00164-6

## Historical Data

From ComCat documentation, incorporated catalogs include:
- ISC-GEM Main Catalog (1900-2010)
- ISC-GEM Supplementary Catalog (1900-2010)

## Tools

### libcomcat

From GitHub documentation:

**findid** - Find events by ID or location/time
- `-i` - Query by event ID
- `-a` - Return all associated IDs

**getcsv** - Export event data

Example: `findid -i us6000m0xl -a`

## Contributing Agencies

From ISC documentation: "600 agencies have contributed to the ISC Bulletin, throughout its history"

Currently: ~90 active contributing agencies

Examples: NEIC, USGS, JMA, GFZ, BJI, GCMT/HRVD

## What Was Not Found

Comprehensive search of official documentation found no evidence of:

1. ISC event IDs stored in USGS ComCat `ids` field
2. USGS event IDs stored in ISC Bulletin
3. Cross-reference tables between catalogs
4. Official matching procedures or algorithms
5. Direct ID linkage mechanism

## ISF Format

From ISC standards documentation:

"ISF is the IASPEI approved standard format for the exchange of parametric seismological data" - Adopted August 2001

Versions: ISF 1.0, ISF 2.0, ISF 2.1

Structure: Hierarchical blocks containing event title, origin block (with AUTHOR), magnitude sub-block, comment sub-block, and phase block.
