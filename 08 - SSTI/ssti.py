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
        # Vulnerable a SSTI
        template = f"Hola, {name}!"
        return render_template_string(template)

if __name__ == '__main__':
    app.run(debug=True)
    
# Intenta con: curl -X POST -d "name={{ config }}" http://127.0.0.1:5000/saludar