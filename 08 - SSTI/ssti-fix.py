from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/saludar', methods=['GET', 'POST'])
def greet():
    if request.method == 'GET':
        return '''
        <h2>Saludar al Usuario</h2>
        <form method="POST">
            <label for="name">Nombre:</label><br>
            <input type="text" name="name"><br><br>
            <input type="submit" value="Saludar">
        </form>
        '''
    
    if request.method == 'POST':
        name = request.form.get('name')
        template = "Hola, {{ name }}!"
        return render_template_string(template, name=name)

if __name__ == '__main__':
    app.run(debug=True)

'''En Jinja2, la sintaxis {{ name }} es un placeholder seguro que representa una variable pasada a la plantilla.
En el código anterior, template = f"Hola, {name}!" permitía que el valor de name se inyectara directamente en la plantilla, lo cual es peligroso, ya que permitía ejecutar código malicioso.
En el código corregido, "Hola, {{ name }}!" es una plantilla segura donde {{ name }} es reemplazado con el valor de name de manera controlada y escapada, evitando así la ejecución de código malicioso.'''

