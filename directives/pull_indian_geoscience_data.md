# SOP: Pull & Process Indian Geoscience, Land Features & Well Log Tools

## Objective
Retrieve, curate, and structure spatial shapefiles, geological boundary layers, Indian land features, and LAS/DLIS well log conversion tools to power the NWIS backend, database, and GIS correlation engine.

## Priority Sources & Repositories
1. **Indian Land Features**: `https://github.com/ramSeraph/indian_land_features.git`
2. **HindustanTimesLabs Shapefiles**: `https://github.com/HindustanTimesLabs/shapefiles.git` (State/District/Assembly boundaries)
3. **IMD Shapefiles**: `https://github.com/India-Meteorological-Department/India-shapefiles.git`
4. **India Shapefiles Bundle**: `https://github.com/data014/India-Shapefiles-Bundle.git`
5. **MIVAA LAS/DLIS to JSON Converter**: `https://github.com/MIVAA-ai/mivaa-las-dlis-to-json-convertor.git`
6. **LAS-py Parser Library**: `https://github.com/laslibs/las-py.git`
7. **NGDR (National Geoscience Data Repository) & DGH NDR**: Investigate schemas, releases, basin layers, and API endpoints.

## Execution Pattern
- Execute via `execution/pull_geoscience_data.py`.
- Repositories are cloned with `--depth 1` into `.tmp/repos/`.
- Crucial spatial assets (.shp, .geojson, .kml, parsers) are categorized into `data/spatial/` and `data/parsers/`.
- Generate an index catalog (`data/catalog.json`) describing all acquired datasets, CRS projections, and database ingestion readiness.
