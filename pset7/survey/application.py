import cs50
import csv

from flask import Flask, jsonify, redirect, render_template, request

# Configure application
app = Flask(__name__)


# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def post_form():
    if request.method == 'POST':
        fname = request.form['fname']
        if fname == '':
            return render_template("error.html", message="Please enter your details")
        lname = request.form['lname']
        if lname == '':
            return render_template("error.html", message="Please enter your details")
        gender = request.form['gender']
        if gender == '':
            return render_template("error.html", message="Please enter your details")
        fields = [fname, lname, gender]
        with open('survey.csv', 'a') as inFile:
            writer = csv.writer(inFile)
            writer.writerow(fields)

        msg = ""
        for row in fields:
            msg = msg + row + " "
    return render_template("submitted.html", message=msg)


@app.route("/sheet", methods=["GET"])
def get_sheet():
    results = []
    msg = ""
    with open("survey.csv", 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            results.append(row)
            for r in row:
                msg = msg + r + " "
            msg = msg + '\n'

    return render_template("submitted.html", message=msg.replace('\n', '<br>'))