import sqlite3
from flask import Flask, render_template, request

query_list=[]
app=Flask(__name__)
conn = sqlite3.connect('blood.db')
curs=conn.cursor()

try:
 curs.execute('''CREATE TABLE blood(ID int AUTO_INCREMENT, username varchar(50) NOT NULL, password varchar(50) NOT NULL, name varchar(50) NOT NULL,dob Date, gender varchar(10) NOT NULL, bloodgroup varchar(10) NOT NULL, pno int(10) NOT NULL, email varchar(50) NOT NULL, town varchar(50) NOT NULL, city varchar(50) NOT NULL); ''')
 print('Table Created')
except:
 print('Table Already Created')

conn.close()

def read_data_from_table():
    conn=sqlite3.connect('blood.db')
    cursor = conn.execute("SELECT * from blood");
    for i in cursor:
        print (i)
    conn.close()


def read_data_for_homePage(k):
    global query_list
    conn=sqlite3.connect('blood.db')
    cursor=conn.execute("SELECT * from blood WHERE bloodgroup=" + k)
    for i in cursor:
        print(i)
        query_list.append(i)
    conn.close()
    return query_list

@app.route('/')
@app.route('/index')
def index():
    return (render_template('index.html'))

@app.route('/about')
def about():
    return (render_template('about.html'))

@app.route('/contact')
def contact():
    return (render_template('contact.html'))

@app.route('/register')
def register():
    return (render_template('register.html'))

@app.route('/change_details')
def change_details():
    return (render_template('change_details.html'))

@app.route('/find_blood')
def find_blood():
    return (render_template('find_donor.html'))

@app.route('/homeblood',methods=['GET'])
def home_blood():
    global query_list
    blood_request_type=request.args.get('bloodgroup')
    print(blood_request_type)
    rows=read_data_for_homePage(blood_request_type)
    print(rows)
    query_list=[]
    return (render_template('find_blood.html',rows=rows))

@app.route('/passdb',methods=['POST'])
def pass_db():
    username='demo'
    password='demo'
    fullname=request.form['fullname']
    dob=request.form['dob']
    gender=request.form['gender']
    bloodgroup=request.form['bloodgroup']
    mobile=request.form['mobile']
    email=request.form['email']
    town=request.form['town']
    state=request.form['state']
    print(username,password,fullname,dob,gender,bloodgroup,mobile,email,town,state)
    conn = sqlite3.connect('blood.db')
    cursor = conn.execute("INSERT INTO blood (username,password,name,dob,gender,bloodgroup,pno,email,town,city) VALUES (?,?,?,?,?,?,?,?,?,?)",(username,password,fullname,dob,gender,bloodgroup,mobile,email,town,state))
    conn.commit()
    print ('Registered into the Table')
    return (render_template('register.html',resultCode='Stored Successfully'))

if __name__=="__main__":
    app.run(debug=True)

