from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def register():
    return render_template('Register.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/image')
def image():
    return render_template('img/background.jpg')

if __name__=="__main__":
    app.run(debug=True)