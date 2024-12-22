from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)

@app.route("/")
def index():
    language = request.cookies.get('language', 'ru')
    
    theme = request.cookies.get('theme', 'light')
    
    return render_template("index.html", language=language, theme=theme)


@app.route("/set_language/<lang>")
def set_language(lang):
    """
    Сохраняем выбранный язык в cookie на год (макс. срок 365 дней).
    После установки куки — делаем редирект на главную.
    """
    resp = make_response(redirect(url_for('index')))
    resp.set_cookie('language', lang, max_age=60*60*24*365)  
    return resp


@app.route("/set_theme/<th>")
def set_theme(th):
    """
    Сохраняем выбранную тему в cookie на год (макс. срок 365 дней).
    После установки куки — редирект на главную.
    """
    resp = make_response(redirect(url_for('index')))
    resp.set_cookie('theme', th, max_age=60*60*24*365)  
    return resp


if __name__ == "__main__":
    app.run(debug=False)
