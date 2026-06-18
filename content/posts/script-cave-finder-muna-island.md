---
title: Script - Cave Finder - Muna Island
created: 2026-01-26
updated: 2025-11-03
status: seed
draft: false
tags:
  - Diving
  - Python
  - Script
---
Related: Sulawesi - Indonesia Expedition Ideas [Exploration](/posts/exploration/) [CaveDB](/posts/cavedb/)

```python
import json
import requests
import csv
import time

API_KEY = 'YOUR GOOGLE API' Â # Replace with your API key

# Keywords likely to return cave/sinkhole/bathing spring results
KEYWORDS = [
Â  Â  'goa', 'gua', 'lubang', 'sumur alam', 'serambi alam',
Â  Â  'lembah', 'grotto', 'cave', 'hole',
Â  Â  'loji', 'koo', 'luban', 'permandian'
]

# Approximate coverage of Muna Island
TILE_LOCATIONS = [
Â  Â  '-4.783,122.566', Â # Raha
Â  Â  '-5.000,122.500', Â # Southwest
Â  Â  '-4.600,122.700', Â # Northeast
Â  Â  '-4.900,122.700' Â  # Southeast
]

RADIUS = 50000 Â # 50km radius â€” max allowed
OUTPUT_CSV = 'muna_island_places.csv'

def search_places(keyword, location, radius, token=None):
Â  Â  url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
Â  Â  params = {
Â  Â  Â  Â  'key': API_KEY,
Â  Â  Â  Â  'keyword': keyword,
Â  Â  Â  Â  'location': location,
Â  Â  Â  Â  'radius': radius,
Â  Â  }
Â  Â  if token:
Â  Â  Â  Â  params['pagetoken'] = token
  
Â  Â  response = requests.get(url, params=params)
Â  Â  return response.json()
  
def collect_all_places():
Â  Â  all_results = [] 
Â  Â  for location in TILE_LOCATIONS:
Â  Â  Â  Â  for keyword in KEYWORDS:
Â  Â  Â  Â  Â  Â  print(f"Searching for '{keyword}' near {location}")
Â  Â  Â  Â  Â  Â  data = search_places(keyword, location, RADIUS)
Â  Â  Â  Â  Â  Â  all_results.extend(data.get('results', []))
  
Â  Â  Â  Â  Â  Â  while 'next_page_token' in data:
Â  Â  Â  Â  Â  Â  Â  Â  time.sleep(2)
Â  Â  Â  Â  Â  Â  Â  Â  token = data['next_page_token']
Â  Â  Â  Â  Â  Â  Â  Â  data = search_places(keyword, location, RADIUS, token)
Â  Â  Â  Â  Â  Â  Â  Â  all_results.extend(data.get('results', []))
  
Â  Â  # Deduplicate by place_id
Â  Â  deduped = {place['place_id']: place for place in all_results}
Â  Â  return list(deduped.values())
  
def save_to_csv(places, filename):
Â  Â  fieldnames = ['name', 'address', 'latitude', 'longitude', 'types', 'place_id']
Â  Â  with open(filename, 'w', newline='', encoding='utf-8') as f:
Â  Â  Â  Â  writer = csv.DictWriter(f, fieldnames=fieldnames)
Â  Â  Â  Â  writer.writeheader()
Â  Â  Â  Â  for place in places:
Â  Â  Â  Â  Â  Â  writer.writerow({
Â  Â  Â  Â  Â  Â  Â  Â  'name': place.get('name'),
Â  Â  Â  Â  Â  Â  Â  Â  'address': place.get('vicinity'),
Â  Â  Â  Â  Â  Â  Â  Â  'latitude': place['geometry']['location']['lat'],
Â  Â  Â  Â  Â  Â  Â  Â  'longitude': place['geometry']['location']['lng'],
Â  Â  Â  Â  Â  Â  Â  Â  'types': ', '.join(place.get('types', [])),
Â  Â  Â  Â  Â  Â  Â  Â  'place_id': place.get('place_id')
Â  Â  Â  Â  Â  Â  })
  
if __name__ == '__main__':
Â  Â  results = collect_all_places()
Â  Â  save_to_csv(results, OUTPUT_CSV)
Â  Â  print(f"\nSaved {len(results)} unique places to '{OUTPUT_CSV}'")
```
