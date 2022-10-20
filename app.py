from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.q15z7ue.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    nickname_receive = request.form['nickname_give']
    comment_receive = request.form['comment_give']

    doc = {
        'nickname': nickname_receive,
        'comment': comment_receive
    }

    db.fanList.insert_one(doc)

    return jsonify({'msg':'응원 등록 완료!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    fan_list = list(db.fanList.find({}, {'_id': False}))
    return jsonify({'fan_list': fan_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)