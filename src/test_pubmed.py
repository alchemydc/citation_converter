#!/usr/bin/env python3

from dotenv import load_dotenv
import os
import pubmed_id

# Load API key
load_dotenv()
api_key = os.getenv('API_KEY')
print(f"API Key loaded: {'Yes' if api_key else 'No'}")

# Print available functions/attributes in the module
print("\nAvailable in pubmed_id module:")
for item in dir(pubmed_id):
    if not item.startswith('_'):
        print(f"- {item}")

# Try to use a sample citation
test_citation = "Voeltz, GK, Prinz WA, Shibata Y, Rist JM and Rapoport TA (2006). A class of membrane proteins shaping the tubular endoplasmic reticulum. Cell 124, 573–586."
print("\nTesting with sample citation:", test_citation)

# Try potential functions/methods
# Print methods in the api module
print("\nMethods in api module:")
for item in dir(pubmed_id.api):
    if not item.startswith('_'):
        print(f"- {item}")

# Try using direct API call to esearch endpoint
import requests

try:
    print("\nTrying direct PubMed search...")
    # Build the query from the citation
    authors = "Voeltz GK"
    year = "2006"
    title = "A class of membrane proteins shaping the tubular endoplasmic reticulum"
    journal = "Cell"
    
    query = f"{authors}[Author] AND {year}[Year] AND {title}[Title] AND {journal}[Journal]"
    
    # Make the API request to esearch
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "api_key": api_key,
        "tool": "citation_converter",
        "email": "example@example.com",
        "retmode": "json"
    }
    
    response = requests.get(base_url, params=params)
    result = response.json()
    print("Search Result:", result)
    
    if 'esearchresult' in result and 'idlist' in result['esearchresult']:
        pmid = result['esearchresult']['idlist'][0]
        print(f"Found PMID: {pmid}")
        
        # Now try to get details using the PubMedAPI with the found PMID
        api = pubmed_id.PubMedAPI()
        api.email = "example@example.com"
        api.tool = "citation_converter"
        details = api.api(pmid)
        print("\nPubMed API Result:", details)
    
except Exception as e:
    print("\nError:", e)
