from flask import Flask
from routes.products import products_blueprint
from utils.db import db

app = Flask(__name__)

app.register_blueprint(products_blueprint)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost:3307/products_demo"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(port=4000, debug=True)