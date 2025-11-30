# Earthquake Catalog Deduplication: Cross-Referencing USGS and ISC


## Executive Summary

No explicit cross-reference mechanism exists between USGS ComCat event IDs and ISC Bulletin event IDs in the official documentation of either service [@03crossreferencefindings2025][@README2025]. However, practical methods for matching events between catalogs have been established in peer-reviewed literature, and limited historical cross-referencing exists for ISC-GEM catalog data (1900-2010) integrated into ComCat [@USGS2025]. Modern ISC Bulletin events (post-2010) do not appear to be systematically cross-referenced with USGS IDs, despite NEIC contributing approximately one-third of all data to the ISC [@02iscbulletinapi2025].


## USGS ComCat Event Identification System

USGS ComCat employs a multi-identifier system designed to track events across multiple seismic networks [@01usgscomcatapi2025]. The primary identifier ($\text{id}$) follows the format: network code + unique identifier (e.g., $\texttt{us6000m0xl}$ where $\texttt{us}$ represents USGS/NEIC) [@01usgscomcatapi2025]. This identifier is explicitly described as "the current preferred id for the event" with the caveat that it "may change over time" [@01usgscomcatapi2025].

The $\texttt{ids}$ field maintains "a comma-separated list of event ids that are associated to an event" from multiple contributing networks [@01usgscomcatapi2025]. For the 2011 Tohoku earthquake ($M_w$ 9.1), the USGS record contains: $\texttt{ids} = \text{",usc0001xgp,official20110311054624120\_30,usp000hvnu,choy20110311054623,duputel201103110546a,atlas20110311054624,iscgem16461282,"}$ [@USGS2025c]. Notably, this includes $\texttt{iscgem16461282}$, demonstrating that historical ISC-GEM catalog identifiers are preserved in ComCat's cross-reference system [@USGS2025c].

The corresponding ISC Bulletin entry for this event shows: $\texttt{EVENTID} = 16461282$, $\texttt{AUTHOR} = \text{ISC}$, with origin time 2011-03-11 05:46:23.20 UTC, location (38.2963°N, 142.4980°E), depth 19.7 km [@ISC2025]. The numeric component of the ISC-GEM identifier ($16461282$) matches the ISC Bulletin event ID exactly, establishing a verifiable linkage for this historical event [@USGS2025c][@ISC2025].

ComCat incorporates historical ISC-GEM data covering 1900-2010, as documented in the contributing catalogs list [@01usgscomcatapi2025]. However, comprehensive documentation searches found no evidence of modern ISC Bulletin event IDs (post-2010) being systematically stored in the USGS $\texttt{ids}$ field, nor of USGS event IDs being preserved in ISC Bulletin records [@03crossreferencefindings2025][@README2025].


## ISC Bulletin Event Identification System

The ISC Bulletin uses numeric event identifiers ($\texttt{EVENTID}$) formatted as 8-character fields in ISF 1.0 or extended to 11 digits in ISF 2.1 [@02iscbulletinapi2025]. Each event is attributed to an originating agency through the $\texttt{AUTHOR}$ field (9 characters), identifying organizations such as ISC, NEIC, GCMT, JMA, or BJI [@02iscbulletinapi2025]. The ISC processes data from approximately 90 currently active contributing agencies, with over 600 agencies having contributed throughout the bulletin's history [@02iscbulletinapi2025].

A critical architectural feature distinguishes ISC from USGS: ISC preserves multiple origin solutions for the same physical event as separate origin blocks within a single bulletin entry [@02iscbulletinapi2025]. The ISF documentation states: "Different agencies' solutions for the same event appear as separate origin blocks within a single ISC bulletin event" [@02iscbulletinapi2025]. The $\texttt{PRIME}$ keyword designates the ISC's preferred solution, while secondary origins from contributing agencies are retained with agency attribution [@02iscbulletinapi2025]. The FDSN API documentation specifies: "Using $\texttt{contributor}$ parameter automatically sets $\texttt{includeallorigins}$ to true," enabling retrieval of all agency submissions for event analysis [@02iscbulletinapi2025].

This multi-origin architecture implies that NEIC solutions are preserved within ISC events with $\texttt{AUTHOR} = \text{NEIC}$, but the ISC documentation provides no specification for storing original USGS network-assigned identifiers (e.g., $\texttt{us6000m0xl}$) in any ISC data field [@03crossreferencefindings2025]. The ISF format's hierarchical structure includes origin identification numbers, author fields, location parameters, and magnitude sub-blocks, but no designated field for external catalog cross-references [@02iscbulletinapi2025].


## Data Flow and Temporal Relationships

