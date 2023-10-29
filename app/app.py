from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_mysqldb import MySQL

app=Flask(__name__)

# Conexion MySQL
#app.config['MYSQL_HOST'] = 'sd-3686659-h00001.ferozo.net'
app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'wi200391_pancho'

app.config['MYSQL_USER'] = 'chopan'
#app.config['MYSQL_PASSWORD'] = 'Pancho2023'
app.config['MYSQL_PASSWORD'] = 'peperoni'

#app.config['MYSQL_DB'] = 'wi200391_wp'

app.config['MYSQL_DB'] = 'data'

conexion = MySQL(app)




@app.before_request # esto sirve para aplicar logica antes de una peticion
def before_request():
    print('antes de la peticion') 

@app.after_request # esto sirve para aplicar logica luego de una peticion
def after_request(response):
    print('despues de la peticion')
    return response


@app.route('/') # URL Raiz
def index():
    # return 'Estoy desarrollando la API'
    cursos = ['php','python','c','java']
    data={ 
        "titulo":"Api Rest en desarrollo",
        "saludo":"Estoy en etapa de desarrollo",
        "cursos":cursos,
        "quantity_cursos":len(cursos)
    } # diccionario con datos
    return render_template('index.html', data=data) # retornamos plantillas

@app.route('/contacto/<nombre>') # URL personalizada con parametros
def contacto(nombre):
    data={
        'titulo':'Contacto',
        'nombre': nombre
    }
    return render_template('contacto.html', data=data)

def query_string(): # vista
    print(request)
    return 'koko' 

@app.route('/db')
def listar_columnas():
    data={}
    try:
        cursor=conexion.connection.cursor()
        sql = "SELECT id, temp, hum, mov, fecha FROM db_ai"
        cursor.execute(sql)
        columnas=cursor.fetchall()
        print(columnas)
        data['mensaje']='Consulta Exitosa'
    except Exception as ex:
        print(ex)
        data['mensaje']='Error...'
    return jsonify(data)

def error_404(error):
    # return render_template('404.html'), 404
    return redirect(url_for('index')) # importamos las librerias redirect & url_for y cada vez que no se encuentra una pagina redireccionamos al usuario a la pestania deseada

    

if __name__=='__main__':
    app.add_url_rule('/query_string', view_func=query_string) # Regla URL
    app.register_error_handler(404, error_404)
    app.run(debug=True, port=5000) # activamos el debugger - Indicamos puerto
    
    