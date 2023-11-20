import sparql_query_templates

agencies = dict(
    fao = dict(
        sparql_endpoint = 'https://stats.fao.org/caliper/sparql/AllVocs',
        default_lang = 'en',
        list_all = sparql_query_templates.list_all_classifications,
        list_items = sparql_query_templates.get_classification_items_estat,
        list_items_rdf = sparql_query_templates.get_classification_items_rdf
    ),
    estat = dict(
        sparql_endpoint = 'https://publications.europa.eu/webapi/rdf/sparql',
        default_lang = 'en',
        list_all = sparql_query_templates.list_all_classifications,
        list_items = sparql_query_templates.get_classification_items_estat,
        list_items_rdf = sparql_query_templates.get_classification_items_rdf
    ),
    insee = dict(
        sparql_endpoint = 'https://rdf.insee.fr/sparql',
        default_lang = 'fr',
        list_all = sparql_query_templates.list_all_classifications,
        list_items = sparql_query_templates.get_classification_items_estat,
        list_items_rdf = sparql_query_templates.get_classification_items_rdf
    )
)


SUPPORTED_MIME_FORMATS = {
        'application/json': 'json', 
        'text/json' : 'json',
        'JSON' : 'json',
        'application/XML' : 'xml',
        'XML' : 'xml',
        'CSV' : 'csv', 
        'text/csv' : 'csv',
        'rdf+xml' : 'rdf+xml',
        'TURTLE' : 'turtle',
        'turtle' : 'turtle',
        'RDFXML' : 'rdf+xml',
        'application/ld+json' : 'ld+json',
        'JSONLD': 'JSONLD',
        'json-ld': 'JSONLD'
    }