from flask import Flask, render_template, request, jsonify, url_for, redirect

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def login():
    return render_template("index.html")

@app.route('/add_entry', methods = ['GET', 'POST'])
def add_entry():
    day = request.form.get('day')
    date_time = request.form.get('date_time')
    title = request.form.get('title')
    things_learned = request.form.get('things_learned')

    text_file = open("logs.txt", "a")
    text_file.write(f'''
    ===========================================================
        Day - {day} \n
        Date & Time - {date_time} \n
        Title - {title} \n
        Things Learned - {things_learned} \n
    ===========================================================
    ''')
    text_file.close()

    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True, port=3000)