from xml.etree import ElementTree as ET
from .models import Paper, Author
from .heuristics import is_non_academic

def parse_paper(xml_data: str) -> Paper:
    root = ET.fromstring(xml_data)
    article = root.find('.//PubmedArticle')
    pubmed_id = article.findtext('.//PMID')
    title = article.findtext('.//ArticleTitle')
    date = article.findtext('.//PubDate/Year') or "Unknown"

    authors = []
    for author in article.findall('.//Author'):
        name = f"{author.findtext('ForeName', '')} {author.findtext('LastName', '')}".strip()
        affiliation = author.findtext('.//Affiliation')
        email = None
        if affiliation:
            import re
            email_match = re.search(r'[\w\.-]+@[\w\.-]+', affiliation)
            email = email_match.group(0) if email_match else None
        authors.append(Author(name=name, affiliation=affiliation, email=email))

    non_academic_authors = [a for a in authors if a.affiliation and is_non_academic(a.affiliation)]
    company_affiliations = list({a.affiliation for a in non_academic_authors if a.affiliation})
    corresponding_email = next((a.email for a in authors if a.email), None)

    return Paper(pubmed_id, title, date, non_academic_authors, company_affiliations, corresponding_email)
