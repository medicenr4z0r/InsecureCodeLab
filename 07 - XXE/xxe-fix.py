from flask import Flask, request
from lxml import etree

app = Flask(__name__)

@app.route('/xml', methods=['POST'])
def xml_parser():
    try:
        xml_data = request.data.decode()
        # Si no se resuelven entidades externas, no se puede hacer XXE, a menos que se pueda utilizar XInclude, cosa que acá no está habilitada
        parser = etree.XMLParser(resolve_entities=False)
        root = etree.fromstring(xml_data, parser)
        response = f"<h2>Root tag: {root.tag}</h2>"
        return response
    except etree.XMLSyntaxError as e:
        return f"Error al procesar XML: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
