# Citation Converter

A tool to automatically find and add PubMed IDs (PMIDs) to academic citations.

## Features

- Searches PubMed for citations and retrieves their PMIDs
- Adds PMIDs and PubMed hyperlinks to citations
- Progress bar shows processing status
- Supports both plain text and markdown output formats

## Setup

### Prerequisites

- Python 3.x
- A PubMed API key (can be obtained from NCBI)

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/citation_converter.git
   cd citation_converter
   ```

2. Create a `.env` file in the root directory and add your PubMed API key:
   ```
   API_KEY=your_api_key_here
   ```

3. Run the setup script:
   - On Unix/MacOS:
     ```bash
     chmod +x setup.sh
     ./setup.sh
     ```
   - On Windows:
     ```batch
     setup.bat
     ```

## Usage

1. Place your citations in `input/citations.txt`, one per line

2. Run the citation converter:
   ```bash
   python src/citation_converter.py
   ```

3. Find your results in `output/decorated_citations.md`:
   - Citations with PMIDs
   - Clickable PubMed links in markdown format
