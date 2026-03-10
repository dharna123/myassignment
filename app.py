from flask import Flask,render_template,request,redirect,url_for
from database import SessionLocal,Tasks

app=Flask(__name__)

@app.route("/")
def index():
    db=SessionLocal()
    tasks=db.query(Tasks).all()
    return render_template('index.html',tasks=tasks)

@app.route('/add',methods=['POST'])
def add_task():
    task_content=request.form.get('content')
    if task_content:
        db=SessionLocal()
        new_task=Tasks(content=task_content)
        db.add(new_task)
        db.commit()
    db.close()
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>',methods=['GET'])
def edit_task(task_id):
    db=SessionLocal()
    task=db.query(Tasks).filter(Tasks.id==task_id).first()
    db.close()
    if task:
        return render_template("edit.html",task=task)
    else:
        return "Task not found",404

@app.route('/update/<int:task_id>',methods=['POST'])
def update_task(task_id):
    db=SessionLocal()
    task=db.query(Tasks).filter(Tasks.id==task_id).first()
    if not task:
        db.close()
        return "Task not found",404
    new_content=request.form.get('new_content')
    completed=request.form.get('completed')
    if new_content:
        task.content=new_content
    task.completed=bool(completed)
    db.commit()
    db.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>',methods=['POST'])
def delete_task(task_id):
    db=SessionLocal()
    task=db.query(Tasks).filter(Tasks.id==task_id).first()
    if not task:
        db.close()
        return "Task not found",404
    db.delete(task)
    db.commit()
    db.close()
    return redirect(url_for('index'))

    
app.run(debug=True)
