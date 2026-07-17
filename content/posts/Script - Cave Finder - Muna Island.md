---
title: Script - Cave Finder - Muna Island
created: 2026-01-26
updated: 2025-11-03
status: seed
draft: false
tags:
  - diving
  - python
  - script
related:
  - "[[Scripts]]"
  - "[[Sulawesi]]"
  - "[[Trips - Ideas]]"
  - "[[Exploration]]"
  - "[[CaveDB]]"
language: Python
---
```python
import json
import requests
import csv
import time

API_KEY = 'YOUR GOOGLE API'  # Replace with your API key

# Keywords likely to return cave/sinkhole/bathing spring results
KEYWORDS = [
    'goa', 'gua', 'lubang', 'sumur alam', 'serambi alam',
    'lembah', 'grotto', 'cave', 'hole',
    'loji', 'koo', 'luban', 'permandian'
]

# Approximate coverage of Muna Island
TILE_LOCATIONS = [
    '-4.783,122.566',  # Raha
    '-5.000,122.500',  # Southwest
    '-4.600,122.700',  # Northeast
    '-4.900,122.700'   # Southeast
]

RADIUS = 50000  # 50km radius — max allowed
OUTPUT_CSV = 'muna_island_places.csv'

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
            print(f"Searching for '{keyword}' near {location}")
            data = search_places(keyword, location, RADIUS)
            all_results.extend(data.get('results', []))
  
            while 'next_page_token' in data:
                time.sleep(2)
                token = data['next_page_token']
                data = search_places(keyword, location, RADIUS, token)
                all_results.extend(data.get('results', []))
  
    # Deduplicate by place_id
    deduped = {place['place_id']: place for place in all_results}
    return list(deduped.values())
  
def save_to_csv(places, filename):
    fieldnames = ['name', 'address', 'latitude', 'longitude', 'types', 'place_id']
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for place in places:
            writer.writerow({
                'name': place.get('name'),
                'address': place.get('vicinity'),
                'latitude': place['geometry']['location']['lat'],
                'longitude': place['geometry']['location']['lng'],
                'types': ', '.join(place.get('types', [])),
                'place_id': place.get('place_id')
            })
  
if __name__ == '__main__':
    results = collect_all_places()
    save_to_csv(results, OUTPUT_CSV)
    print(f"\nSaved {len(results)} unique places to '{OUTPUT_CSV}'")
```
