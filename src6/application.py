from flask import Flask, render_template, request

#Configure app
app = Flask(__name__)

#Registered students
students = list()

@app.route("/")
def index():
    name = request.args.get("name", "world")
    return render_template("index.html", foo=name)

@app.route("/registrants")
def registrants():
    return render_template("registered.html", students=students)



@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name") #get arguments in request.args post in .form
    dorm = request.form.get("dorm")
    if not name or not dorm:
        return render_template("failure.html")
    students.append(f"{name} from {dorm}")
    return redirect("/registrants")

