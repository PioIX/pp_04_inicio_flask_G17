from flask import Flask
from datetime import date
import random

app = Flask(__name__)

@app.route('/dado')
def dado_random():
  x = random.randint(1, 6)
  return str(x)

@app.route("/dado/<n>")
def dado_random_con_n(n):
    z = []
    if int(n) > 0 and int(n) < 11:
      for i in range(3):
        x = random.randint(1, 6)
        z.append(x)
      return str(z)

@app.route("/fecha")
def fecha_random():
  inicio = date(1970, 1, 1)
  final =  date(2100, 12, 31)
  
  random_date = inicio + (final - inicio) * random.random()
  
  return str(random_date)

@app.route("/fecha/<y>")
def fecha_random2(y):
  inicio = date(int(y), 1, 1)
  final  = date(int(y), 12, 31)
  
  random_date = inicio + (final - inicio) * random.random()
  
  return str(random_date)

@app.route("/fecha/<y>/<m>")
def fecha_random3(y, m):
  inicio = date(int(y), int(m), 1)
  final =  date(int(y), int(m), 31)
  
  random_date = inicio + (final - inicio) * random.random()
  
  return str(random_date)

@app.route("/color")
def color_random():  
  Hexadecimal = ["#"+''.join([random.choice('ABCDEF0123456789')for i in range(6)])]
  color = str(Hexadecimal[0])
  return f'<h1 style="color:{color};">COLOR</h1>'

app.run(host='0.0.0.0', port=81)
