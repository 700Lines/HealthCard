from flask import Flask

from flask_pymongo import PyMongo

from bson.json_util import dumps

from bson.objectid import ObjectId

from flask import jsonify, request

from app import not_found

app = Flask(__name__)

app.secret_key = "secret_key"

app.config['MONGO_URI'] = "mongodb://localhost:27017/Users"

mongo = PyMongo(app)


@app.route('/add/doctor', methods=['POST'])
def add_doctor():
    _json = request.json
    _name = _json['name']
    _hospital_name = _json['hospital name']
    _speciality = _json['speciality']

    if _name and _hospital_name and _speciality and request.method == 'POST':
        mongo.db.doctor.insert({'name': _name, 'hospital name': _hospital_name, 'speciality': _speciality})

        resp = jsonify("Doctor added successfully")

        resp.status_code = 200
        return resp
    else:
        return not_found()


@app.route('/doctors')
def doctors():
    doctors = mongo.db.doctor.find()
    resp = dumps(doctors)
    return resp


@app.route('/doctor/<id>')
def doctor(id):
    doctor = mongo.db.doctor.find_one({'_id': ObjectId(id)})
    resp = dumps(doctor)
    return resp


@app.route('/delete/doctor/<id>', methods=['DELETE'])
def delete_doctor(id):
    mongo.db.doctor.delete_one({'_id': ObjectId(id)})
    resp = jsonify("Doctor deleted successfully")

    resp.status_code = 200

    return resp


@app.route('/update/doctor/<id>', methods=['PUT'])
def update_doctor(id):
    _id = id
    _json = request.json
    _name = _json['name']
    _hospital_name = _json['hospital name']
    _speciality = _json['speciality']

    if _name and _hospital_name and _speciality and request.method == 'PUT':
        mongo.db.doctor.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {
            '$set': {'name': _name, 'hospital name': _hospital_name, 'speciality': _speciality}})
        resp = jsonify("Doctor updated successfully")
        return resp
    else:
        return not_found


if __name__ == "__main__":
    app.run(debug=True)
