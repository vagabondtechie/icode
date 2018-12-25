from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Welcome to icode", 200

@app.route('/ide', methods=['GET', 'POST'])
def ide():
    if request.method == 'GET':
        return render_template('ide.html')
    elif request.method == 'POST':
        mycode = request.form['mycode']
        language = request.form['language']
        with open('codefile.c', 'w') as codefile:
            codefile.write(mycode)
        return render_template('ide.html', mycode=mycode)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