USGS documentation states: "ISF files are created to share data with the International Seismological Centre" [@03crossreferencefindings2025]. NEIC's Preliminary Determination of Epicenters (PDE) program provides near real-time earthquake reporting, while ISC publishes its reviewed bulletin "typically 24 months behind real-time operations" [@02iscbulletinapi2025][@03crossreferencefindings2025]. This temporal lag reflects ISC's role as "the definitive record of the Earth's seismicity" and "the final global archive of parametric earthquake data" [@02iscbulletinapi2025][@03crossreferencefindings2025].

The documented data flow establishes that USGS contributes parametric seismological data to ISC, including hypocenters, magnitudes, phase arrivals, and moment tensors in ISF format [@03crossreferencefindings2025]. However, the transformation process from USGS event records (with network-prefixed alphanumeric IDs) to ISC bulletin entries (with numeric ISC-assigned IDs) involves no documented mechanism for bidirectional ID preservation [@03crossreferencefindings2025][@README2025].


## Peer-Reviewed Methods for Catalog Matching

In the absence of official cross-reference mechanisms, seismologists employ spatiotemporal matching algorithms to identify duplicate events across catalogs. The nearest neighbor method, published in *Frontiers in Earth Science* (2022), provides a rigorous two-step approach for discriminating duplicates from aftershocks when merging earthquake catalogs [@Frontiers2025].

The method's critical innovation distinguishes duplicates from aftershocks by recognizing that duplicates: (1) have no causal relationship, (2) form pairs from different source catalogs, and (3) exhibit bidirectional time differences (i.e., $\Delta t$ can be positive or negative), whereas aftershocks exhibit unidirectional temporal relationships with mainshocks [@Frontiers2025]. Applied to Tohoku earthquake catalogs (JMA and ANSS), the method achieved >97% duplicate identification reliability and identified over 700 events missed by the JMA network [@Frontiers2025].


## Machine Learning Approaches

Modern seismic phase association algorithms—including GaMMA (Gaussian Mixture Model Association), REAL (Rapid Earthquake Association and Location), and GENIE (Graph Earthquake Neural Interpretation Engine)—treat event association as an unsupervised clustering problem in probabilistic frameworks [@Earth-planets-space2025]. The FAST (Fingerprint And Similarity Thresholding) method analyzes continuous seismic waveform data 140 times faster than autocorrelation by creating compact waveform fingerprints [@Science2025]. These computational methods enable large-scale catalog processing but require careful validation against ground truth datasets to avoid systematic biases in duplicate detection [@Earth-planets-space2025].


## ObsPy and Computational Tools

ObsPy, the Python toolbox for seismology, provides comprehensive infrastructure for earthquake catalog operations through its catalog object architecture [@ResearchGate2025]. The library supports access to waveform, station, and event data from FDSN web services spanning IRIS, ORFEUS, Geonet, RESIF, INGV, ETH, and GFZ data centers [@ResearchGate2025]. ObsPy's $\texttt{get\_events}$ function provides a consistent interface for creating event catalogs from multiple sources, serving as a foundation for machine learning and conventional seismological analysis [@ArXiv210808601].

USGS provides libcomcat, a Python library for querying ComCat with the $\texttt{findid}$ tool for event identification [@01usgscomcatapi2025]. The command $\texttt{findid -i <eventid> -a}$ retrieves the authoritative ID plus all contributing identifiers from the $\texttt{ids}$ field, returning "ID, time, location coordinates, depth, magnitude, distance calculations, temporal differences, and azimuth measurements" [@01usgscomcatapi2025][@03crossreferencefindings2025]. This tool accepts IDs from any contributing source network but operates exclusively within the ComCat ecosystem, with no documented capability to resolve ISC Bulletin event IDs [@03crossreferencefindings2025].


## Practical Matching Strategy - Phase 1: Historical Events (1900-2010)

For events within the ISC-GEM temporal range, query USGS ComCat and examine the $\texttt{ids}$ field for $\texttt{iscgem}$-prefixed identifiers [@01usgscomcatapi2025]. The numeric component following $\texttt{iscgem}$ corresponds directly to the ISC $\texttt{EVENTID}$ [@USGS2025c][@ISC2025]. This method provides definitive linkage with 100% reliability for ISC-GEM catalog events [@USGS2025b].


## Critical Constraint: Aftershock Discrimination

Simple spatiotemporal thresholds fail catastrophically in high-seismicity regions where mainshock-aftershock sequences produce hundreds of events within minutes and tens of kilometers [@Frontiers2025]. The nearest neighbor method's bidirectional time difference criterion ($\Delta t$ can be positive or negative for duplicates) explicitly addresses this failure mode [@Frontiers2025]. For earthquake swarms or sequences, implement declustering algorithms (e.g., Reasenberg 1985, Gardner-Knopoff 1974) prior to duplicate detection to separate background seismicity from clustered events [@Link2025].


