# PubMed Papers Fetcher
A Python-based command-line tool to search PubMed for research papers matching a user-defined query, and filter those that have at least one non-academic author affiliated with pharmaceutical or biotech companies.

# Key Features
Search PubMed using full query syntax support.

Identify non-academic authors using custom heuristics.

Extract corresponding author email addresses.

Output results to the console or CSV file.

Modular code structure with a typed Python core module and a separate CLI.

Configurable via command-line options like --debug and --file.

# Tech Stack
Python 3

Poetry for packaging and dependency management

Click for CLI

Requests for HTTP API calls

# Bonus
Modularized for reuse

Compatible with TestPyPI publishing

Supports extension via additional heuristics for affiliation detection.

# Usage Example
bash
Copy
Edit
poetry run get-papers-list "cancer immunotherapy" --debug --file results.csv
