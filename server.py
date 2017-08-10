from flask import Flask, request, render_template, redirect, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key= "Jade"

mysql = MySQLConnector(app, 'email_db')

@app.route('/')
def index():		
	return render_template('index.html')

@app.route('/validator', methods=['POST'])
def check():
	name = request.form['email']
	print name
	return redirect('/')


app.run(debug=True)