## Limitations and Uncertainty Quantification

The absence of official cross-reference mechanisms introduces irreducible uncertainty in matching USGS and ISC events for the modern catalog (post-2010) [@03crossreferencefindings2025][@README2025]. Conservative spatiotemporal thresholds minimize false positives (incorrectly matching distinct events) at the cost of increased false negatives (failing to match genuine duplicates with unusually large location or timing discrepancies) [@Frontiers2025].


## Conclusion

No direct ID cross-reference system links USGS ComCat and ISC Bulletin for modern earthquakes, despite substantial data sharing between the institutions [@03crossreferencefindings2025][@README2025]. Historical events (1900-2010) benefit from systematic ISC-GEM integration into ComCat, enabling deterministic matching via $\texttt{iscgem}$ identifiers in the USGS $\texttt{ids}$ field [@01usgscomcatapi2025][@USGS2025c]. For contemporary events, the peer-reviewed nearest neighbor algorithm with spatiotemporal proximity functions provides a scientifically validated alternative to the "arbitrary threshold" approach, achieving >97% reliability when properly implemented with aftershock discrimination [@Frontiers2025].


## Executive Summary (File 2)

No direct cross-reference mechanism exists between USGS ComCat event IDs and ISC Bulletin event IDs. [@03crossreferencefindings2025] The two catalogs use fundamentally different identifier schemes: USGS employs alphanumeric network-prefixed identifiers (e.g., `us6000m0xl`), while ISC uses numeric identifiers (8-11 digits). [@01usgscomcatapi2025][@02iscbulletinapi2025] Matching earthquake events across these catalogs requires spatiotemporal proximity methods rather than direct ID lookups, with careful attention to avoiding false positives from aftershocks and earthquake swarms.


## USGS ComCat ID Structure

USGS ComCat uses a multi-identifier system designed to track events across contributing seismic networks. [@01usgscomcatapi2025] The primary identifier field, `id`, contains the current preferred network-prefixed ID (e.g., `us6000m0xl` where `us` represents USGS/NEIC), and this preferred ID may change over time as new analyses become available. [@01usgscomcatapi2025] The `ids` field stores a comma-separated list of all associated identifiers from contributing networks, for example: `",ci15296281,us2013mqbd,at00mji9pf,"` representing contributions from California Integrated (ci), USGS (us), and Austrian (at) networks. [@01usgscomcatapi2025] A parallel `sources` field lists the corresponding network codes: `",ci,us,at,"`. [@01usgscomcatapi2025]


## ISC Bulletin ID Structure

The ISC Bulletin employs a completely different identification scheme centered on numeric event identifiers assigned by ISC. [@02iscbulletinapi2025] The primary identifier field, `EVENTID`, contains an alphanumeric value originally limited to 8 characters in ISF 1.0 format but extended to 11 digits in ISF 2.1. [@02iscbulletinapi2025] A separate `AUTHOR` field (9 characters) identifies which organization computed the solution, with common values including ISC, NEIC, GCMT, JMA, and BJI. [@02iscbulletinapi2025] When multiple agencies provide solutions for the same physical earthquake, ISC preserves all contributions as separate "origin blocks" within a single event, with one designated as the "prime" (preferred) origin. [@02iscbulletinapi2025] The CSV catalogue output returns only the prime hypocenter for each event, while the bulletin search returns both prime and secondary origins. [@02iscbulletinapi2025]


## Absence of Direct Cross-References

Comprehensive examination of USGS and ISC API documentation, data format specifications, and web service descriptions found no evidence of direct ID linkage between the catalogs. [@03crossreferencefindings2025] USGS ComCat's `ids` field contains identifiers from contributing seismic networks (ci, at, pt, nc, ak, etc.) but no ISC event IDs. [@03crossreferencefindings2025] An actual API query for event `us6000m0xl` returned `ids` containing `",pt24001001,at00s6kml3,us6000m0xl,"` with no ISC identifiers present. [@03crossreferencefindings2025] Similarly, ISC Bulletin documentation describes storage of agency-specific origins with `AUTHOR` attribution but makes no mention of preserving original USGS event IDs, network-specific identifiers, or cross-reference tables. [@03crossreferencefindings2025]


## Data Flow Relationship

