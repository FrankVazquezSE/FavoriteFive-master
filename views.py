from flask import Blueprint, render_template, request, redirect,

views = Blueprint(__name__,"views")

@views.route('/')
def home():
    return render_template("index.html",name="Frank")

@views.route('/FaveFive')
def FaveFive():
    args = request.args
    name = args.get('name')
    return render_template("index.html", name="FaveFive")

@views.route("/json")
def get_json():
    return jsonify({'name':'Frank'})

@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

@views.route("go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))