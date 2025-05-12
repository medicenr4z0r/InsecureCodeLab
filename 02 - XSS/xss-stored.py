import sqlite3
from flask import Flask, request, render_template_string, redirect

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS comments (id INTEGER PRIMARY KEY, content TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('SELECT content FROM comments')
    comments = c.fetchall()
    conn.close()

    comment_section = ''.join([f"<p>{comment[0]}</p>" for comment in comments])

    return render_template_string('''
        <h1>Deja un comentario</h1>
        <form method="POST" action="/add_comment">
            <input type="text" name="content" placeholder="Escribe tu comentario">
            <button type="submit">Enviar</button>
        </form>
        <h2>Comentarios:</h2>
        {}
    '''.format(comment_section))

@app.route('/add_comment', methods=['POST'])
def add_comment():
    content = request.form.get('content')

    # Vulnerabilidad de XSS Stored: No se sanitiza el contenido antes de guardarlo
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('INSERT INTO comments (content) VALUES (?)', (content,))
    conn.commit()
    conn.close()

    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