Despite the absence of direct ID linkage, a well-established data flow exists between USGS and ISC. [@03crossreferencefindings2025] USGS documentation states that "ISF files are created to share data with the International Seismological Centre," and NEIC (National Earthquake Information Center, part of USGS) contributes approximately one-third of all data used by ISC. [@03crossreferencefindings2025] ISC receives parametric seismological data including hypocenters, magnitudes, phase arrivals, and moment tensors from NEIC and approximately 90 other contributing agencies. [@02iscbulletinapi2025] ISC then performs comprehensive review and reanalysis, publishing a definitive bulletin typically 24 months after events occur. [@02iscbulletinapi2025][@03crossreferencefindings2025] The ISC Bulletin is considered "the final global archive of parametric earthquake data." [@03crossreferencefindings2025]


## Historical Integration: ISC-GEM in ComCat

One notable exception to the ID separation involves historical data. [@03crossreferencefindings2025] USGS ComCat incorporates the ISC-GEM (Global Instrumental Earthquake) catalog covering 1900-2014, appearing as both "ISC-GEM Main Catalog" and "ISC-GEM Supplementary Catalog" in ComCat's list of contributing catalogs. [@03crossreferencefindings2025][@USGS2025b] For the 2011 Tohoku M9.1 earthquake, USGS includes an ISC-GEM identifier (`iscgem16461282`) in the event's `ids` field, demonstrating that ISC-GEM catalog integration does preserve ISC identifiers for historical events. [@USGS2025c] However, documentation provides no evidence that modern ISC Bulletin event IDs are similarly integrated into ComCat for recent earthquakes. [@03crossreferencefindings2025]


## Case Study: 2011 Tohoku M9.1 Earthquake - USGS ComCat Representation

The USGS primary identifier for the 2011 Tohoku earthquake is `official20110311054624120_30`, with the `net` field showing "official" rather than a specific network code. [@USGS2025c] The comprehensive `ids` field contains seven identifiers: `",usc0001xgp,official20110311054624120_30,usp000hvnu,choy20110311054623,duputel201103110546a,atlas20110311054624,iscgem16461282,"` representing different analysis products and the ISC-GEM historical catalog entry. [@USGS2025c] The corresponding `sources` field lists: `",us,official,us,choy,duputel,atlas,iscgem,"` showing contributions from multiple USGS analysts and the ISC-GEM catalog. [@USGS2025c]


## Case Study: 2011 Tohoku M9.1 Earthquake - ISC Bulletin Representation

The ISC Bulletin assigns event ID `16461282` to the Tohoku earthquake, documented with the event code `TOHOKU2011`. [@Isc-mirror2025] The ISC record shows origin time 2011-03-11 at 05:46:23 UTC, coordinates 38.30°N, 142.50°E, depth 19.7 km, with moment magnitude Mw(GCMT) = 9.1. [@Isc-mirror2025] The ISC maintains comprehensive data for this event including 1991 articles in its bibliography, multiple agency origins (including NEIC contributions), and complete phase arrival data. [@Isc-mirror2025]


## Case Study: 2011 Tohoku M9.1 Earthquake - Cross-Catalog Observation

Notably, the USGS `ids` field contains `iscgem16461282`, which corresponds to the ISC event ID `16461282` with the "iscgem" catalog prefix. [@USGS2025c][@Isc-mirror2025] This linkage exists because the event falls within the ISC-GEM catalog coverage (1900-2014) that has been integrated into ComCat. [@03crossreferencefindings2025][@USGS2025b] However, this represents historical catalog integration, not a general cross-reference mechanism for modern earthquake monitoring. [@03crossreferencefindings2025] For earthquakes after 2014 not included in ISC-GEM, no such direct ID connection exists in either direction. [@03crossreferencefindings2025]


## Declustering vs. Duplicate Detection

It is crucial to distinguish between earthquake catalog "declustering" (removing aftershocks and foreshocks to isolate mainshocks) and duplicate detection (identifying the same physical event reported in multiple catalogs). [@Corssa2025] Declustering algorithms like the widely-used Gardner-Knopoff (1974) window method deliberately remove dependent events using magnitude-dependent spatial and temporal windows; for example, M4.0 earthquakes use L=30.07 km and T=41.36 days, while M6.0 earthquakes use L=53.19 km and T=499.34 days. [@OUP2025] These windows are designed to remove aftershocks, not to match identical events across catalogs, and directly applying declustering thresholds to duplicate detection would incorrectly exclude genuine aftershocks that appear in both catalogs. [@OUP2025] The Reasenberg (1985) method and stochastic approaches based on the ETAS (Epidemic Type Aftershock Sequence) model represent alternative declustering strategies commonly used in seismic hazard studies. [@OUP2025]


## ObsPy Event Handling

