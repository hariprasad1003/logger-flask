'''
author - Hari Prasad

resorces - 
    https://stackoverflow.com/questions/38055762/how-do-you-save-the-inputs-into-text-file
    https://www.quora.com/What-is-the-right-way-to-read-a-file-and-display-its-content-on-browser-using-flask
    https://www.kite.com/python/answers/how-to-erase-the-file-contents-of-a-text-file-in-python
    https://medium.com/@tasnuva2606/dockerize-flask-app-4998a378a6aa
    
'''

'''
    text_file = open('logs.txt', 'r') 
    show_file = text_file.read()
    print(show_file)
    return render_template('show_log.html', text=show_file)

    with open('logs.txt', 'r') as f: 
        return render_template('show_log.html', text=f.read())

'''



from flask import Flask, render_template, request, jsonify, url_for, redirect

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def login():
    return render_template("index.html")

@app.route('/view_log', methods = ['GET', 'POST'])
def view_log():
    with open('logs.txt', 'r') as f: 
        return render_template('show_log.html', text=f.read())

@app.route('/add_entry', methods = ['GET', 'POST'])
def add_entry():

    day             = request.form.get('day')
    date_time       = request.form.get('date_time')
    title           = request.form.get('title')
    things_learned  = request.form.get('things_learned')

    text_file = open("logs.txt", "a")
    text_file.write(f'''
=========================================================== \n
Day - {day} \n
Date & Time - {date_time} \n
Title - {title} \n
Things Learned - \n{things_learned} \n \t
=========================================================== \n
    ''')
    text_file.close()

    return redirect(url_for('login'))
    
@app.route('/clear_logs', methods = ['GET', 'POST'])
def clear_logs():
    
    text_file = open("logs.txt","r+")
    text_file.truncate(0)
    text_file.close()

    return redirect(url_for('view_log'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)