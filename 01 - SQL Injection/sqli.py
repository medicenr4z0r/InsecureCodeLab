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
        
        # Vulnerable to SQL injection
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        print("Consulta generada:", query)  # Imprime la consulta completa
        
        try:
            c.execute(query)
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


# Para probar la vulnerabilidad de inyección SQL, puedes seguir estos pasos:
# 1. python3 sqli.py
# 2. curl -X POST http://localhost:5000/login -d "username=razor' OR ''='--"

# Referencias: https://r4z0r.gitbook.io/las-notas-de-r4z0r/web-app-pentest/sql-nosql-injection/sql-injection