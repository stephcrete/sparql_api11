from SPARQLWrapper import SPARQLWrapper, CSV, JSON, XML, TURTLE, RDFXML, JSONLD, N3
from rdflib import Graph
from flask import jsonify, make_response
import config


def getResponseText(endpoint, query, requestedMimeType):
    retFormat = config.SUPPORTED_MIME_FORMATS.get(requestedMimeType)

    client = SPARQLWrapper(endpoint)
    client.setQuery(query)

    if retFormat=='json':
        client.setReturnFormat(JSON)
        print("json")
        result = client.queryAndConvert()
    elif retFormat=='JSONLD':
        client.setReturnFormat(N3)
        result = client.query().convert()
        g = Graph().parse(data=result, format='n3')
        result = g.serialize(format='json-ld', indent=4)
    elif retFormat == 'xml':
        result = client.queryAndConvert().toxml()
    elif retFormat == 'turtle':
        client.setReturnFormat(N3)
        result = client.query().convert()
        g = Graph().parse(data=result, format='turtle')
        result = g.serialize(format='text/turtle')
    elif retFormat == 'rdf+xml':
        client.setReturnFormat(N3)
        result = client.query().convert()
        g = Graph().parse(data=result)
        result = g.serialize(format='pretty-xml')
    elif retFormat == 'csv':
        client.setReturnFormat(CSV)
        result = client.query().convert()
    else:
        print("else")
        result = client.queryAndConvert()

    return result


def serialize_response(result, mime_type):
    retFormat = config.SUPPORTED_MIME_FORMATS.get(mime_type)
    if retFormat in ['json']:
        #print(result)
        return jsonify(result)
    elif retFormat in ['json+ld', 'JSONLD']:
        #return jsonify(result)
        response = make_response(result)
        response.headers['Content-Disposition'] = "attachment; filename=myjson.json"
        return response
    elif retFormat == 'rdf+xml':
        response = make_response(result)
        response.headers['Content-Disposition'] = "attachment; filename=myxml.xml"
        return response
    elif retFormat == 'turtle':
        response = make_response(result)
        response.headers['Content-Disposition'] = "attachment; filename=myTurtle.ttl"
        return response
    elif retFormat == 'csv':
        response = make_response(result)
        response.headers['Content-Disposition'] = "attachment; filename=myCSV.csv"
        return response
    else:
        return result
    
