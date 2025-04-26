from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_principal import Principal, Permission, RoleNeed, identity_loaded, Identity, AnonymousIdentity, identity_changed
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'clave_secreta'

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Flask-Principal setup
principals = Principal(app)

# Definir roles
admin_permission = Permission(RoleNeed('admin'))
user_permission = Permission(RoleNeed('user'))

# Usuarios de ejemplo
users = {
    'admin': {'password': generate_password_hash('admin123'), 'role': 'admin'},
    'user': {'password': generate_password_hash('user123'), 'role': 'user'}
}

class User(UserMixin):
    def __init__(self, username, role):
        self.id = username
        self.role = role

@login_manager.user_loader
def load_user(user_id):
    user = users.get(user_id)
    if user:
        return User(user_id, user['role'])
    return None

@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    if hasattr(current_user, 'role'):
        identity.provides.add(RoleNeed(current_user.role))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        if user and check_password_hash(user['password'], password):
            user_obj = User(username, user['role'])
            login_user(user_obj)
            identity_changed.send(app, identity=Identity(user_obj.id))
            return redirect(url_for('dashboard'))
        return 'Credenciales inválidas', 401
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    identity_changed.send(app, identity=AnonymousIdentity())
    return redirect(url_for('home'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.id, role=current_user.role)

@app.route('/admin')
@login_required
@admin_permission.require(http_exception=403)
def admin_panel():
    return "<h1>Área de administrador</h1>"

@app.route('/user')
@login_required
@user_permission.require(http_exception=403)
def user_panel():
    return "<h1>Área de usuario</h1>"

if __name__ == '__main__':
    app.run(debug=True)
