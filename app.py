from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Example data for cars
cars = [
    {"id": 1, "model": "Toyota Supra", "year": 2021},
    {"id": 2, "model": "Omni", "year": 2022},
    {"id": 3, "model": "Ford Mustang", "year": 2020}
]

# To keep track of bookings
bookings = []

@app.route('/')
def index():
    return render_template('index.html', cars=cars)

@app.route('/rent', methods=['POST'])
def rent():
    car_id = int(request.form['car_id'])
    name = request.form['name']
    email = request.form['email']
    car = next((car for car in cars if car['id'] == car_id), None)
    if car:
        bookings.append({'car_id': car_id, 'name': name, 'email': email})
        return render_template('confirmation.html', car=car, name=name, email=email)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
