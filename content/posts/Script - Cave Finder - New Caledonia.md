---
title: Script - Cave Finder - New Caledonia
created: 2026-01-26
updated: 2025-11-03
status: seed
draft: false
tags:
  - diving
  - python
  - script
Related:
  - "[[Scripts]]"
  - "[[Trips - Ideas]]"
  - "[[Exploration]]"
  - "[[CaveDB]]"
  - "[[Caving]]"
language: Python
---
```python
import requests
import json
import time

API_KEY = 'YOUR_GOOGLE_MAPS_API_KEY'  # Replace this with your valid API key

KEYWORDS = [
    'cave', 'hole', 'grotto',               # English
    'grotte', 'caverne', 'trou', 'aven',    # French
    'puits naturel', 'faille',              # Other French karst terms
    'mu', 'koo', 'kou'                      # Local (Drehu, Paicî)
]

TILE_LOCATIONS = [
    '-21.25,165.3',     # Nouméa
    '-20.8,165.1',      # Central Grande Terre
    '-20.2,164.7',      # Northern Grande Terre
    '-20.9,167.25',     # Île des Pins
    '-20.6,167.0',      # Lifou
    '-21.0,167.5',      # Maré
    '-20.4,166.6'       # Ouvéa
]

RADIUS = 50000  # Max for Google Maps Places API
OUTPUT_FILE = 'new_caledonia_caves.json'

def search_places(keyword, location, radius, token=None):
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    params = {
        'key': API_KEY,
        'keyword': keyword,
        'location': location,
        'radius': radius,
    }
    if token:
        params['pagetoken'] = token

    response = requests.get(url, params=params)
    return response.json()

def collect_all_places():
    all_results = []

    for location in TILE_LOCATIONS:
        for keyword in KEYWORDS:
            print(f"Searching '{keyword}' near {location}")
            data = search_places(keyword, location, RADIUS)
            all_results.extend(data.get('results', []))

            # Handle paginated results
            while 'next_page_token' in data:
                time.sleep(2)
                token = data['next_page_token']
                data = search_places(keyword, location, RADIUS, token)
                all_results.extend(data.get('results', []))

    # Deduplicate by place_id
    deduped_results = {place['place_id']: place for place in all_results}
    return list(deduped_results.values())

def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    places = collect_all_places()
    save_to_json(places, OUTPUT_FILE)
    print(f"\nSaved {len(places)} unique cave-related places to '{OUTPUT_FILE}'")
```

---

