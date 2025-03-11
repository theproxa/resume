from flask import Flask, render_template
import os

app = Flask(__name__)

# Генерация SECRET_KEY
app.config['SECRET_KEY'] = os.urandom(24).hex()

@app.route('/')
def index():
    return render_template('resume_en.html')  # По умолчанию показываем английскую версию

@app.route('/ru')
def resume_ru():
    return render_template('index.html')  # Русская версия

if __name__ == '__main__':
    app.run(debug=True)