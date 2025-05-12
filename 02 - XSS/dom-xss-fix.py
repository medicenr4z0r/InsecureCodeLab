from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    # Se obtiene el parámetro "texto" de la URL
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>DOM XSS Example</title>
        </head>
        <body>
            <h1>DOM XSS Example</h1>
            <p>Ingresa un mensaje en el parámetro "texto" de la URL.</p>
            <p>Ejemplo: http://127.0.0.1:5000/?texto=test</p>
            <p id="output"></p>

            <script>
                var params = new URLSearchParams(window.location.search);
                var texto = params.get('texto');
                // usamos textContent en lugar de innerHTML para evitar XSS
                document.getElementById('output').textContent = texto;
            </script>
        </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)