ObsPy, the standard Python library for seismology, provides comprehensive tools for earthquake event handling but limited functionality for cross-catalog duplicate detection. [@Docs2025] ObsPy Event objects support multiple origins associated with the same event, covering automatic and manual locations, different agencies, and various location programs. [@Docs2025] The library includes a `coincidence_trigger` function for event detection based on STA/LTA (Short-Term Average/Long-Term Average) characteristic functions, creating reference catalogs independent of a-priori known origin times. [@Docs2025b] ObsPy's mass downloader implements duplicate station detection using the `minimum_interstation_distance_in_m` parameter, preventing downloads from stations closer than a specified threshold. [@GitHub2025] However, this station-level deduplication differs from event-level catalog matching; published literature indicates that specific duplicate event detection algorithms must be implemented separately. [@Docs2025]


## USGS libcomcat Library

The USGS libcomcat Python library provides command-line tools for querying ComCat, including the `findid` utility for finding events by ID or location/time parameters. [@01usgscomcatapi2025] The `-i` flag queries by event ID, while the `-a` flag returns all associated identifiers from contributing networks, potentially useful for discovering multiple IDs for the same event within ComCat. [@01usgscomcatapi2025][@03crossreferencefindings2025] Example usage `findid -i ci38572791 -a -r 200 -w 120` returns comprehensive event information including ID, time, location coordinates, depth, magnitude, distance calculations, temporal differences, and azimuth measurements. [@01usgscomcatapi2025] The tool works exclusively with ComCat event IDs from contributing source networks and does not provide cross-referencing with ISC Bulletin identifiers. [@03crossreferencefindings2025]


## ISC Grouping Algorithm

The ISC employs an automated algorithm that scores hypocenters using multiple quality metrics, compares location and origin time parameters, and groups, splits, or creates new events based on hypocenter scores and parameter comparison. [@02iscbulletinapi2025] This algorithm determines when different agency reports represent the same physical earthquake versus distinct events, effectively solving the duplicate detection problem as part of ISC's data integration workflow. [@02iscbulletinapi2025] ISC analysts subsequently review the automated groupings using the Visual Bulletin Analysis System (VBAS) to verify that hypocenter grouping and phase arrival associations are appropriate. [@02iscbulletinapi2025] The review process explicitly checks for "split events," instances where severely mis-located hypocenter solutions from contributing agencies led to the formation of two separate events in the bulletin when only one physical event occurred. [@02iscbulletinapi2025]


## Multiple Origins and Author Attribution

When ISC successfully groups origins, the resulting event contains multiple origin blocks, each tagged with an `AUTHOR` field identifying the contributing organization. [@02iscbulletinapi2025] Querying the ISC FDSN web service with the `contributor=NEIC` parameter returns events where NEIC contributed data and automatically sets `includeallorigins=true`, providing all agency solutions rather than just the prime origin. [@02iscbulletinapi2025] This architecture allows users to examine all agency determinations for a single physical event, including both ISC's reviewed solution and the original NEIC (USGS) hypocenter. [@02iscbulletinapi2025] However, the original NEIC report appears as a secondary origin within the ISC event structure without preserving the USGS ComCat event ID; only the agency name (NEIC) and parametric data are retained. [@02iscbulletinapi2025][@03crossreferencefindings2025]


## ISC Rebuild Project Lessons

The ISC Rebuild Project (Storchak et al. 2020) systematically reprocessed historical bulletin data and documented numerous cases of incorrectly grouped events. [@02iscbulletinapi2025] Examples include a Turkish observatory's event incorrectly cross-matched with a NEIC report due to data corruption, where identical P and S arrival times revealed the error. [@03crossreferencefindings2025] Such cases demonstrate that even with sophisticated algorithms and comprehensive parametric data, automated event association can fail, requiring expert review and correction. [@02iscbulletinapi2025][@03crossreferencefindings2025] The project's findings underscore the complexity of reliably matching earthquake events and the dangers of naive approaches that could merge distinct earthquakes based solely on spatiotemporal proximity. [@03crossreferencefindings2025]


## Critical Consideration: Aftershock and Swarm Exclusion

Any matching algorithm must explicitly account for aftershock sequences and earthquake swarms where numerous distinct events occur in close spatiotemporal proximity. [@Frontiers2025] The failure mode described in the task specification ("events within 50km and 60 seconds must be the same") would catastrophically merge mainshocks with their aftershocks, essentially destroying the scientific value of the merged catalog. [@Frontiers2025] Proper approaches implement nearest-neighbor matching rather than window-based matching, ensuring each event in catalog A matches at most one event in catalog B. [@Frontiers2025] Additional safeguards include examining the full spatiotemporal context (are there dozens of events nearby?), checking magnitude consistency across matched events, and flagging potential matches in known aftershock sequences for manual expert review. [@Frontiers2025][@OUP2025]


