import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/ejecutar', methods=['GET', 'POST'])
def execute():
    if request.method == 'GET':
        return '''
            <div style="display: flex; justify-content: center; align-items: center; height: 100vh; font-family: Arial, sans-serif;">
                <div style="text-align: center;">
                    <h2>RCE Lab</h2>
                    <form method="POST">
                        <div>
                            <label>Comando:</label><br>
                            <input type="text" name="command" placeholder="whoami" style="margin-bottom: 10px; width: 300px;"><br>
                        </div>
                        <input type="submit" value="Ejecutar" style="padding: 5px 10px;">
                    </form>
                </div>
            </div>
        '''

    if request.method == 'POST':
        try:
            command = request.form.get('command')
            result = subprocess.check_output(command, shell=True).decode()
            return f"<pre>{result}</pre>"
        except Exception as e:
            return f"Error ejecutando el comando: {e}"

if __name__ == '__main__':
    app.run(debug=True)