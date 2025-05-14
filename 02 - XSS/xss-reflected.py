from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name', 'mundo') # en mundo meter el payload malicioso
    #name = request.args.get('name', '<script>alert("r4z0r was here")</script>')

    # Vulnerable a XSS
    return render_template_string('<h1>Hola, {}!</h1>'.format(name))

if __name__ == '__main__':
    app.run(debug=True)
    
# Referencias: https://r4z0r.gitbook.io/las-notas-de-r4z0r/web-app-pentest/cross-site-scripting-xss