from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    # Se obtiene el parámetro "texto" de la URL
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>DOM XSS Lab</title>
        </head>
        <body>
            <h1>DOM XSS Lab</h1>
            <p>Ingresa un mensaje en el parámetro "texto" de la URL.</p>
            <p>Ejemplo: http://127.0.0.1:5000/?texto=test</p>
            <p id="output"></p>

            <script>
                // Vulnerable a DOM XSS
                var params = new URLSearchParams(window.location.search);
                var texto = params.get('texto');
                document.getElementById('output').innerHTML = texto;
            </script>
        </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
    
    
'''
Algunas funciones JavaScript vulnerables a DOM XSS:
innerHTML
outerHTML
document.write()
document.writeln()
insertAdjacentHTML()
eval()
location.href
location.assign()
location.replace()
window.location
window.location.search
window.name
postMessage() (si el contenido no está validado y sanitizado)
'''

# Referencias: https://r4z0r.gitbook.io/las-notas-de-r4z0r/web-app-pentest/cross-site-scripting-xss
