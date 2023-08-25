from flask import Flask,request,jsonify
animes = {
    1: {
        'titulo': 'Gintama:THE FINAL',
        'categoria': 'ACTION,COMEDY,DRAMA,SCI-FI ',
        'rating': 91,
        'season': 'wINTER 2021',
        'review': 'the perfect ending to the greatest story ever told',
        'tipo': 'MOVIE ',
        'imagen':'xd'
    },
    2: {
        'titulo': 'fRUITS BASKET:THE FINAL',
        'categoria': 'COMEDY,DRAMA,PYSCHOLOGICAL,ROMANCE,SLICE OF LIFE',
        'rating': 90,
        'season': 'PRIMAVERA 2021',
        'review': 'After last season’s revelations, the Soma family moves forward, but the emotional chains that bind them are not easily broken. Unable to admit why she wants the cure, Tohru wrestles with the truth, aware that time is running out for someone close.',
        'tipo': 'TV',
        'imagen':''
    },
    3: {
        'titulo': '3-gatsu no Lion 2',
        'categoria': 'ACTION,ADVENTURE,FANTASY',
        'rating': 89,
        'season': 'FINALIZADA 2017',
        'review': 'Una descripción detallada del Anime 3...',
        'tipo': 'TV SHOW',
        'imagen':''
    }
}

app = Flask(__name__)

# Obtener todos los animes
@app.route('/animes', methods=['GET'])
def get_animes():
    return jsonify(animes)

# Obtener un anime por ID
@app.route('/animes/<int:id>', methods=['GET'])
def get_anime(id):
    if id in animes:
        return jsonify(animes[id])
    else:
        return jsonify({'ALERTA': 'ANIME NO ENCONTRADO'})

# Crear un nuevo anime
@app.route('/animes', methods=['POST'])
def create_anime():
    new_anime = request.json
    id = max(animes.keys()) + 1
    animes[id] = new_anime
    return jsonify({'message': 'Anime creado exitosamente', 'id': id}), 201

# Actualizar un anime por ID (PUT)
@app.route('/animes/<int:id>', methods=['PUT'])
def update_anime(id):
    if id in animes:
        animes[id] = request.json
        return jsonify({'message': 'Anime actualizado exitosamente'})
    else:
        return jsonify({'ALERTA': 'ANIME NO ENCONTRADO'})

# Actualizar propiedades específicas de un anime por ID (PATCH)
@app.route('/animes/<int:id>', methods=['PATCH'])
def partial_update_anime(id):
    if id in animes:
        anime = animes[id]
        anime.update(request.json)
        return jsonify({'message': 'Actualización parcial exitosa'})
    else:
        return jsonify({'ALERTA': 'ANIME NO ENCONTRADO'})

# Eliminar un anime por ID
@app.route('/animes/<int:id>', methods=['DELETE'])
def delete_anime(id):
    if id in animes:
        del animes[id]
        return jsonify({'message': 'Anime eliminado exitosamente'})
    else:
        return jsonify({'ALERTA': 'ANIME NO ENCONTRADO'})
if __name__ == '__main__':
    app.run(debug=True, port=5001)
