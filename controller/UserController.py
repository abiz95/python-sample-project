from app import app
from flask import request, jsonify

from constants import HttpStatus, ResponseData
from service.DataService import getData, saveData


@app.route('/all', methods=['GET'])
def emp():
    try:
        if request.method == 'GET':
            data = getData("SELECT * FROM User")
            response = jsonify(data)
            response.status_code = HttpStatus.OK
            return response
        else:
            ResponseData.construct['success'] = False
            ResponseData.construct['error'] = 'Something happened. Please try again!'
            response = jsonify(ResponseData.construct)
            response.status_code = HttpStatus.BAD_REQUEST
            return response
    except Exception as e:
        print(e)
        ResponseData.construct['success'] = False
        ResponseData.construct['error'] = str(e)
        response.status_code = HttpStatus.BAD_REQUEST
        response = jsonify(ResponseData.construct)
        response.status_code = HttpStatus.BAD_REQUEST
        return response


@app.route('/add', methods=['POST'])
def test():
    try:
        json = request.json
        email = json['email']
        password = json['password']
        username = json['username']
        if email and password and username and request.method == 'POST':
            sql = "INSERT INTO user(email, password, username) VALUES( %s, %s, %s)"
            data = (email, password, username)
            response = saveData(sql, data)
            response = jsonify(response)
            response.status_code = HttpStatus.OK
            return response
        else:
            ResponseData.construct['success'] = False
            ResponseData.construct['error'] = 'Something happened. Please try again!'
            response = jsonify(ResponseData.construct)
            response.status_code = HttpStatus.BAD_REQUEST
            return response
    except Exception as e:
        print(e)
        ResponseData.construct['success'] = False
        ResponseData.construct['error'] = str(e)
        response = jsonify(ResponseData.construct)
        response.status_code = HttpStatus.BAD_REQUEST
        return response


@app.route('/update/<int:id>', methods=['PUT'])
def testupdate(id):
    try:
        json = request.json
        email = json['email']
        password = json['password']
        username = json['username']
        if email and password and username and request.method == 'POST':
            sql = "UPDATE user SET email = %s, password = %s, username = %s WHERE username = %s"
            data = (email, password, username, id)
            response = saveData(sql, data)
            response = jsonify(response)
            response.status_code = HttpStatus.OK
            return response
        else:
            ResponseData.construct['success'] = False
            ResponseData.construct['error'] = 'Something happened. Please try again!'
            response = jsonify(ResponseData.construct)
            response.status_code = HttpStatus.BAD_REQUEST
            return response
    except Exception as e:
        print(e)
        ResponseData.construct['success'] = False
        ResponseData.construct['error'] = str(e)
        response = jsonify(ResponseData.construct)
        response.status_code = HttpStatus.BAD_REQUEST
        return response
