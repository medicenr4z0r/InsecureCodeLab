import requests
from flask import Flask, request, abort
from urllib.parse import urlparse

app = Flask(__name__)

# Lista blanca de dominios permitidos
ALLOWED_DOMAINS = ["r4z0r.gitbook.io", "juankaenel.com"]

def is_url_allowed(url):
    try:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        return any(domain.endswith(allowed) for allowed in ALLOWED_DOMAINS)
    except Exception:
        return False

@app.route('/fetch', methods=['GET', 'POST'])
def fetch():
    if request.method == 'GET':
        # Mostrar el formulario
        return '''
            <div style="display: flex; justify-content: center; align-items: center; height: 100vh; font-family: Arial, sans-serif;">
                <div style="text-align: center;">
                    <h2>SSRF Lab - Fix</h2>
                    <form method="POST">
                        <div>
                            <label>URL:</label><br>
                            <input type="text" name="url" style="margin-bottom: 10px; width: 300px;"><br>
                        </div>
                        <input type="submit" value="Fetch" style="padding: 5px 10px;">
                    </form>
                </div>
            </div>
        '''

    if request.method == 'POST':
        url = request.form.get('url')

        if not is_url_allowed(url):
            abort(403, "URL no permitida")

        try:
            response = requests.get(url, timeout=5)
            return response.text
        except Exception as e:
            return f"Error obteniendo URL: {e}"

if __name__ == '__main__':
    app.run(debug=True)
