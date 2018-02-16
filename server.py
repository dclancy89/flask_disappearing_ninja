from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ninja')
def ninja():
	return render_template('ninja.html', img='tmnt.png')

@app.route('/ninja/<color>')
def ninja_color(color):
	if color == "blue":
		img = "leonardo.jpg"
	elif color == "orange":
		img = "michelangelo.jpg"
	elif color == "red":
		img = "raphael.jpg"
	elif color == "purple":
		img = "donatello.jpg"
	else:
		img = "notapril.jpg"
	return render_template('ninja.html', img=img)

app.run(debug=True)