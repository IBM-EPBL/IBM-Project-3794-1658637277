from flask import Flask, render_template, request, redirect, url_for, session
from newscatcherapi import NewsCatcherApiClient
import requests, json
import ibm_db

app = Flask(__name__)

API_KEY = 'SLnqIfKjC1HEKi13KDCgas-_rYnlIUHN0vu4wkb02Ws'

# newscatcherapi = NewsCatcherApiClient(x_api_key=API_KEY)


app.secret_key = 'a'
conn = ibm_db.connect( 
    "DATABASE=bludb; HOSTNAME=6667d8e9-9d4d-4ccb-ba32-21da3bb5aafc.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud; PORT=30376;SECURITY=SSL; SSLServerCertificate=DigiCertGlobalRootCA.crt; UID=qxd38229; PWD=7BhEfmm9wnlWMfjP",
     '', '')



@app.route('/about.html')
def about_page():
    return render_template('about.html', topic='About')


@app.route('/contact.html')
def contact_page():
    return render_template('contact.html', topic='Contact')


@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['pwd']
        sql = "SELECT * FROM users WHERE email =? and password=?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt, 1, email)
        ibm_db.bind_param(stmt, 2, password)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            print("Login successful")
            return redirect(url_for('main_page', topic='Trending'))
        else:
            return render_template('elsepage.html')