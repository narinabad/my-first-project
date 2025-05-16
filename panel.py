
from flask import Blueprint,render_template,url_for,redirect,request
from extentions import db
from func import get_user
from models.Task import Task
from models.Contact import Contact

panel=Blueprint('panel_blueprint',__name__)


@panel.route('/')
def home():
 user=get_user()
 if get_user == False:
     return redirect(url_for('login_blueprint.home'))
 return render_template('panel.html',user=user)


@panel.route('/add',methods=['POST'])
def add():
 user=get_user()
 if get_user == False:
   return '{"status":"nologin"}'
 description=request.form["description"]
 task=Task(description=description)
 
 user.tasks.append(task)
 db.session.add(task)
 db.session.commit()
 return '{"status":"ok","task_id":"'+str(task.id)+'"}'

@panel.route('/remove',methods=['POST'])
def remove():
 user=get_user()
 if get_user == False:
   return '{"status":"nologin"}'
 task_id=request.form["id"]
 Task.query.filter(Task.id==task_id).delete()
 db.session.commit()
 return '{"status":"ok"}'

@panel.route('/update',methods=['POST'])
def update():
 user=get_user()
 if get_user == False:
   return '{"status":"nologin"}'
 task_id=request.form["id"]
 description=request.form["description"]
 task=Task.query.filter(Task.id==task_id).first()
 task.description=description
 db.session.commit()
 return '{"status":"ok"}'

@panel.route('/edit_contact',methods=['POST'])
def edit_contact():
 user=get_user()
 if user == False:
   return redirect(url_for('login_blueprint.home'))
 city=request.form["city"]
 phone=request.form["phone"]
 if(user.contact != None):
   user.contact.phone=phone
   user.contact.city=city
 else:
    contact=Contact(phone=phone,city=city)
    user.contact=contact
    db.session.add(contact)
 db.session.commit()
 return redirect(url_for('panel_blueprint.home'))