## Implementation Workflow

A practical implementation workflow involves the following steps: (1) Query USGS ComCat for events in the region and time period of interest using the FDSN web service with appropriate magnitude, location, and temporal filters. [@01usgscomcatapi2025] (2) Query ISC Bulletin using equivalent search parameters; note that ISC reviewed data is typically available 24 months after event occurrence. [@02iscbulletinapi2025] (3) For each ISC event, compute distances and time differences to all USGS events, identifying the nearest neighbor. [@Frontiers2025] (4) Filter candidate matches using threshold criteria (distance, time, magnitude difference). [@Nature2025] (5) Resolve ambiguous cases where multiple USGS events match a single ISC event or vice versa, typically by selecting the closest match and flagging others for manual review. [@Frontiers2025] (6) Validate results by examining events in known aftershock sequences and checking for implausible magnitude or location discrepancies. [@OUP2025]


## Special Cases and Exceptions

For earthquakes included in the ISC-GEM historical catalog (1900-2014), direct ID linkage exists via the `iscgem` entries in USGS ComCat's `ids` field. [@03crossreferencefindings2025][@USGS2025b] Users working with historical earthquakes should first check for ISC-GEM identifiers before implementing spatiotemporal matching. [@USGS2025b] For events outside ISC-GEM coverage (primarily post-2014), spatiotemporal matching remains necessary. [@03crossreferencefindings2025] Users should also note that USGS preferred event IDs can change over time as new analyses become available; the `ids` field provides historical tracking of identifier evolution. [@01usgscomcatapi2025] When ISC reprocesses events during their review cycle, origin time and location may shift slightly from initial NEIC determinations, potentially affecting threshold-based matching; magnitude comparisons should use consistent magnitude types (e.g., Mw) when available. [@02iscbulletinapi2025]


## Conclusion (File 2)

No official cross-reference mechanism exists for linking USGS ComCat event IDs with ISC Bulletin event IDs, with the exception of historical events covered by the ISC-GEM catalog (1900-2014). [@03crossreferencefindings2025][@USGS2025b] Earthquake catalog deduplication across these two fundamental global datasets requires spatiotemporal proximity matching using methods documented in peer-reviewed seismological literature. [@Frontiers2025][@Nature2025] Conservative distance (50-100 km), time (60-120 seconds), and magnitude (0.3-0.5 units) thresholds combined with nearest-neighbor matching algorithms provide the most reliable approach while avoiding catastrophic false positives that would merge mainshocks with aftershocks. [@Frontiers2025][@Nature2025] Understanding that seismologists at ISC solve this same problem during their data integration workflow—using automated algorithms, quality metrics, and expert review—provides confidence that the challenge, while complex, is solvable with appropriate methodological rigor. [@02iscbulletinapi2025]


## Summary (File 3)

No direct cross-reference mechanism exists between USGS ComCat event IDs and ISC Bulletin event IDs in official documentation. The USGS ComCat database contains 627,000 events with alphanumeric identifiers (e.g., `us6000m0xl`), while the ISC Bulletin contains 1.5 million events with numeric identifiers (8-11 digits). Although NEIC (part of USGS) contributes approximately one-third of all data to the ISC and ISC files are created to share data with ISC, no documented storage of ISC event IDs in USGS ComCat or USGS event IDs in ISC Bulletin was found. [@03crossreferencefindings2025]

The ISC Bulletin is considered the final global archive of parametric earthquake data, with reviewed versions published approximately 24 months after real-time operations. [@02iscbulletinapi2025]


## USGS ComCat Identifier System (File 3)

The USGS ComCat API returns events with three identifier-related fields: `id` (the current preferred identifier), `ids` (a comma-separated list of associated identifiers from multiple networks), and `sources` (a comma-separated list of contributing network codes). [@01usgscomcatapi2025]

The `id` field format consists of a network code prefix followed by a unique identifier. [@01usgscomcatapi2025] For example, `us6000m0xl` where `us` represents the USGS/NEIC network code. [@01usgscomcatapi2025] The documentation explicitly states that the preferred ID may change over time. [@01usgscomcatapi2025]

The `ids` field aggregates identifiers from multiple seismic networks that have reported the same event. [@01usgscomcatapi2025] An actual API query for event `us6000m0xl` returned identifiers from three networks: `",pt24001001,at00s6kml3,us6000m0xl,"` with corresponding sources `",pt,at,us,"`. [@03crossreferencefindings2025] Critically, no ISC identifiers were present in this response. [@03crossreferencefindings2025]

