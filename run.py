import os
from app import create_app
from app import db

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)


if __name__ == '__main__':
    app.run(debug=True)
    db.create_all()
    