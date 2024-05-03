import os
from flask import Flask, render_template, request, jsonify, redirect, session, g
import sqlite3
import bcrypt

app = Flask(__name__, static_url_path='/static')
app.secret_key = os.urandom(24)

app.config['DATABASE'] = os.path.join(os.getcwd(), 'user_database.db')

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(app.config['DATABASE'])
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def register():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register_user():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'message': 'Invalid request. Missing username or password.'}), 400

        db = get_db()
        cursor = db.cursor()

        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            return jsonify({'message': 'Username already exists. Please choose a different username.'}), 400

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        db.commit()

        return jsonify({'message': 'User registered successfully!'})

    except Exception as e:
        print(f"An error occurred during registration: {e}")
        return jsonify({'message': 'An error occurred. Please try again.'}), 500

@app.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'GET':
        return render_template('login.html')

    elif request.method == 'POST':
        try:
            data = request.get_json()
            username = data.get('username')
            password = data.get('password')

            if not username or not password:
                return jsonify({'message': 'Invalid request. Missing username or password.'}), 400

            db = get_db()
            cursor = db.cursor()

            cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
            stored_password = cursor.fetchone()

            if stored_password:
                if bcrypt.checkpw(password.encode('utf-8'), stored_password[0]):
                    session['username'] = username
                    return jsonify({'success': True, 'message': 'Login successful!'})
                else:
                    return jsonify({'success': False, 'message': 'Invalid username or password.'}), 401
            else:
                return jsonify({'success': False, 'message': 'Invalid username or password.'}), 401

        except Exception as e:
            print(f"An error occurred during login: {e}")
            return jsonify({'success': False, 'message': 'An error occurred. Please try again.'}), 500

@app.route('/user-data', methods=['GET'])
def get_user_data():
    if 'username' in session:
        try:
            username = session['username']
            return jsonify({'username': username})
        except Exception as e:
            print(f"An error occurred while fetching user data: {e}")
            return jsonify({'message': 'An error occurred. Please try again.'}), 500
    else:
        return jsonify({'message': 'User not authenticated'}), 401

@app.route('/user')
def user_page():
    if 'username' in session:
        return render_template('user.html', username=session['username'])
    else:
        return redirect('/login')

@app.route('/logout', methods=['POST'])
def logout_user():
    try:
        session.clear()
        return jsonify({'success': True, 'message': 'Logout successful.'})

    except Exception as e:
        print(f"An error occurred during logout: {e}")
        return jsonify({'success': False, 'message': 'An error occurred during logout.'}), 500

@app.route('/register', methods=['GET'])
def register_page():
    return render_template('register.html')

if __name__ == "__main__":
    app.run(debug=True)