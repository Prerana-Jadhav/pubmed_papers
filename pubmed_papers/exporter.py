import csv
from typing import List
from .models import Paper

def export_to_csv(papers: List[Paper], filename: str):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['PubmedID', 'Title', 'Publication Date', 'Non-academic Author(s)', 'Company Affiliation(s)', 'Corresponding Author Email'])

        for paper in papers:
            non_acad_names = '; '.join(a.name for a in paper.non_academic_authors)
            affiliations = '; '.join(paper.company_affiliations)
            writer.writerow([paper.pubmed_id, paper.title, paper.publication_date, non_acad_names, affiliations, paper.corresponding_author_email or ""])
