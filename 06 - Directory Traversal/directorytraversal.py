from flask import Flask, request, send_file
import os

app = Flask(__name__)

BASE_DIR = "./files"

@app.route('/download', methods=['GET'])
def download_file():
    filename = request.args.get('file')
    # No se realiza ninguna validación sobre el contenido de 'filename'
    try:
        return send_file(f'./files/{filename}')
    except FileNotFoundError:
        return "<h2>Archivo no encontrado</h2>"
    except Exception as e:
        return f"<h2>Error: {e}</h2>"

if __name__ == '__main__':
    os.makedirs(BASE_DIR, exist_ok=True)
    # Crear archivos de ejemplo
    with open(os.path.join(BASE_DIR, 'file1.txt'), 'w') as f:
        f.write("Contenido del archivo 1")
    with open(os.path.join(BASE_DIR, 'file2.txt'), 'w') as f:
        f.write("Contenido del archivo 2")
    app.run(debug=True)


# En este caso, la vulnerabilidad es un Directory Traversal, ya que el usuario puede manipular el parámetro 'file' para acceder a archivos fuera del directorio permitido.
# Si ejecutamos: http://127.0.0.1:5000/download?file=../../../../../../etc/passwd, nos descargaremos el archivo /etc/passwd ya que no se está validando lo que el usuario ingresa

# Referencias: https://r4z0r.gitbook.io/las-notas-de-r4z0r/web-app-pentest/directory-traversal-path-traversal