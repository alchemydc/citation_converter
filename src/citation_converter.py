#!/usr/bin/env python3

import os
import re
import requests
from dotenv import load_dotenv
from typing import List, Optional, Tuple
from tqdm import tqdm

def read_citations(input_file: str) -> List[Tuple[int, str]]:
    """Read citations from input file, returning list of (number, citation) tuples."""
    citations = []
    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # Extract citation number and text
            try:
                num, citation = line.split('. ', 1)
                citations.append((int(num), citation))
            except ValueError:
                print(f"Warning: Could not parse line: {line}")
                continue
    return citations

def parse_citation(citation: str) -> Tuple[str, str, str, str]:
    """Parse a citation into its components."""
    # Extract year
    year_match = re.search(r'\((\d{4})\)', citation)
    year = year_match.group(1) if year_match else ""
    
    # Extract authors (first author)
    author_match = re.search(r'^[^(]+', citation)
    first_author = author_match.group(0).split(',')[0].strip() if author_match else ""
    
    # Extract title (between ). and .)
    title_match = re.search(r'\)\.\s*([^.]+)', citation)
    title = title_match.group(1).strip() if title_match else ""
    
    # Extract journal (everything between the last . and the volume/page numbers)
    parts = citation.split(')')[-1].split('.')
    if len(parts) > 1:
        journal_part = parts[-1]
        journal_match = re.search(r'^[^0-9]+', journal_part)
        journal = journal_match.group(0).strip() if journal_match else ""
    else:
        journal = ""
    
    return first_author, year, title, journal

def get_pmid_for_citation(citation: str, api_key: str, tool: str = "citation_converter", email: str = "example@example.com") -> Optional[str]:
    """Query PubMed to get PMID for a citation."""
    try:
        # Parse citation
        author, year, title, journal = parse_citation(citation)
        
        # Build search query - make title and journal optional
        query_parts = []
        if author:
            query_parts.append(f"{author}[Author]")
        if year:
            query_parts.append(f"{year}[Year]")
        if title:
            query_parts.append(f"({title}[Title] OR {title}[Title:~0.8])")  # Allow for some fuzziness in title
        if journal:
            query_parts.append(f"{journal}[Journal]")
        
        query = " AND ".join(query_parts)
        
        # Query PubMed
        base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
        params = {
            "db": "pubmed",
            "term": query,
            "api_key": api_key,
            "tool": tool,
            "email": email,
            "retmode": "json"
        }
        
        response = requests.get(base_url, params=params)
        result = response.json()
        
        # Extract PMID from result
        if 'esearchresult' in result and 'idlist' in result['esearchresult'] and result['esearchresult']['idlist']:
            return result['esearchresult']['idlist'][0]
    except Exception as e:
        print(f"Error querying PubMed: {e}")
        return None

def decorate_citation(num: int, citation: str, pmid: Optional[str]) -> str:
    """Format citation with its number, PMID, and hyperlink in markdown format."""
    if pmid:
        return f"{num}. {citation} [PMID: {pmid}](https://pubmed.ncbi.nlm.nih.gov/{pmid})"
    return f"{num}. {citation} [PMID: Not found]"

def main():
    # Load environment variables
    load_dotenv()
    api_key = os.getenv('API_KEY')
    if not api_key:
        print("Error: API_KEY not found in .env file")
        return

    input_file = "input/citations.txt"
    output_file = "output/decorated_citations.md"

    # Read citations
    print("Reading citations...")
    citations = read_citations(input_file)
    
    # Process citations, get PMIDs, and add hyperlinks
    print("Processing citations...")
    decorated_citations = []
    for num, citation in tqdm(citations):
        pmid = get_pmid_for_citation(citation, api_key)
        decorated = decorate_citation(num, citation, pmid)
        decorated_citations.append(decorated)
    
    # Write results
    print("Writing markdown results...")
    with open(output_file, 'w') as f:
        f.write("# Citations with PubMed Links\n\n")
        for citation in decorated_citations:
            f.write(f"{citation}\n")
    
    print(f"Done! Processed {len(citations)} citations and saved as markdown.")

if __name__ == "__main__":
    main()
