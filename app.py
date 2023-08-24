from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route("/anime",methods=['GET','POST'])
def anime():
    if request.method  == 'GET':
        return jsonify({'anime': 'HunterxHunter'})
    elif request.method == 'POST':
        req_json = request.json
        name = req_json['name']
        req_json2 = request.json
        categoria = req_json2['categoria']
        req_json3 = request.json
        rating = req_json3['rating']
        req_json4 = request.json
        review = req_json4['review']
        req_json5 = request.json
        season = req_json5['season']
        req_json6 = request.json
        tipo = req_json6['tipo']
        return jsonify({'name': name,'categoria': categoria,'rating': rating,'review': review,'season': season,'tipo': tipo    
})
    @app.route("/anime/3350",methods=['GET'])
    def animeid():
        if request.method  == 'GET':
            return jsonify({'anime': 'HunterxHunter',"categoria":"Action","Rating":"89%","review":"A mastrepiece","season":"fall 2011","tipo":"TV Show"})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
