from flask import Flask, request, render_template_string, send_file
import os

app = Flask(__name__)
BASE_DIR = "./templates"

@app.route('/view', methods=['GET'])
def view_file():
    filename = request.args.get('file', 'index.html')
    try:
        file_path = os.path.abspath(os.path.join(BASE_DIR, filename))
        # Validamos que el archivo esté dentro del directorio permitido y no permitir caracteres maliciosos para que use Path Traversal
        if not file_path.startswith(os.path.abspath(BASE_DIR)) or '..' in filename or '%' in filename or filename.startswith('/'):
            return "<h2>Acceso denegado. Ruta no permitida.</h2>"

        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "<h2>Archivo no encontrado</h2>"
    except Exception as e:
        return f"<h2>Error: {e}</h2>"

if __name__ == '__main__':
    os.makedirs(BASE_DIR, exist_ok=True)
    # Crear archivos de ejemplo
    with open(os.path.join(BASE_DIR, 'index.html'), 'w') as f:
        f.write("<h2>Inicio</h2><p>Esta es la página de de Inicio.</p>")
    with open(os.path.join(BASE_DIR, 'contact.html'), 'w') as f:
        f.write("<h2>Contacto</h2><p>Esta es la página de Contacto.</p>")
    app.run(debug=True)
