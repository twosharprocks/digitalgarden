---
title: Script - Cave Finder - Vanuatu
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
  - "[[Vanuatu]]"
  - "[[Expedition Ideas]]"
  - "[[Exploration]]"
  - "[[CaveDB]]"
language: Python
---
```python
import requests
import json
import time

API_KEY = 'YOUR_GOOGLE_MAPS_API_KEY'  # Replace with your actual API key

# Keywords including English and local/regional cave-related terms
KEYWORDS = ['cave', 'hole', 'grotto']

# Approximate central points covering Vanuatu's main islands (lat, long)
TILE_LOCATIONS = [
    '-15.3767,166.9592',  # Espiritu Santo
    '-17.7404,168.3215',  # Efate (Port Vila)
    '-19.5333,169.2833',  # Tanna Island
    '-16.5167,167.4167',  # Malekula
    '-13.8333,167.6667',  # Banks Islands
]

RADIUS = 50000  # Max for Google Maps Places API (50 km)
OUTPUT_FILE = 'vanuatu_caves.json'

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
            print(f"Searching '{keyword}' around {location}")
            data = search_places(keyword, location, RADIUS)
            all_results.extend(data.get('results', []))

            # Handle pagination
            while 'next_page_token' in data:
                time.sleep(2)  # Required delay before next_page_token works
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

