from flask import Flask, request, render_template, redirect, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app.secret_key= "Jade"

mysql = MySQLConnector(app, 'email_db')

@app.route('/')
def index():		
	return render_template('index.html')

@app.route('/validator', methods=['POST'])
def check():
	name = request.form['email']
	data_emails = mysql.query_db("SELECT * FROM emails")
	count=0

	if len(name) < 1:
		flash("Blank Email Address!")
		count=1
	elif not EMAIL_REGEX.match(name):
		flash("Invalid Email Address!")	
		count=1
	else:
		for x in data_emails:
			if x['email']==name:
				flash("Email is already in use!")
				count=1
				break

	if count==0:
		query="INSERT INTO emails(email,c_date) VALUES(:name2,NOW())"

		data= {
			'name2':name
		}

		mysql.query_db(query, data)
			
	return redirect('/')


app.run(debug=True)
