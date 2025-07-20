import click
from pubmed_papers import pubmed_api, parser, exporter

@click.command()
@click.argument('query')
@click.option('-d', '--debug', is_flag=True, help='Enable debug output')
@click.option('-f', '--file', type=str, help='Filename to save results')
def main(query, debug, file):
    if debug:
        click.echo(f"Fetching PubMed IDs for query: {query}")

    ids = pubmed_api.fetch_pubmed_ids(query)
    papers = []

    for pid in ids:
        xml_data = pubmed_api.fetch_paper_details(pid)
        paper = parser.parse_paper(xml_data)
        if paper.non_academic_authors:
            papers.append(paper)

    if file:
        exporter.export_to_csv(papers, file)
        click.echo(f"Results written to {file}")
    else:
        for paper in papers:
            click.echo(paper)

if __name__ == '__main__':
    main()