ComCat integrates data from multiple contributing networks including USGS/NEIC (`us`), Southern California Seismic Network (`ci`), Northern California Seismic Network (`nc`), Alaska Earthquake Center (`ak`), Pacific Tsunami Warning Center (`pt`), and many others. [@01usgscomcatapi2025] The documentation also lists incorporated historical catalogs including the ISC-GEM Main Catalog (1900-2010) and ISC-GEM Supplementary Catalog (1900-2010). [@01usgscomcatapi2025]


## ISC Bulletin Identifier System (File 3)

The ISC Bulletin uses numeric event identifiers (`EVENTID`) assigned by ISC, formatted as 8 characters in ISF 1.0 or 11 digits in ISF 2.1. [@02iscbulletinapi2025] Each origin block contains an `AUTHOR` field (9 characters) identifying the organization that computed the solution, such as ISC, NEIC, GCMT, JMA, or BJI. [@02iscbulletinapi2025]

The ISC collects data from approximately 90 currently active contributing agencies, with 600 agencies having contributed throughout the bulletin's history. [@02iscbulletinapi2025] Major contributors include NEIC (National Earthquake Information Center), USGS (United States Geological Survey), JMA (Japan Meteorological Agency), GFZ (German Research Centre for Geosciences), BJI (China Earthquake Networks Center), and GCMT/HRVD (Global Centroid Moment Tensor Project). [@02iscbulletinapi2025]

Different agencies' solutions for the same physical earthquake appear as separate origin blocks within a single ISC bulletin event. [@02iscbulletinapi2025] The ISC designates one solution as the "prime" (preferred) origin, with alternative solutions classified as secondary origins. [@02iscbulletinapi2025] The catalogue search returns only the prime hypocentre for each event, while the bulletin search returns both prime and secondary estimates. [@02iscbulletinapi2025]


## Data Flow Between USGS and ISC (File 3)

USGS documentation states that ISF (ISC Seismic Format) files are created to share data with the International Seismological Centre. [@03crossreferencefindings2025] The NEIC PDE (Preliminary Determination of Epicenters) program contributes approximately one-third of all data used by the ISC. [@03crossreferencefindings2025]

The ISF format includes parametric seismological data such as hypocenters, magnitudes, phase arrivals, and moment tensors. [@03crossreferencefindings2025] However, no documentation was found describing storage of original USGS event IDs in the ISC Bulletin, preservation of network-specific identifiers, or cross-reference tables linking USGS IDs to ISC IDs. [@03crossreferencefindings2025]

The ISC review process involves automated grouping followed by manual review. [@02iscbulletinapi2025] The automated algorithm scores hypocentres using multiple quality metrics, compares location and origin time parameters, and groups, splits, or creates new events based on these comparisons. [@02iscbulletinapi2025] Analysts then review groupings using the Visual Bulletin Analysis System (VBAS) to ensure appropriate association of phase arrivals and hypocentres. [@02iscbulletinapi2025]

The ISC Rebuild Paper (Storchak et al. 2020) documents instances where severely mis-located hypocentre solutions from reporting agencies led to the formation of two separate events in the original ISC Bulletin when only one physical event occurred, termed "split events." [@02iscbulletinapi2025] The paper provides an example where a Turkish observatory's event was incorrectly cross-matched with a NEIC report, with identical P and S arrival times suggesting data corruption. [@03crossreferencefindings2025][@Geoscienceletters2025]


## ID Format Incompatibility (File 3)

USGS ComCat and ISC Bulletin use fundamentally different identifier formats. [@03crossreferencefindings2025] USGS employs alphanumeric identifiers with network prefixes such as `us6000m0xl`, `ci15296281`, `pt24001001`, and `at00s6kml3`. [@03crossreferencefindings2025] In contrast, ISC uses purely numeric identifiers formatted as 8-character fields in ISF 1.0 or 11-digit fields in ISF 2.1. [@03crossreferencefindings2025]

The temporal workflow also differs significantly. USGS provides near real-time earthquake reporting through the PDE program, while ISC's reviewed bulletin is typically published 24 months after real-time operations. [@03crossreferencefindings2025] This temporal offset means events are initially reported by USGS and later integrated and re-assessed by ISC after collecting data from multiple global agencies. [@03crossreferencefindings2025]


## Academic Methods - Gardner and Knopoff (File 3)

The Gardner and Knopoff (1974) method is one of the most widely used declustering algorithms for probabilistic seismic hazard assessment. [@OUP2025] This mainshock-window method removes earthquakes within magnitude-dependent space-time windows around each potential mainshock, with larger windows for larger magnitude shocks. [WEB:Gardner & Knopoff search results]

