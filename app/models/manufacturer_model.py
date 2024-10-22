from app import db


class Manufacturer(db.Model):
    """
    A model representing a Manufacturer.

    **Fields**:
    - `id`: Integer, primary key, unique identifier for the manufacturer.
    - `name`: String, the name of the manufacturer (max length 50).
    - `description`: Text, a detailed description of the manufacturer.
    - `country`: String, the country where the manufacturer is based
    (max length 50).
    - `certificates`: Text, stores certification information related to the
    manufacturer.
    - `internal_id`: Integer, an internal identifier for the manufacturer.
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.Text)
    country = db.Column(db.String(50))
    certificates = db.Column(db.Text)
    internal_id = db.Column(db.Integer)
    brands = db.relationship('Brand',
                             secondary='brand_manufacturer',
                             back_populates='manufacturers')

    @staticmethod
    def serialize_manufacturer(manufacturer):
        """Serializes a manufacturer object into a dictionary."""
        return {
            'id': manufacturer.id,
            'name': manufacturer.name,
            'description': manufacturer.description,
            'country': manufacturer.country,
            'certificates': manufacturer.certificates,
            'internal_id': manufacturer.internal_id
        }


brand_manufacturer = db.Table(
    'brand_manufacturer',
    db.Column('brand_id', db.Integer, db.ForeignKey('brand.id')),
    db.Column('manufacturer_id', db.Integer, db.ForeignKey('manufacturer.id'))
)
