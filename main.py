from flask import Flask, request, jsonify
from dummy import Dummy

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
    return {"response": "success"}


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    app.run()
