from flask_frozen import Freezer
from app import app

freezer = Freezer(app)

# Указываем URL для генерации
@freezer.register_generator
def url_generator():
    yield '/'
    yield '/ru.html'

if __name__ == '__main__':
    freezer.freeze()