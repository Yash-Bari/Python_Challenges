from flask import Flask, render_template, request

app = Flask(__name__)

# Sample data to store user submissions
user_data = []

@app.route('/')
def index():
    return render_template('index.html', users=user_data)

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        email = request.form['email']
        phone = request.form['phone']
        skills = request.form['skills']

        # Process the submitted data
        user_entry = {
            'name': name,
            'address': address,
            'email': email,
            'phone': phone,
            'skills': skills
        }
        user_data.append(user_entry)

    return render_template('add_user.html')

if __name__ == '__main__':
    app.run(debug=True)
