from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.oqxmexp.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def index():
    return render_template('place_index.html')

####장소추천 - 서울
@app.route('/place_seoul')
def seoul():
    return render_template('place_seoul.html')

@app.route("/seoulplace", methods=["POST"])
def seoulplace_post():
    url_receive = request.form['url_give']
    name_receive = request.form['name_give']
    address_receive = request.form['address_give']
    star_receive = request.form['star_give']
    comment_receive = request.form['comment_give']

    doc = {
        'url': url_receive,
        'name': name_receive,
        'address': address_receive,
        'star': star_receive,
        'comment': comment_receive
    }
    db.seoulplaces.insert_one(doc)

    return jsonify({'msg': '추천 완료!'})

@app.route("/seoulplace", methods=["GET"])
def seoulplace_get():
    seoulplaces_list = list(db.seoulplaces.find({}, {'_id': False}))
    return jsonify({'seoulplaces': seoulplaces_list })

@app.route("/seouloutplace", methods=["POST"])
def seouloutplace_post():
    outurl_receive = request.form['outurl_give']
    outname_receive = request.form['outname_give']
    outaddress_receive = request.form['outaddress_give']
    outstar_receive = request.form['outstar_give']
    outcomment_receive = request.form['outcomment_give']

    doc = {
        'out_url': outurl_receive,
        'out_name': outname_receive,
        'out_address': outaddress_receive,
        'out_star': outstar_receive,
        'out_comment': outcomment_receive
    }
    db.seouloutplaces.insert_one(doc)

    return jsonify({'msg': '추천 완료!'})

@app.route("/seouloutplace", methods=["GET"])
def seouloutplace_get():
    seouloutplaces_list = list(db.seouloutplaces.find({}, {'_id': False}))
    return jsonify({'seouloutplaces': seouloutplaces_list })

####장소추천 - 인천
@app.route('/place_incheon')
def incheon():
    return render_template('place_incheon.html')

@app.route("/incheonplace", methods=["POST"])
def incheonplace_post():
    url_receive = request.form['url_give']
    name_receive = request.form['name_give']
    address_receive = request.form['address_give']
    star_receive = request.form['star_give']
    comment_receive = request.form['comment_give']

    doc = {
        'url': url_receive,
        'name': name_receive,
        'address': address_receive,
        'star': star_receive,
        'comment': comment_receive
    }
    db.incheonplaces.insert_one(doc)

    return jsonify({'msg': '추천 완료!'})

@app.route("/incheonplace", methods=["GET"])
def incheonplace_get():
    incheonplaces_list = list(db.incheonplaces.find({}, {'_id': False}))
    return jsonify({'incheonplaces': incheonplaces_list })

@app.route("/incheonoutplace", methods=["POST"])
def incheonoutplace_post():
    outurl_receive = request.form['outurl_give']
    outname_receive = request.form['outname_give']
    outaddress_receive = request.form['outaddress_give']
    outstar_receive = request.form['outstar_give']
    outcomment_receive = request.form['outcomment_give']

    doc = {
        'out_url': outurl_receive,
        'out_name': outname_receive,
        'out_address': outaddress_receive,
        'out_star': outstar_receive,
        'out_comment': outcomment_receive
    }
    db.incheonoutplaces.insert_one(doc)

    return jsonify({'msg': '추천 완료!'})

@app.route("/incheonoutplace", methods=["GET"])
def incheonoutplace_get():
    incheonoutplaces_list = list(db.incheonoutplaces.find({}, {'_id': False}))
    return jsonify({'incheonoutplaces': incheonoutplaces_list })


####장소추천 - 화성
@app.route('/place_hwaseong')
def hwaseong():
    return render_template('place_hwaseong.html')

@app.route("/hwaseongplace", methods=["POST"])
def hwaseongplace_post():
    url_receive = request.form['url_give']
    name_receive = request.form['name_give']
    address_receive = request.form['address_give']
    star_receive = request.form['star_give']
    comment_receive = request.form['comment_give']

    doc = {
        'url': url_receive,
        'name': name_receive,
        'address': address_receive,
        'star': star_receive,
        'comment': comment_receive
    }
    db.hwaseongplaces.insert_one(doc)

    return jsonify({'msg': '추천 완료!'})

@app.route("/hwaseongplace", methods=["GET"])
def hwaseongplace_get():
    hwaseongplaces_list = list(db.hwaseongplaces.find({}, {'_id': False}))
    return jsonify({'hwaseongplaces': hwaseongplaces_list })

@app.route("/hwaseongoutplace", methods=["POST"])
def hwaseongoutplace_post():
    outurl_receive = request.form['outurl_give']
    outname_receive = request.form['outname_give']
    outaddress_receive = request.form['outaddress_give']
    outstar_receive = request.form['outstar_give']
    outcomment_receive = request.form['outcomment_give']

    doc = {
        'out_url': outurl_receive,
        'out_name': outname_receive,
        'out_address': outaddress_receive,
        'out_star': outstar_receive,
        'out_comment': outcomment_receive
    }
    db.hwaseongoutplaces.insert_one(doc)

    return jsonify({'msg': '추천 완료!'})

@app.route("/hwaseongoutplace", methods=["GET"])
def hwaseongoutplace_get():
    hwaseongoutplaces_list = list(db.hwaseongoutplaces.find({}, {'_id': False}))
    return jsonify({'hwaseongoutplaces': hwaseongoutplaces_list })


####장소추천 - 수원
@app.route('/place_suwon')
def suwon():
    return render_template('place_suwon.html')

@app.route("/suwonplace", methods=["POST"])
def suwonplace_post():
    url_receive = request.form['url_give']
    name_receive = request.form['name_give']
    address_receive = request.form['address_give']
    star_receive = request.form['star_give']
    comment_receive = request.form['comment_give']

    doc = {
        'url': url_receive,
        'name': name_receive,
        'address': address_receive,
        'star': star_receive,
        'comment': comment_receive
    }
    db.suwonplaces.insert_one(doc)

    return jsonify({'msg': '추천 완료!'})

@app.route("/suwonplace", methods=["GET"])
def suwonplace_get():
    suwonplaces_list = list(db.suwonplaces.find({}, {'_id': False}))
    return jsonify({'suwonplaces': suwonplaces_list })

@app.route("/suwonoutplace", methods=["POST"])
def suwonoutplace_post():
    outurl_receive = request.form['outurl_give']
    outname_receive = request.form['outname_give']
    outaddress_receive = request.form['outaddress_give']
    outstar_receive = request.form['outstar_give']
    outcomment_receive = request.form['outcomment_give']

    doc = {
        'out_url': outurl_receive,
        'out_name': outname_receive,
        'out_address': outaddress_receive,
        'out_star': outstar_receive,
        'out_comment': outcomment_receive
    }
    db.suwonoutplaces.insert_one(doc)

    return jsonify({'msg': '추천 완료!'})

@app.route("/suwonoutplace", methods=["GET"])
def suwonoutplace_get():
    suwonoutplaces_list = list(db.suwonoutplaces.find({}, {'_id': False}))
    return jsonify({'suwonoutplaces': suwonoutplaces_list })

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)