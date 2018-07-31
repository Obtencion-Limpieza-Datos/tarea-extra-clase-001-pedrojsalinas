from flask import Flask,render_template,request
from wtforms import Form, SelectField, StringField, PasswordField, validators
import pandas as pd
import sqlite3

app = Flask(__name__)

class BuscadorForm(Form):
    query = StringField('', validators=[validators.required()])
    opcion = SelectField('Programming opcion',choices=[('provincia', 'Provincia'), ('ciudad', 'Ciudad'), ('tipo', 'Tipo lugar')])


@app.route('/',methods=['POST', 'GET'])
def index():
    data = None
    long = None
    form = BuscadorForm(request.form)
    if request.method == 'POST':
        query=request.form['query']
        opcion=request.form['opcion']
        if form.validate():
            conn = sqlite3.connect("database.db")
            df = pd.read_sql("SELECT * from turisticos", conn)
            if(opcion=='provincia'):
                data = df[(df['Provincia'].str.contains(query.upper(),na=False))][['Nombre','Tipolugar','Provincia','Ciudad','Localizacion']]
            elif(opcion=='ciudad'):
                data = df[(df['Ciudad'].str.contains(query.upper(),na=False))][['Nombre','Tipolugar','Provincia','Ciudad','Localizacion']]
            else:
                data = df[(df['Tipolugar'].str.contains(query.upper(),na=False))][['Nombre','Tipolugar','Provincia','Ciudad','Localizacion']]
            data = data.to_dict(orient="records")
            long=len(data)
    return render_template('index.html',form=form,data=data,long=long )
