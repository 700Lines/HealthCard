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


@app.route('/add/medicine', methods=['POST'])
def add_medicine():
    _json = request.json
    _name = _json['medicine name']
    _group = _json['medicine group']
    _company_name = _json['company name']

    if _name and _group and _company_name and request.method == "POST":
        mongo.db.medicine.insert({'medicine name': _name, 'medicine group': _group, 'company name': _company_name})

        resp = jsonify("Medicine added successfully")

        resp.status_code = 200
        return resp
    else:
        return not_found()


@app.route('/medicines')
def medicines():
    medicines = mongo.db.medicine.find()
    resp = dumps(medicines)

    return  resp


@app.route('/medicine/<id>')
def medicine(id):
    medicine = mongo.db.medicine.find_one({'_id': ObjectId(id)})
    resp = dumps(medicine)

    return resp


@app.route('/delete/medicine/<id>', methods=['DELETE'])
def delete_medicine(id):
    mongo.db.medicine.delete_one({'_id': ObjectId(id)})
    resp = jsonify("Medicine deleted successfully")

    return resp


@app.route('/update/medicine/<id>', methods=['PUT'])
def update_medicine(id):
    _id = id
    _json = request.json
    _name = _json['medicine name']
    _group = _json['medicine group']
    _company_name = _json['company name']

    if _name and _group and _company_name and request.method == "PUT":

        mongo.db.medicine.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)} ,{'$set' : {'medicine name' : _name, 'medicine group': _group, 'company name': _company_name}})
        resp = jsonify("Medicine updated sucessfully")

        return resp

    else:
        return not_found()




if __name__ == "__main__":
    app.run(debug=True)