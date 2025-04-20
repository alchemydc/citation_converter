# System Patterns

## Final Architecture
Unified script with modular functions:
1. Citation Reading & Parsing
2. PubMed API Integration
3. Markdown Formatting
4. Progress Tracking
5. Error Handling

## Implementation Patterns
- **Factory Functions**: Clean function interfaces with type hints
- **Strategy Pattern**: Flexible citation parsing with regex
- **Iterator Pattern**: Line-by-line citation processing
- **Observer Pattern**: Progress bar for monitoring processing

## Data Flow
```mermaid
flowchart LR
    A[Input File] --> B[Citation Reader]
    B --> C[Citation Parser]
    C --> D[PubMed Querier]
    D --> E[Markdown Formatter]
    E --> F[Output File]
```

## Error Handling Patterns
1. **File Operations**
   - Input file not found
   - Output directory creation
   - File writing errors

2. **Citation Processing**
   - Invalid citation formats
   - Missing citation components
   - Number preservation

3. **PubMed Integration**
   - API connection errors
   - Rate limiting
   - Not found PMIDs
   - Invalid API key

4. **User Feedback**
   - Progress bar updates
   - Clear error messages
   - Processing status

## Component Architecture

### Citation Processing
- Regular expression based parsing
- Component extraction (author, year, title)
- Flexible format handling
- Number preservation

### PubMed Integration
- E-utilities API via pubmed-id
- Environment-based configuration
- Fuzzy title matching
- Error resilient queries

### Output Generation
- Markdown formatting
- Clickable links
- Clean formatting
- Progress indication

### Setup Automation
- Cross-platform scripts
- Directory structure
- Sample data
- Dependencies management

## Design Decisions
1. **Simplification**
   - Single script approach
   - Direct file operations
   - Clear function boundaries
   - Minimal dependencies

2. **User Experience**
   - Visual progress tracking
   - Clear error messages
   - Sample data included
   - Easy setup process

3. **Maintainability**
   - Modular functions
   - Strong typing
   - Clear documentation
   - Consistent formatting

## System Boundaries
- Input: Citation text file
- Processing: Local Python execution
- External: PubMed API calls
- Output: Markdown file with links

## Performance Considerations
- Memory efficient processing
- Progress visualization
- Error resilience
- Clean output format
