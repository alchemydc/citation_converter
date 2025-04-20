# Technical Context

## Technology Stack
- **Language**: Python 3.x
- **Package Management**: pip
- **Version Control**: Git

## Dependencies
1. **Core Libraries**
   - python-dotenv: Environment variable management
   - pubmed-id: PubMed API integration
   - tqdm: Progress bar visualization
   - requests: HTTP requests (via pubmed-id)

2. **Standard Library Usage**
   - `re`: Regular expressions for citation parsing
   - `os`: File and environment handling
   - `typing`: Type hints for better code clarity

## Project Structure
```
citation_converter/
├── input/
│   └── citations.txt
├── output/
│   └── decorated_citations.md
├── samples/
│   └── citations.txt
├── src/
│   └── citation_converter.py
├── setup.sh
├── setup.bat
├── requirements.txt
└── README.md
```

## Implementation Details
1. **Citation Processing**
   - Regular expressions for parsing citations
   - Component extraction (author, year, title, journal)
   - Fuzzy title matching for better PMID lookup
   - Original citation number preservation

2. **PubMed Integration**
   - Direct E-utilities API usage via pubmed-id
   - API key configuration through .env
   - Robust error handling for API requests
   - Not-found case handling

3. **Output Generation**
   - Markdown formatting
   - Clickable PubMed links
   - Clean, readable output format
   - Progress visualization during processing

## Setup Automation
1. **Cross-Platform Scripts**
   - `setup.sh` for Unix systems
   - `setup.bat` for Windows
   - Virtual environment creation
   - Dependencies installation
   - Directory structure setup
   - Sample data copying

2. **Environment Configuration**
   - `.env` file for API key
   - Configurable tool name and email
   - Easy setup instructions in README

## Code Organization
- Single script design for simplicity
- Clear function separation:
  - Citation reading
  - Citation parsing
  - PubMed querying
  - Output formatting
- Strong type hints throughout
- Comprehensive error handling
- Progress tracking integration

## Performance Features
- Progress bar for visual feedback
- Efficient API usage
- Graceful error handling
- Memory-efficient processing

## User Experience
- Simple command-line interface
- Clear progress indication
- Informative error messages
- Sample data for testing
- Markdown output for better usability

## Documentation
- Comprehensive README
- Clear setup instructions
- Usage examples
- Sample data included
- Configuration guidance
