from flask import Flask
from flask import request
from flask import url_for

app = Flask(__name__)


@app.route('/choice/<planet_name>')
def choice():
    choice_list = [
        'Эта планета близка к Земле',
        "На ней много необходимых ресурсов",
        "На ней есть вода и атмсофсера",
        "На ней есть небольшое магнитное поле",
        "Наконец, она просто красива!"
    ]
    return """<!doctype html>
                <html lang='en'>
                 <head>
                  <meta charset="utf-8">
                  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
                  <title>Выборы</title>
                 <head>
                 <body>
                  <h1>"Моё предложение: {}</h1>"
                  <h3>{}</h3>
                  <div class = "alert-success" role="alert">
                   <br><h3>{}</h3>
                  </div>
                  <div class = "alert-secondary" role="alert">
                   <br><h3>{}</h3>
                  </div>
                  <div class = "alert-warning" role="alert">
                   <br><h3>{}</h3>
                  </div>
                  <div class = "alert-danger" role="alert">
                   <br><h3>{}</h3>
                  </div>
                 </body>
                </html>""".format(planet_name, *choice_list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
