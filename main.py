from flask import Flask, request, jsonify
from dummy import Dummy
from typing import List
from object_model import ObjectModel
from error_handler import AppError

app = Flask(__name__)
# app.config["DEBUG"] = True

@app.route('/data/list', methods=['GET'])
def getData():
    dataList = Dummy().dummyList()
    dataList_json = []
    for row in dataList:
        dataList_json.append(row.__dict__)

    print(dataList_json)
    return jsonify(dataList_json)

@app.route('/data/insert', methods=['POST'])
def insertData():
    print(request.json)

    if "name" not in request.json:
        return AppError().bad_request()
    if "age" not in request.json:
        return AppError().bad_request()
    if "gender" not in request.json:
        return AppError().bad_request()

    name = request.json['name']
    age = request.json['age']
    gender = request.json['gender']

    return {
        "status": "success",
        "response": {
            "name": name,
            "age": age,
            "gender": gender
        }
    }

@app.route('/data/<id>/update', methods=['PATCH'])
def updateData(id):
    print(request.json)
    dummies: List[ObjectModel] = Dummy().dummyList()

    # set default object
    result: ObjectModel = ObjectModel(0, "", 0, "")

    for row in dummies:
        if row.id == int(id):
            result = row

    # # # IF RECEIVE WRONG ID
    if result.id is 0:
        print("ID does not match")
        return AppError().not_found()

    if "name" in request.json:
        result.name = request.json['name']

    if "age" in request.json:
        result.age = request.json['age']

    if "gender" in request.json:
        result.gender = request.json['gender']

    return result.__dict__


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    app.run()
