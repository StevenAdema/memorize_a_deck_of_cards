from flask import Flask, render_template, request, url_for, flash
from werkzeug.utils import redirect
from flask_mysqldb import MySQL
import pandas as pd

app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'deck_mem'

mysql = MySQL(app)

# cur = mysql.connection.cursor()
# cur.execute("SELECT * FROM card_system")
df = pd.read_csv('./data/pao.csv', sep=',')
# df = pd.DataFrame(cur.fetchall())
df = df.sample(frac=1).reset_index(drop=True) 
print(df)
index = df.index.values.tolist()
first = [0,3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51]
second = [1,4,7,10,13,16,19,22,25,28,31,34,37,40,43,46,49,52]
images = df['ImgLink']
per = df['Person']
act = df['Action']
obj = df['Object']