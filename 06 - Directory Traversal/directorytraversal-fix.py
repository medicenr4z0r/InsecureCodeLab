from flask import Flask, request, send_file
import os

app = Flask(__name__)

BASE_DIR = "./files"

@app.route('/download', methods=['GET'])
def download_file():
    filename = request.args.get('file')
    try:
        file_path = os.path.abspath(os.path.join(BASE_DIR, os.path.normpath(filename)))
        # Validar que el archivo esté dentro del directorio permitido y no permitir caracteres maliciosos para Path Traversal
        if not file_path.startswith(os.path.abspath(BASE_DIR)) or filename.startswith('/') or '//' in filename or '\\' in filename or '%' in filename or '..' in os.path.normpath(filename):
            return "<h2>Acceso denegado. Ruta no permitida.</h2>"
        return send_file(file_path)
    except FileNotFoundError:
        return "<h2>Archivo no encontrado, prueba con file1.txt</h2>"
    except Exception as e:
        return f"<h2>Error: {e}</h2>"

if __name__ == '__main__':
    os.makedirs(BASE_DIR, exist_ok=True)
    with open(os.path.join(BASE_DIR, 'file1.txt'), 'w') as f:
        f.write("Contenido del archivo 1")
    with open(os.path.join(BASE_DIR, 'file2.txt'), 'w') as f:
        f.write("Contenido del archivo 2")
    app.run(debug=True)

