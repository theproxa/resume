import os
from flask import Flask, render_template

app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(24).hex()
# Настройка MIME-типов
app.config['FREEZER_DEFAULT_MIMETYPE'] = 'text/html'

@app.route('/')
def index():
    return render_template('resume_en.html')

@app.route('/ru.html')  # Маршрут для русской версии
def resume_ru():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)