The Reasenberg (1985) method uses adaptive space-time interaction zones based on Omori's Law. [WEB:Reasenberg search results] The spatial interaction relationship is defined by $\log d(\text{km}) = 0.4M_0 - 1.943 + k$, where $k = 1$ for distance to the largest earthquake and $k = 0$ for distance to the last earthquake. [WEB:Reasenberg search results] The algorithm also employs temporal parameters $\tau_{\min}$ (minimum look-ahead time) and $\tau_{\max}$ (maximum look-ahead time) for cluster formation. [WEB:Reasenberg search results]


## ISC Association Algorithm (File 3)

The time-based algorithm results in chance mis-associations and occasionally synthesizes fictitious events. [WEB:ISC association search results] Currently, these mis-associations are identified and corrected through manual intervention by seismologists who scrutinize the output for unlikely events and incorrect associations. [WEB:ISC association search results] The ISC does not publish explicit distance and time thresholds for event association, instead relying on manual review using the Visual Bulletin Analysis System. [@Geoscienceletters2025]

During the ISC Rebuild project, analysts manually reviewed events with considerable departures in epicenter or depth from previous solutions and those with large travel-time residuals at individual reporting stations. [@Geoscienceletters2025] Events were removed if they were supported only by hydro-acoustic networks, poorly constrained with single-agency reports and inadequate station coverage, or contained time stamp errors. [@Geoscienceletters2025]


## Tools - libcomcat (File 3)

The USGS libcomcat library provides a command-line tool called findid that can query events by ID and return all associated identifiers with the `-a` flag. [@01usgscomcatapi2025] The tool accepts IDs from any contributing source network and outputs comprehensive event information including time, location coordinates, depth, magnitude, distance calculations, temporal differences, and azimuth measurements. [@01usgscomcatapi2025] However, this tool works exclusively within the ComCat system and does not provide ISC event IDs. [@03crossreferencefindings2025]


## Recommendation (File 3)

Given the absence of official cross-reference mechanisms, matching earthquake events between USGS ComCat and ISC Bulletin requires implementing spatiotemporal proximity algorithms. [@03crossreferencefindings2025] The most reliable approach combines automated matching with manual validation of ambiguous cases, following the same methodology employed by the ISC itself. [WEB:ISC association search results][@Geoscienceletters2025]

Query both catalogs using overlapping spatiotemporal search windows rather than attempting one-to-one ID lookups. [@01usgscomcatapi2025][@02iscbulletinapi2025] The USGS API supports geographic searches via box coordinates or radial distance with magnitude filtering. [@01usgscomcatapi2025] The ISC API provides similar geographic search capabilities with the `includeallorigins=true` parameter to retrieve all contributing agency solutions. [@02iscbulletinapi2025] Comparing the NEIC-contributed origins within ISC events against USGS events provides the most direct matching path given NEIC's role as a major contributor to both systems. [@02iscbulletinapi2025][@03crossreferencefindings2025]


## Conclusion (File 3)

No direct cross-reference mechanism exists between USGS ComCat event IDs and ISC Bulletin event IDs. [@03crossreferencefindings2025] The two catalogs use incompatible identifier formats (alphanumeric with network prefixes versus purely numeric), operate on different timescales (real-time versus 24-month reviewed bulletin), and serve different purposes (comprehensive real-time reporting versus definitive global archive). [@01usgscomcatapi2025][@02iscbulletinapi2025][@03crossreferencefindings2025]

Seismologists address this challenge using spatiotemporal matching algorithms with magnitude-dependent distance and time windows, following established methods such as Gardner and Knopoff (1974) and Reasenberg (1985). [WEB:Gardner & Knopoff search results][WEB:Reasenberg search results] The ISC's own association process combines time-based algorithms with extensive manual review by expert seismologists. [WEB:ISC association search results][@Geoscienceletters2025] Any implementation of cross-catalog matching must similarly combine automated proximity algorithms with manual validation to prevent errors such as merging mainshocks with aftershocks or incorrectly associating events from earthquake swarms. [@task2025]

The most practical approach leverages the NEIC's role as a major contributor to both systems. [@03crossreferencefindings2025] Query ISC bulletin data with `contributor=NEIC` to retrieve origins computed by NEIC, then match these against USGS ComCat events using spatiotemporal proximity. [@02iscbulletinapi2025] This approach minimizes ambiguity by comparing solutions from the same source agency while accepting that some events will remain unmatchable due to differences in reporting coverage and quality control decisions between the two catalogs. [@02iscbulletinapi2025][@Geoscienceletters2025]
