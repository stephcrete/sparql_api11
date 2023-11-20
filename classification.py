from flask import render_template, request, jsonify
import config, sparql_query_templates, sparql_functions
import ssl

def read_all(agency_id, format=None):

    ssl._create_default_https_context = ssl._create_unverified_context

    if format == None:
        mime_type = request.headers['Accept']
        if mime_type.count(",") > 1 or mime_type == "*/*":
            mime_type = 'application/json'
        print(mime_type)
    else:
        mime_type = format

    sparql_ep = config.agencies[agency_id.lower()]['sparql_endpoint']
    print(sparql_ep)

    query = config.agencies[agency_id.lower()]['list_all']
    query = query.replace('~~default_lang~~', str(config.agencies[agency_id.lower()]['default_lang']))
    print(query)
    result = sparql_functions.getResponseText(sparql_ep, query, mime_type)

    return sparql_functions.serialize_response(result, mime_type)

