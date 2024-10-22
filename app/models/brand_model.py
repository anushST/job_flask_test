from flask import request

from .manufacturer_model import Manufacturer
from app import db


class Brand(db.Model):
    """
    A model representing a Brand.

    **Fields**:
    - `id`: Integer, primary key, unique identifier for the brand.
    - `logo`: String, stores the URL or path to the brand's logo image
    (max length 500).
    - `name`: String, the name of the brand (max length 50).
    - `description`: Text, a detailed description of the brand.
    - `internal_id`: Integer, an internal identifier for the brand.
    """

    id = db.Column(db.Integer, primary_key=True)
    logo = db.Column(db.String(500))
    name = db.Column(db.String(50))
    description = db.Column(db.Text)
    internal_id = db.Column(db.Integer)
    # secondary table is in manufactorer_model.py
    manufacturers = db.relationship('Manufacturer',
                                    secondary='brand_manufacturer',
                                    back_populates='brands')

    @staticmethod
    def serialize_brand(brand):
        """
        Serializes a brand object into a dictionary, including its
        manufacturers.
        """
        return {
            'id': brand.id,
            'name': brand.name,
            'description': brand.description,
            'internal_id': brand.internal_id,
            'logo': f'{request.host_url}{brand.logo}',
            'manufacturers': [Manufacturer.serialize_manufacturer(m)
                              for m in brand.manufacturers]
        }
