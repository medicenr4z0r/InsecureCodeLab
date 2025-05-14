from flask import Flask, request, render_template_string, send_file
import os

app = Flask(__name__)
BASE_DIR = "./templates"

@app.route('/view', methods=['GET'])
def view_file():
    filename = request.args.get('file')
    # Vulnerable a LFI - Permite cargar archivos locales sin validación
    try:
        file_path = os.path.join(BASE_DIR, filename if filename else 'index.html')
        with open(file_path, 'r') as file:
            content = file.read()
        return render_template_string(content)
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
    
# Intenta con http://127.0.0.1:5000/view?file=../../../../../etc/passwd
# Recuerda que al ser LFI, a diferencia de un Path Traversal aquí puedes cargar y ejecutar archivos locales, en un Path Traversal solo puedes leer archivos locales.

# Referencias: https://r4z0r.gitbook.io/las-notas-de-r4z0r/web-app-pentest/local-file-inclusion-lfi