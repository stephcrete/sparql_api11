from flask import render_template, request, jsonify
import config, sparql_query_templates, sparql_functions
import ssl

def read_one_item_by_uri(agency_id, uri, code_id, format=None):
    ssl._create_default_https_context = ssl._create_unverified_context

    if format == None:
        mime_type = request.headers['Accept']
        if mime_type.count(",") > 1:
            mime_type = 'application/json'
        print(mime_type)
    else:
        mime_type = format

    sparql_ep = config.agencies[agency_id.lower()]['sparql_endpoint']

    retFormat = config.SUPPORTED_MIME_FORMATS.get(mime_type)
    if retFormat.lower() in ["rdf+xml", "turtle", "ld+json", "jsonld", "json-ld"]:
        query = config.agencies[agency_id.lower()]['list_items_rdf']
        query = query.replace('~~item_condition~~', str("skos:notation '" + code_id + "' ;"))
    else:
        query = config.agencies[agency_id.lower()]['list_items']
        query = query.replace('~~item_condition~~', str("FILTER(?notation='" + code_id + "')"))

    query = query.replace('~~uri~~', str(uri))
    query = query.replace('~~default_lang~~', str(config.agencies[agency_id.lower()]['default_lang']))
    print(query)

    result = sparql_functions.getResponseText(sparql_ep, query, mime_type)
    return sparql_functions.serialize_response(result, mime_type)


def read_one_by_notation(agency_id, notation, format=None):
    ssl._create_default_https_context = ssl._create_unverified_context
    if format == None:
        mime_type = request.headers['Accept']
        if mime_type.count(",") > 1:
            mime_type = 'application/json'
        print(mime_type)
    else:
        mime_type = format

    sparql_ep = config.agencies[agency_id.lower()]['sparql_endpoint']
    print(sparql_ep)

    if notation != None:
        print(notation)

    query = sparql_query_templates.get_classificationURI_byNotation
    query = query.replace('~~notation~~', str(notation))
    query = query.replace('~~default_lang~~', str(config.agencies[agency_id.lower()]['default_lang']))
    result = sparql_functions.getResponseText(sparql_ep, query, "JSON")
    print(jsonify(result))
    if not (result["results"]["bindings"]):
        return("Can't find a classification with the notation: " + notation)
    uri = result["results"]["bindings"][0]['scheme']['value']
    print(uri)

    retFormat = config.SUPPORTED_MIME_FORMATS.get(mime_type)
    if retFormat.lower() in ["rdf+xml", "turtle", "ld+json", "jsonld", "json-ld"]:
        query = config.agencies[agency_id.lower()]['list_items_rdf']
    else:
        query = config.agencies[agency_id.lower()]['list_items']

    query = query.replace('~~uri~~', str(uri))
    query = query.replace('~~item_condition~~', str(""))
    query = query.replace('~~default_lang~~', str(config.agencies[agency_id.lower()]['default_lang']))

    result = sparql_functions.getResponseText(sparql_ep, query, mime_type)
    return sparql_functions.serialize_response(result, mime_type)

def read_one_by_uri(agency_id, uri, format=None):
    ssl._create_default_https_context = ssl._create_unverified_context

    if format == None:
        mime_type = request.headers['Accept']
        if mime_type.count(",") > 1:
            mime_type = 'application/json'
        print(mime_type)
    else:
        mime_type = format

    sparql_ep = config.agencies[agency_id.lower()]['sparql_endpoint']

    retFormat = config.SUPPORTED_MIME_FORMATS.get(mime_type)
    if retFormat.lower() in ["rdf+xml", "turtle", "ld+json", "jsonld", "json-ld"]:
        query = config.agencies[agency_id.lower()]['list_items_rdf']
    else:
        query = config.agencies[agency_id.lower()]['list_items']

    query = query.replace('~~uri~~', str(uri))
    query = query.replace('~~item_condition~~', str(""))
    query = query.replace('~~default_lang~~', str(config.agencies[agency_id.lower()]['default_lang']))

    result = sparql_functions.getResponseText(sparql_ep, query, mime_type)
    return sparql_functions.serialize_response(result, mime_type)


