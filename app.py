# Importar Flask y jsonify para crear la API y formatear respuestas en JSON
from flask import Flask, jsonify

app = Flask(__name__)

# Definir la ruta que responde a las solicitudes GET en - /personas
@app.route('/personas', methods=['GET'])
def get_personas():
    nombres = [ {'name' :'Juan'}, {'name' :'wilder'}, {'name' :'Luis'}, {'name' :' María '} ]  # Lista estática de nombres
    # Devolver la lista de nombres en formato JSON
    return jsonify(nombres)
# Ejecutar la aplicación en modo de depuración si se llama directamente
if __name__ == '__main__':
    app.run(debug=True)
