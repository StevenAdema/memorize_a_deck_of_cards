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

@app.route('/index')
@app.route('/')
def Index():
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

    return render_template('index.html', data=zip(images,per,act,obj,index), first=first, second=second)

@app.route('/memory_palace')
def memory_palace():
    # cur = mysql.connection.cursor()
    # cur.execute("SELECT * FROM card_system")
    df = pd.read_csv('./data/pao.csv', sep=',')
    # df = pd.DataFrame(cur.fetchall())
    df = df.sample(frac=1).reset_index(drop=True) 
    images = df['ImgLink']
    per = df['Person']
    act = df['Action']
    obj = df['Object']

    return render_template('memory_palace.html', data=zip(images,per,act,obj))

@app.route('/deck_memorization')
def deck_memorization():
    # cur = mysql.connection.cursor()
    # cur.execute("SELECT * FROM card_system")
    df = pd.read_csv('./data/pao.csv', sep=',')
    # df = pd.DataFrame(cur.fetchall())
    df = df.sample(frac=1).reset_index(drop=True) 
    index = df.index.values.tolist()
    first = [0,3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51]
    second = [1,4,7,10,13,16,19,22,25,28,31,34,37,40,43,46,49,52]
    images = df['ImgLink']
    per = df['Person']
    act = df['Action']
    obj = df['Object']

    return render_template('deck_memorization.html', data=zip(images,per,act,obj,index), first=first, second=second)

@app.route('/card_PAO_memorization')
def card_PAO_memorization():
    # cur = mysql.connection.cursor()
    # cur.execute("SELECT * FROM card_system")
    df = pd.read_csv('./data/pao.csv', sep=',')
    # df = pd.DataFrame(cur.fetchall())
    df = df.sample(frac=1).reset_index(drop=True) 
    images = df['ImgLink']
    per = df['Person']
    act = df['Action']
    obj = df['Object']

    return render_template('card_PAO_memorization.html', data=zip(images,per,act,obj))

@app.route('/PAO_system')
def PAO_system():
    # cur = mysql.connection.cursor()
    # cur.execute("SELECT * FROM card_system")
    df = pd.read_csv('./data/pao.csv', sep=',')
    # df = pd.DataFrame(cur.fetchall())
    df = df[['CardRank','Person','Action','Object']]
    df.columns = ['Card','Person','Action','Object']
    return render_template('PAO_system.html', tables=[df.to_html(classes='data', index=False)], titles=df.columns)


if __name__ == "__main__":
    # app.run(debug=True, host='0.0.0.0', port=5000)
    app.run(debug=True)

