import sqlite3
from flask import Flask, request

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
    c.execute("INSERT INTO users (username, password) VALUES ('razor', 'argentinacampeondelmundoperro')")
    conn.commit()
    conn.close()

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        conn = sqlite3.connect('example.db')
        c = conn.cursor()
        
        # Para remediar la vulnerabilidad utilizamos consultas parametrizadas
        fixquery = "SELECT * FROM users WHERE username = ? AND password = ?" # consultas parametrizadas
        print("")
        print("Consulta generada:", fixquery)  
        print("")
        try:
            c.execute(fixquery, (username, password)) # ejecutar la consulta parametrizada
            result = c.fetchone()
            conn.close()
            
            if result:
                return "Login exitoso!"
            else:
                return "Credenciales inválidas"
        except Exception as e:
            print(f"Error: {e}")
            return "Error en la consulta SQL"
    
    # Si es GET, devolvemos un formulario simple para iniciar sesión
    return '''
        <div style="display: flex; justify-content: center; align-items: center; height: 100vh; font-family: Arial, sans-serif;">
            <div style="text-align: center;">
                <h2>SQL Injection Lab</h2>
                <form method="POST">
                    <div>
                        <label>Usuario:</label><br>
                        <input type="text" name="username" style="margin-bottom: 10px;"><br>
                    </div>
                    <div>
                        <label>Contraseña:</label><br>
                        <input type="password" name="password" style="margin-bottom: 10px;"><br>
                    </div>
                    <input type="submit" value="Login" style="padding: 5px 10px;">
                </form>
            </div>
        </div>
    '''
    
if __name__ == '__main__':
    init_db()
    app.run(debug=True)


