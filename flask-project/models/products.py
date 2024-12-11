from utils.db import db
from sqlalchemy.orm import Mapped, mapped_column
import sqlalchemy as sa

class Products(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(20), unique=True)
    description = sa.Column(sa.String(100))
    price = sa.Column(sa.Integer, nullable=False, default=0)
    stock = sa.Column(sa.Integer, nullable=False, default=0)
    
    def __init__(self, name, description, price, stock):
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        super().__init__()