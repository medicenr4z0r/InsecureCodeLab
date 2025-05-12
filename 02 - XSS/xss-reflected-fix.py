from flask import Flask, request, render_template_string
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    # usamos escape para evitar XSS
    name = escape(request.args.get('name', '"><img src=z onerror=prompt(3)>')) 
    
    return render_template_string('<h1>Hola, {}!</h1>'.format(name))

if __name__ == '__main__':
    app.run(debug=True)