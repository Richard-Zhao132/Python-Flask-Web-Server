from flask import Blueprint, render_template, request, flash, redirect, url_for, flash
from . import mysql
from flask_mysqldb import MySQL

views = Blueprint('views', __name__)



@views.route('/')
def Student():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM student")
    fetchdata = cur.fetchall()
    cur.close()
        
    return render_template("student1.html", students = fetchdata)




@views.route('/class')
def classes():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Course")
    fetchdata = cur.fetchall()
    cur.close()
        
    return render_template("class.html", classes = fetchdata)


@views.route('/teacher')
def teacher():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM professor")
    fetchdata = cur.fetchall()
    cur.close()
    return render_template("teacher.html", professor = fetchdata)

@views.route('/dept')
def dept():
    return render_template("dept.html")


@views.route('/studentClass', methods = ['POST', 'GET'])
def studentClass():
    if request.method == 'POST':
        sID = request.form['sID']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM take Where StudentID=%s", (sID))
        classData = cur.fetchall()
        cur.close()
        return render_template("studentClass.html", studentClasses = classData)
    return render_template("studentClass.html")



@views.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        flash('Data Inserted Successfully')
        sID = request.form['sID']
        Fname = request.form['Fname']
        Lname = request.form['Lname']
        address = request.form['address']
        major = request.form['major']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO student(StudentID, FirstName, LastName, Address, Major) VALUES (%s, %s, %s, %s, %s)", (sID, Fname, Lname, address, major))
        mysql.connection.commit()
        return redirect(url_for('views.Student'))


@views.route('/update', methods = ['POST', 'GET'])
def update():
    if request.method == 'POST':
        sID = request.form['sID']
        Fname = request.form['Fname']
        Lname = request.form['Lname']
        address = request.form['address']
        major = request.form['major']

        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE student
               SET FirstName=%s, LastName=%s, Address=%s, Major=%s
               WHERE StudentID=%s
            """, (Fname, Lname, address, major, sID))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('views.Student'))


@views.route('/delete/<string:id_data>', methods = ['POST', 'GET'])
def delete(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM student WHERE StudentID=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('views.Student'))


@views.route('/insertSC', methods=['POST'])
def insertSC():
    if request.method == 'POST':
        flash('Data Inserted Successfully')
        sID = request.form['sID']
        cID = request.form['cID']
        grade = request.form['grade']


        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO take(StudentID, CourseID, Grade) VALUES (%s, %s, %s)", (sID, cID, grade))
        mysql.connection.commit()
        return redirect(url_for('views.studentClass'))


@views.route('/updateSC', methods = ['POST', 'GET'])
def updateSC():
    if request.method == 'POST':
        sID = request.form['sID']
        cID = request.form['cID']
        grade = request.form['grade']

        cur = mysql.connection.cursor()
        cur.execute("UPDATE take SET grade=%s WHERE StudentID=%s AND CourseID=%s", (grade, sID, cID))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('views.studentClass'))



@views.route('/deleteSC/<string:id_data>', methods = ['POST', 'GET'])
def deleteSC(id_data):
    IDs = id_data.split(' ')
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM take WHERE StudentID=%s AND CourseID=%s", (IDs[0],IDs[1]))
    mysql.connection.commit()
    return redirect(url_for('views.studentClass'))


@views.route('/updateC', methods = ['POST', 'GET'])
def updateC():
    if request.method == 'POST':
        cID = request.form['cID']
        Cname = request.form['Cname']
        credits = request.form['credits']
        prof = request.form['Pname']

        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE Course
               SET CourseID=%s, Title=%s, Credits=%s, ProfessorName=%s
               WHERE CourseID=%s
            """, (cID, Cname, credits, prof, cID))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('views.classes'))


@views.route('/insertC', methods=['POST'])
def insertC():
    if request.method == 'POST':
        flash('Data Inserted Successfully')
        cID = request.form['cID']
        Cname = request.form['Cname']
        credits = request.form['credits']
        prof = request.form['Pname']


        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Course(CourseID, Title, Credits, ProfessorName) VALUES (%s, %s, %s, %s)", (cID, Cname, credits, prof))
        mysql.connection.commit()
        return redirect(url_for('views.classes'))

@views.route('/deleteC/<string:id_data>', methods = ['POST', 'GET'])
def deleteC(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM Course WHERE CourseID=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('views.classes'))




    
@views.route('/updateT', methods = ['POST', 'GET'])
def updateT():
    if request.method == 'POST':
        Pname = request.form['Pname']
        dept = request.form['dept']
        email = request.form['email']

        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE professor
               SET ProfessorName=%s, Department=%s, Email=%s
               WHERE ProfessorName=%s
            """, (Pname, dept, email, Pname))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('views.teacher'))


@views.route('/insertT', methods=['POST'])
def insertT():
    if request.method == 'POST':
        flash('Data Inserted Successfully')
        Pname = request.form['Pname']
        dept = request.form['dept']
        email = request.form['email']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO professor(ProfessorName, Department, Email) VALUES (%s, %s, %s)", (Pname, dept, email))
        mysql.connection.commit()
        return redirect(url_for('views.teacher'))



@views.route('/deleteT/<string:id_data>', methods = ['POST', 'GET'])
def deleteT(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM professor WHERE ProfessorName=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('views.teacher'))