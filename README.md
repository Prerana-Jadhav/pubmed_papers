# 📄 get-papers-list

A Python command-line tool and library to fetch PubMed research papers based on a user-provided query, identifying papers with at least one author affiliated with pharmaceutical or biotech companies. Results can be saved as a CSV file or printed to the console.

---

## 📌 Features

- Query PubMed using its full query syntax
- Filter papers to find **non-academic authors** using email domain and affiliation heuristics
- Extract details:
  - PubMed ID
  - Title
  - Publication Date
  - Non-academic Authors
  - Company Affiliations
  - Corresponding Author Email
- Output results to a CSV file or the console
- Command-line options for debug mode, output filename, and help
- Fully typed Python code
- Poetry for dependency management
- Modular codebase (library + CLI)
- Published to **Test PyPI**

---

## 📁 Code Organization
## 🛠️ Installation

### Prerequisites
- Python 3.8+
- Poetry

### Install dependencies
```bash
poetry install