from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is my first flask application. Yay!'

@app.route('/second_route')
def route_two():
    return 'This is a second route for my first application.  I hope it works!'

@app.route('/sammy')
def sammy_html():
    return '''
    <html>
        <head>
            <title>Dogs</title>
            <link rel="stylesheet" type="text/css" href="index.css">
        </head>
        <body>
            <h1>Dogs</h1><a href="http://en.wikipedia.org/wiki/Dog">Dog</a>
            <h2>Sammy</h2>
            <img src="sammy.jpg"/>
            <p> Sammy is an awesome dog!</p>
        </body>
    </html>
    '''
