list_all_classifications = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

    SELECT  ?scheme ?notation ?label WHERE {
    ?scheme rdf:type skos:ConceptScheme .
    OPTIONAL {?scheme skos:notation ?notation }.
    OPTIONAL {?scheme skos:prefLabel ?label . FILTER(lang(?label)='~~default_lang~~') }.
    }
    ORDER BY ASC(?notation)
    """

get_classificationURI_byNotation = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

    SELECT  ?scheme ?notation ?label WHERE {
    ?scheme rdf:type skos:ConceptScheme .
    ?scheme skos:notation ?notation . FILTER(?notation='~~notation~~') .
    ?scheme skos:prefLabel ?label . FILTER(lang(?label)='~~default_lang~~') .
    }
    ORDER BY ASC(?notation)
    """
get_classification_items_fao = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

    SELECT  DISTINCT ?code (MAX(?broaderCodes) as ?broader) ?label  WHERE {
    ?concept rdf:type skos:Concept . 
    ?concept skos:inScheme ?concept_scheme . FILTER regex(str(?concept_scheme),'~~uri~~') .
    ?concept skos:notation ?code .
    OPTIONAL {?concept skos:broader ?broader_concept . ?broader_concept skos:notation ?broaderCode1 . BIND(?broaderCode1 as ?broaderCodes)} 
    ?concept skos:prefLabel ?label . FILTER(lang(?label)='~~default_lang~~') .
    }
    GROUP BY ?code ?broader ?label 
    ORDER BY ?code
    """

get_classification_items_estat = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

    SELECT ?s ?code ?Broader_code ?label WHERE {
    ?s a skos:Concept ;
        skos:inScheme <~~uri~~> ;
        skos:prefLabel ?label ;
        skos:notation ?notation .
        OPTIONAL {?s skos:broader ?BT.  
        ?BT skos:notation ?BT_notation .}
            FILTER(lang(?label)='~~default_lang~~')
            ~~item_condition~~
        BIND (STR(?notation) as ?code)
        BIND (STR(?BT_notation) as ?Broader_code)
    }order by ?code
"""

get_classification_items_rdf = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

    CONSTRUCT 
    WHERE { 
            ?c a skos:Concept ;
                skos:inScheme <~~uri~~> ;
                ~~item_condition~~
                ?property ?value .
    }
   """