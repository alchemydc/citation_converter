# Product Context

## Problem Space
Scientific citations need to be associated with their PubMed IDs (PMIDs) for tracking and reference purposes. Manually looking up PMIDs for a large list of citations is time-consuming and error-prone.

## Solution
Automated script that processes a list of citations, queries the PubMed database to find corresponding PMIDs, and decorates each citation with its PMID.

## User Experience Goals
- Minimal setup required
- Fast processing of citation lists
- Clear feedback on successful/failed PMID lookups
- Easy to understand output format
- Handles common citation formats reliably

## Success Criteria
- Correctly identifies PMIDs for well-formed citations
- Creates properly formatted output file
- Processes entire citation list without manual intervention
- Provides clear indication of any citations that couldn't be matched

## Usage Workflow
1. User prepares input file with list of citations
2. User runs script
3. Script processes citations and creates decorated output
4. User can review output file for decorated citations
