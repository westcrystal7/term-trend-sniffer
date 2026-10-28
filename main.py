import requests
import re
from datetime import date

# Simulate fetching from X/GitHub/HF sitemaps (replace with real endpoints)
SOURCES = [
    'https://github.com/trending',
    'https://huggingface.co/models',
    'https://x.com/search?q=AI%20model'
]

# Mock data for demo - in real use, parse HTML/API
MOCK_TEXTS = [
    'New model "Llama-4" and "DeepSeek-R2" trending',
    'Repo "solid-glass" and "folkbench" are hot today',
    'Product "MotionMaxxing" appears on X'
]

# Simple heuristic: extract CamelCase or hyphenated names with numbers/words
PATTERN = r'\b[A-Z][a-z]+(?:[-_][A-Za-z0-9]+)*\b'

seen = set()
new_terms = []

today = date.today().isoformat()

print(f'=== AI Term Radar - {today} ===')

# In real implementation, fetch actual content and filter by recency
for text in MOCK_TEXTS:
    matches = re.findall(PATTERN, text)
    for term in matches:
        # Filter out common words and in-sentence caps
        if term.lower() in ['new', 'the', 'and', 'for']:
            continue
        if term not in seen:
            seen.add(term)
            new_terms.append(term)
            print(f'  + New term: {term}')

# Deduplicate and sort (in real scenario, check against yesterday's list)
if not new_terms:
    print('  No new terms today')

# Future: push to a JSON file or database for daily tracking
with open('new_terms_log.json', 'a') as f:
    import json
    json.dump({'date': today, 'terms': new_terms}, f)
    f.write('\n')

print(f'\nLogged {len(new_terms)} new terms to new_terms_log.json')
