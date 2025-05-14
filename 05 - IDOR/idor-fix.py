from flask import Flask

app = Flask(__name__)

users = {
    '1': {'username': 'R4z0r', 'email': 'razor@codigovulnerable.xyz', 'dni': '30.000.000', 'phone': '3712112233', 'address': 'Calle Falsa 123, Buenos Aires'},
    '2': {'username': 'Uzumaki Naruto', 'email': 'naruto@codigovulnerable.xyz', 'dni': '30.000.001', 'phone': '3712112234', 'address': 'Avenida Siempreviva 742, Buenos Aires'},
    '3': {'username': 'Rock Lee', 'email': 'rocklee@codigovulnerable.xyz', 'dni': '30.000.002', 'phone': '3712112235', 'address': 'Calle Los Álamos 456, Buenos Aires'},
    '4': {'username': 'Gaara de la Arena', 'email': 'gaara@codigovulnerable.xyz', 'dni': '30.000.003', 'phone': '3712112236', 'address': 'Pasaje del Sol 789, Buenos Aires'},
    '5': {'username': 'Uchiha Sasuke', 'email': 'sasuke@codigovulnerable.xyz', 'dni': '30.000.004', 'phone': '3712112237', 'address': 'Boulevard de los Sueños Rotos 101, Buenos Aires'}
}

@app.route('/users/<user_id>', methods=['GET'])
def profile(user_id):
    # Simulación del usuario autenticado (en un caso real, se obtendría de la cookie de sesión o token.
    current_user_id = '1'  # Usuario autenticado: R4z0r
    
    if user_id == current_user_id:
        user_data = users[user_id]
        return f"<h2>Perfil de {user_data['username']}</h2><p>Email: {user_data['email']}<br>DNI: {user_data['dni']}<br>Teléfono: {user_data['phone']}<br>Dirección: {user_data['address']} <h4>Estás autenticado como *R4z0r*</h4></p>"
    else:
        return "<h2>Acceso denegado. No tienes permiso para ver este perfil.</h2>"

if __name__ == '__main__':
    app.run(debug=True)