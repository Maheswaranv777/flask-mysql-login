from flask import Flask ,render_template,request,session
import mysql.connector as ra
app=Flask(__name__)
app.secret_key="ui"
con=ra.connect(host="localhost",user="root",password="root")
cur=con.cursor(dictionary=True)
try:
    cur.execute("create database rock")
except:
    pass

finally:
    cur.execute("use rock")
    try:
        cur.execute("create table rko(Id int primary key auto_increment,name varchar(20),password int)")
    except:
        pass
@app.route("/",methods=["GET","POST"])
def Ak():
    if request.method=="POST":
        a=request.form['name']
        b=int(request.form['pcode'])
        # session['name']=a
        # session['pcode']=b
        cur.execute("insert into rko(name,password) values(%s,%s)",(a,b))
        con.commit()
        return render_template("lo.html")
    else:
        return render_template("sin.html")
@app.route("/log",methods=["GET","POST"])
def log():
    if request.method=="POST":
        c=request.form['lname']
        d=int(request.form['lcode'])
        # where name=%s and password=%s",(c,d)
        cur.execute("select * from rko")
        k=cur.fetchall()
        print(k)
        for t in k:
            if t['name']==c and t['password']==d:
                 return "login in succesfull"
        else:
            return "failed"

    else:
        return render_template("tik.html")




if __name__=="__main__":
    app.run(debug=True)

