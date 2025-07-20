def is_non_academic(affiliation: str) -> bool:
    academic_keywords = ['university', 'institute', 'college', 'school', 'hospital', 'laboratory', 'centre', 'center']
    return not any(word.lower() in affiliation.lower() for word in academic_keywords)
