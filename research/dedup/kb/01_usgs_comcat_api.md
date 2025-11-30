# USGS ComCat API Documentation

Source: https://earthquake.usgs.gov/data/comcat/

## Overview

The ANSS Comprehensive Earthquake Catalog (ComCat) aggregates earthquake parameters and products from multiple seismic networks, including hypocenters, magnitudes, phase picks, and derived products like moment tensors and ShakeMaps.

## API Endpoint

**Base URL:** `https://earthquake.usgs.gov/fdsnws/event/1/`

## Event Identifier Fields

### id

"A unique identifier for the event. This is the current preferred id for the event, and may change over time."

**Format:** Network code + unique identifier

**Example:** `us6000m0xl` where `us` is the USGS/NEIC network code

### ids

"A comma-separated list of event ids that are associated to an event."

**Example:** `",ci15296281,us2013mqbd,at00mji9pf,"`

### sources

"A comma-separated list of network contributors."

**Example:** `",ci,us,at,"`

### net

The network that originally authored the reported location (locationSource).

### code

Unique identifier from the source network.

## Query Parameters

### Time Parameters
- `starttime` - ISO8601 format, UTC default
- `endtime` - ISO8601 format, UTC default
- `updatedafter` - Filter by modification date

### Location Parameters

**Rectangle:**
- `minlatitude`, `maxlatitude`
- `minlongitude`, `maxlongitude`

**Circle:**
- `latitude`, `longitude`
- `maxradius` or `maxradiuskm`

### Event Selection
- `eventid` - Data center-specific identifier
- `catalog` - Filter by catalog source
- `contributor` - Filter by contributing network
- `limit` - Maximum results (max 20,000)
- `offset` - Pagination offset
- `orderby` - Sort order

### Magnitude & Depth
- `minmagnitude`, `maxmagnitude`
- `mindepth`, `maxdepth`

### Additional Filters
- `alertlevel`, `eventtype`, `reviewstatus`
- `maxgap`, `mingap`, `maxsig`, `minsig`
- `producttype`, `productcode`

## Response Formats

Supported via `format` parameter:
- `geojson` (default)
- `xml` (QuakeML 1.2)
- `csv`
- `kml`
- `text`

## GeoJSON Response Structure

### Feature Properties

From actual API response (eventid=us6000m0xl):

```json
{
  "type": "Feature",
  "id": "us6000m0xl",
  "properties": {
    "mag": 7.8,
    "place": "...",
    "time": 1234567890000,
    "updated": 1234567890000,
    "tz": null,
    "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us6000m0xl",
    "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us6000m0xl&format=geojson",
    "felt": 123,
    "cdi": 5.6,
    "mmi": 6.7,
    "alert": "red",
    "status": "reviewed",
    "tsunami": 1,
    "sig": 890,
    "net": "us",
    "code": "6000m0xl",
    "ids": ",pt24001001,at00s6kml3,us6000m0xl,",
    "sources": ",pt,at,us,",
    "types": ",origin,phase-data,moment-tensor,shakemap,",
    "nst": 234,
    "dmin": 0.123,
    "rms": 0.45,
    "gap": 23,
    "magType": "mww",
    "type": "earthquake"
  },
  "geometry": {
    "type": "Point",
    "coordinates": [longitude, latitude, depth]
  }
}
```

## Product Preference

From documentation: "When multiple products of the same type associate with an event, the system selects the 'most preferred' based on preferredWeight ranking and most recent updateTime."

## Contributing Networks

ComCat integrates data from multiple networks including:
- `us` - USGS/NEIC
- `ci` - Southern California Seismic Network
- `nc` - Northern California Seismic Network
- `ak` - Alaska Earthquake Center
- `pt` - Pacific Tsunami Warning Center
- `at` - Austrian seismic network
- Many others

## Incorporated Catalogs

Documentation lists contributing catalogs including:
- ISC-GEM Main Catalog (1900-2010)
- ISC-GEM Supplementary Catalog (1900-2010)
- Global CMT project
- Regional networks

## Limitations

- Maximum 20,000 results per query
- Event identifiers are data center specific
- Preferred ID may change over time

## Command Line Tools

### libcomcat

GitHub: https://github.com/usgs/libcomcat

**findid** - Find events by ID or location/time
- `-i` - Query by event ID
- `-a` - Return all associated IDs

**getcsv** - Export event data to CSV/Excel

Example from documentation:
```bash
findid -i ci38572791 -a -r 200 -w 120
```

Output includes: ID, time, location coordinates, depth, magnitude, distance calculations, temporal differences, and azimuth measurements.
