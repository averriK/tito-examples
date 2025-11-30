# ISC Bulletin API Documentation

Source: http://www.isc.ac.uk/iscbulletin/

## Overview

From ISC documentation: "The ISC Bulletin serves as the primary output of the ISC and is regarded as the definitive record of the Earth's seismicity."

Data coverage: 1900 to present

Reviewed version: Typically 24 months behind real-time operations

## Relationship to USGS

From USGS documentation: "The Bulletin of the International Seismological Centre is considered to be the final global archive of parametric earthquake data."

From web search results: "NEIC PDE program contributes about one-third of all data used by the ISC."

## API Endpoints

### FDSN Event Web Service
`http://www.isc.ac.uk/fdsnws/event/1/`

### Web Services (Legacy CGI)
`http://www.isc.ac.uk/cgi-bin/web-db-run`

## Available Services

1. **Bulletin Search** - Returns event parametric data (QuakeML or ISF format)
2. **Event Catalogue** - Delivers condensed event lists (QuakeML or CSV)
3. **Arrivals** - Outputs phase data (QuakeML, CSV, or IMS1.0)
4. **Focal Mechanism Solutions** - Provides mechanism data (QuakeML or CSV)

## Event Identifiers

### EVENTID

From ISF documentation: "Origin identification number" - 8 characters in ISF 1.0, extended to 11 digits in ISF 2.1

Format: Alphanumeric field (a8 or 11 digits)

Assigned by: ISC

### AUTHOR

From ISF documentation: "Author of the origin" - 9 characters

Identifies the organization that computed the solution.

Examples: ISC, NEIC, GCMT, JMA, BJI

## Contributing Agencies

From ISC documentation: "600 agencies have contributed to the ISC Bulletin, throughout its history."

Currently: ~90 contributing agencies

Major contributors include:
- NEIC - National Earthquake Information Center (USA)
- USGS - United States Geological Survey (USA)
- JMA - Japan Meteorological Agency
- GFZ - German Research Centre for Geosciences
- BJI - China Earthquake Networks Center
- GCMT/HRVD - Global Centroid Moment Tensor Project

## FDSN Query Parameters

### Geographic

**Box Search:**
- `minlatitude`, `maxlatitude` (degrees)
- `minlongitude`, `maxlongitude` (degrees)

**Radial Search:**
- `latitude`, `longitude` (center point)
- `minradius`, `maxradius` (degrees)

Note: Box and radial searches are mutually exclusive

### Temporal
- `starttime` - Format: `YYYY-MM-DDThh:mm:ss[.ssssss]`
- `endtime` - Format: `YYYY-MM-DDThh:mm:ss[.ssssss]`

### Magnitude
- `minmagnitude`, `maxmagnitude`
- `magnitudetype` - Case-insensitive (Ml, MS, mb, Mw, etc.)

### Depth
- `mindepth`, `maxdepth` - In kilometers, positive downward

### Agency Filtering
- `catalog`
- `contributor` - e.g., "NEIC MOS"
- `limit`, `offset`
- `orderby`

### Event ID
- `eventid` - Unique ID numbers assigned by ISC

### Response Control
- `includeallorigins` - Include all agency origins (default: false)
- `includeallmagnitudes` - Include all magnitude determinations
- `includearrivals` - Include phase arrival data

From documentation: "Using `contributor` parameter automatically sets `includeallorigins` to true."

## Response Formats

- `xml` - QuakeML 1.2 (default)
- `isf` - ISC Seismic Format 1.0
- `isf2` - ISC Seismic Format 2.0

### CSV Catalogue Fields

- `EVENTID` - ISC event identifier
- `AUTHOR` - Agency that computed the solution
- `DATE` - Event date (yyyy/mm/dd)
- `TIME` - Event time (hh:mm:ss.sss)
- `LAT` - Latitude
- `LON` - Longitude
- `DEPTH` - Depth in km
- `MAGNITUDE` - Magnitude value

From documentation: "CSV catalogue returns only the preferred (prime) hypocentre for each event."

## ISF Format Structure

From ISF documentation: "ISF is the IASPEI approved standard format for the exchange of parametric seismological data." Adopted August 2001.

### Hierarchical Structure

1. Bulletin title
2. Event title
3. Origin block
   - Date and time
   - Origin identification number
   - Author field (9 characters)
   - Location parameters
4. Magnitude sub-block
   - Magnitude values
   - Magnitude type
   - Author of magnitude
5. Comment sub-block
6. Phase block

### Multiple Origins

From documentation: "Different agencies' solutions for the same event appear as separate origin blocks within a single ISC bulletin event."

**Keywords:**
- `PRIME` - Designates preferred/prime origin
- `CENTROID` - Indicates centroid moment tensor solutions

## Event Processing

### Automated Grouping

From documentation: "Automatic algorithm that scores hypocentres using multiple quality metrics, compares location and origin time parameters, and groups, splits, or creates new events based on the hypocentre score and parameter comparison."

### Review Process

From documentation: "Analysts review groupings to check that the grouping of hypocentres and association of phase arrivals is appropriate."

Tool: Visual Bulletin Analysis System (VBAS)

### Split Events

From ISC Rebuild Paper (Storchak et al. 2020): "Split events are instances where one of the agencies reporting a severely mis-located hypocentre solution led to the formation of two separate events in the original ISC Bulletin, where in fact, there was just one physical event."

## Prime vs. Secondary Origins

From documentation:

**Prime (Preferred) Origin:** The ISC's preferred solution for an event

**Secondary Origins:** Alternative solutions from contributing agencies

From catalogue search documentation: "The catalogue search returns only the preferred (prime) hypocentre for each event."

From bulletin search documentation: "Bulletin Search returns prime (preferred) hypocentre origins and secondary estimates."

## Arrivals/Phase Data

From documentation: "Only the prime origin are output for each event" across CSV, ISF, and QuakeML formats.

"Defining phases only exist for events with an ISC authored hypocentre."

"The defined region is used to check only the prime hypocentre."

## Access Methods

### Web Interface
- Catalogue Search: http://www.isc.ac.uk/iscbulletin/search/catalogue/
- Bulletin Search: http://www.isc.ac.uk/iscbulletin/search/bulletin/

### Programmatic Access

From documentation:
```
wget --output-document='iscsearch.xml' 'http://www.isc.ac.uk/cgi-bin/web-db-run?...'
```

## Data Standards

From ISC standards page:

**ISF Versions:**
- ISF 1.0 - Adopted August 2001
- ISF 2.0 - Enhanced format
- ISF 2.1 - Extended station details and 11-digit IDs

**Other Formats:**
- QuakeML - "A flexible, extensible and modular XML representation of seismological data"
- GSE2.1 Format
- Nordic Format
- Fixed Format Bulletin (FFB)
