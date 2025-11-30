# Cross-Reference Between USGS and ISC: Documentation Findings

## USGS ComCat ID Fields

### What is Documented

From ComCat documentation:

**id field:**
"A unique identifier for the event. This is the current preferred id for the event, and may change over time."

Format: Network code + unique identifier (e.g., `us6000m0xl`)

**ids field:**
"A comma-separated list of event ids that are associated to an event."

Example from documentation: `",ci15296281,us2013mqbd,at00mji9pf,"`

**sources field:**
"A comma-separated list of network contributors."

Example from documentation: `",ci,us,at,"`

### Actual API Response Example

Query: `https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&eventid=us6000m0xl`

Response:
```json
{
  "id": "us6000m0xl",
  "properties": {
    "ids": ",pt24001001,at00s6kml3,us6000m0xl,",
    "sources": ",pt,at,us,"
  }
}
```

Observation: The `ids` field contains identifiers from three networks (pt, at, us). No ISC identifiers present in this response.

## ISC Bulletin ID Fields

### What is Documented

From ISF format documentation:

**Origin identification number:** 8 characters (ISF 1.0) or 11 digits (ISF 2.1)

**Author field:** 9 characters - "Author of the origin"

Examples of AUTHOR values from documentation: ISC, NEIC, GCMT, JMA, BJI

### CSV Output Structure

From ISC documentation, CSV fields include:
- `EVENTID` - ISC event identifier
- `AUTHOR` - Agency that computed the solution
- `DATE`, `TIME`, `LAT`, `LON`, `DEPTH`, `MAGNITUDE`

## Data Flow: USGS to ISC

### Documented Data Sharing

From USGS catalog page:
"ISF files are created to share data with the International Seismological Centre."

### What is Shared

From documentation: ISF format includes "parametric seismological data" including hypocenters, magnitudes, phase arrivals, and moment tensors.

### What is NOT Documented

No documentation found describing:
- Storage of original USGS event IDs in ISC Bulletin
- Preservation of network-specific identifiers (like `us6000m0xl`)
- Cross-reference tables linking USGS IDs to ISC IDs

## ISC Multiple Origins

### Documented Behavior

From ISF documentation:
"Different agencies' solutions for the same event appear as separate origin blocks within a single ISC bulletin event."

From bulletin search documentation:
"Bulletin Search returns prime (preferred) hypocentre origins and secondary estimates."

### AUTHOR Attribution

From documentation: Each origin block contains AUTHOR field identifying the contributing organization (e.g., NEIC, ISC, JMA).

From FDSN API documentation:
"Using `contributor` parameter automatically sets `includeallorigins` to true."

Example query: `contributor=NEIC` returns events where NEIC contributed data, including all origins.

## Documented Relationships

### From Web Search Results

"The ISC Bulletin is considered the final global archive of parametric earthquake data."

"NEIC PDE program contributes about one-third of all data used by the ISC."

"When ISC magnitude becomes available, magnitudes from ComCat should be revised and re-cited to ISC."

### From ISC Review Paper (Storchak et al. 2020)

"Data from reporting agencies arrived...they were integrated, re-assessed, reviewed and published."

"One of the agencies reporting a severely mis-located hypocentre solution...led to the formation of two separate events in the original ISC Bulletin, where in fact, there was just one physical event."

Example from paper: "A Turkish observatory's event was incorrectly cross-matched with a NEIC report, with identical P and S arrival times suggesting data corruption."

## Incorporated Historical Data

### ComCat Documentation

From ComCat overview, contributing catalogs include:
- ISC-GEM Main Catalog (1900-2010)
- ISC-GEM Supplementary Catalog (1900-2010)

### Modern ISC Bulletin

No documentation found describing integration of modern ISC Bulletin event IDs into ComCat.

## Catalog Timelines

### USGS
From documentation: Near real-time earthquake reporting (PDE - Preliminary Determination of Epicenters)

### ISC
From documentation: "Reviewed version typically 24 months behind real-time operations"

## ID Format Differences

### USGS
Format: Alphanumeric with network prefix

Examples from documentation and API responses:
- `us6000m0xl`
- `ci15296281`
- `pt24001001`
- `at00s6kml3`

### ISC
Format: Numeric

From ISF documentation: 8-character field (ISF 1.0) or 11 digits (ISF 2.1)

## Tools: libcomcat

### findid Tool

From libcomcat documentation:

Query by ID:
```bash
findid -i ci38572791
```

Get all associated IDs:
```bash
findid -i ci38572791 -a -r 200 -w 120
```

From documentation: "-a flag returns the authoritative ID plus all contributing identifiers"

Output: "ID, time, location coordinates, depth, magnitude, distance calculations, temporal differences, and azimuth measurements"

### Scope

From documentation: findid works with ComCat event IDs. The tool accepts "IDs from any contributing source network."

## IRIS Integration

### From Web Search Results

"IRIS-DMC fdsnws-event web service returns earthquake information from catalogs originating from USGS and ISC data centers."

"Events retrieved from the USGS PDE catalog for recent events and then the ISC catalog when it becomes available."

### Not Documented

No documentation found describing how IRIS maintains cross-references between USGS and ISC event IDs internally.

## Summary of Documentation Search

### What Was Found

1. USGS `ids` field contains associated identifiers from multiple seismic networks
2. ISC `AUTHOR` field identifies contributing agencies
3. ISC preserves multiple origins with agency attribution
4. NEIC contributes approximately 1/3 of ISC data
5. ISC publishes reviewed bulletin ~24 months after events
6. ISC-GEM historical catalog (1900-2010) is incorporated into ComCat

### What Was NOT Found

1. Documentation of ISC event IDs stored in USGS ComCat
2. Documentation of USGS event IDs stored in ISC Bulletin
3. Cross-reference tables or lookup mechanisms
4. Official matching algorithms or procedures
5. Direct ID linkage between the two catalogs

### Observation

All comprehensive searches of official USGS and ISC documentation, API specifications, data format descriptions, and web services found no explicit cross-reference mechanism between USGS event IDs and ISC event IDs.
