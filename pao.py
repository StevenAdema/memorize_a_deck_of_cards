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


class Pao:
    def __init__(self, name='STEVEN'):
        self.name = name
        mysql = MySQL(app)
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM card_system")
        df = pd.DataFrame(cur.fetchall())
        df = df.sample(frac=1).reset_index(drop=True)
        df.columns = ['PaoSystemId','CardId','CardRank','Suit','Person','Action','Object','ImgLink']

    def display_df(self):
        print(self.df)

p = Pao()
p.display_df()