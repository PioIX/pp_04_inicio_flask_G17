import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/listado")
def listado_per_capita():
  conn = sqlite3.connect('co_emissions.db')

  q = f"""SELECT Country FROM emissions 
          WHERE Series = 'pcap' 
          ORDER BY Value DESC 
          LIMIT 10"""
  x = conn.execute(q)
  return render_template('lista_per_capita.html', lineamostrar = x)
  conn.close()

@app.route("/listado/top")
def listado_total():
  conn = sqlite3.connect('co_emissions.db')

  q = f"""SELECT Country FROM emissions 
          WHERE Series = 'total' 
          ORDER BY Value DESC 
          LIMIT 10"""
  x = conn.execute(q)
  return render_template('lista_total.html', lineamostrar = x)
  conn.close()

@app.route("/listado/argentina")
def listado_arg():
  conn = sqlite3.connect('co_emissions.db')

  q = f"""SELECT * FROM emissions 
          WHERE Country = 'Argentina'
          ORDER BY Year ASC"""
  x = conn.execute(q)
  return render_template('listadoArgentina.html', lineamostrar2 = x)
  conn.close()

@app.route("/ayuda")
def ayuda():
  return render_template('ayuda.html');


@app.route("/")
def home():
  return render_template('index.html');

app.run(host='0.0.0.0', port=81)
