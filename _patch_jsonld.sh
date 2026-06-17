#!/bin/bash
# Add JSON-LD structured data to English page only
JSONLD='<script type="application/ld+json">{"@context":"https://schema.org","@type":"WebSite","name":"The 420 Code","url":"https://the420code.org","description":"42 Artist'\''s Proofs deriving ethics from physics. One measured input. Zero fitted parameters. 258 kill switches. Copyleft.","author":{"@type":"Person","name":"G","affiliation":{"@type":"Organization","name":"Studio G","address":"Strand, Cape Town"}},"inLanguage":["en","es","fr","de","pt","nl","it","zh","ja","ko","ru","ar","hi"],"license":"https://creativecommons.org/licenses/by/4.0/","identifier":{"@type":"PropertyValue","propertyID":"DOI","value":"10.5281/zenodo.19208226"}}</script>'

sed -i "s|</head>|$JSONLD\n</head>|" index.html
echo "JSON-LD added to English page"
