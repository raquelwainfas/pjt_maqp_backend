from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///animais.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.String(8), nullable=False)
    sex = db.Column(db.String(10), nullable=False)
    size = db.Column(db.String(20), nullable=False)
    personality = db.Column(db.String(200), nullable=True)
    image_url = db.Column(db.String(200), nullable=True)

@app.route('/')
def index():
    return "Serviço On Line."

@app.route('/animais', methods=['POST'])
def create_animal():
    data = request.get_json()
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    image_url = response.json().get('message')
    new_animal = Animal(
        name=data['name'],
        age=data['age'],
        sex=data['sex'],
        size=data['size'],
        personality=data.get('personality'),
        image_url=image_url
    )
    db.session.add(new_animal)
    db.session.commit()
    return jsonify({'message': 'Animal created successfully'}), 201

@app.route('/animais/<int:animal_id>', methods=['GET'])
def get_animal(animal_id):
    animal = Animal.query.get_or_404(animal_id)
    return jsonify({
        'id': animal.id,
        'name': animal.name,
        'age': animal.age,
        'sex': animal.sex,
        'size': animal.size,
        'personality': animal.personality,
        'image_url': animal.image_url
    })

@app.route('/animais', methods=['GET'])
def get_animals():
    animais = Animal.query.all()
    animais_list = [{
        'id': animal.id,
        'name': animal.name,
        'age': animal.age,
        'sex': animal.sex,
        'size': animal.size,
        'personality': animal.personality,
        'image_url': animal.image_url
    } for animal in animais]
    return jsonify(animais_list)

@app.route('/animais/<int:animal_id>', methods=['PUT'])
def update_animal(animal_id):
    data = request.get_json()
    animal = Animal.query.get_or_404(animal_id)
    animal.name = data['name']
    animal.age = data['age']
    animal.sex = data['sex']
    animal.size = data['size']
    animal.personality = data.get('personality', animal.personality)
    db.session.commit()
    return jsonify({'message': 'Animal updated successfully'})

@app.route('/animais/<int:animal_id>', methods=['DELETE'])
def delete_animal(animal_id):
    animal = Animal.query.get_or_404(animal_id)
    db.session.delete(animal)
    db.session.commit()
    return jsonify({'message': 'Animal deleted successfully'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
