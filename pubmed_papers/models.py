from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Author:
    name: str
    affiliation: Optional[str]
    email: Optional[str]

@dataclass
class Paper:
    pubmed_id: str
    title: str
    publication_date: str
    non_academic_authors: List[Author]
    company_affiliations: List[str]
    corresponding_author_email: Optional[str]
