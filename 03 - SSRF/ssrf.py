import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/fetch', methods=['GET', 'POST'])
def fetch():
    if request.method == 'GET':
        return '''
            <div style="display: flex; justify-content: center; align-items: center; height: 100vh; font-family: Arial, sans-serif;">
                <div style="text-align: center;">
                    <h2>SSRF Lab</h2>
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
        try:
            response = requests.get(url) # Sin ningún tipo de validación, vulnerable a SSRF
            return response.text
        except Exception as e:
            return f"Error obteniendo una URL: {e}"

if __name__ == '__main__':
    app.run(debug=True)
    
# Visitar: http://127.0.0.1:5000/fetch y meter una url, la petición se hará internamente desde el servidor víctima.

# Referencias: https://r4z0r.gitbook.io/las-notas-de-r4z0r/web-app-pentest/server-side-request-forgery-ssrf