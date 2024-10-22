from flask import Blueprint

from app.controllers import BrandController, ManufacturerController

api = Blueprint('api', __name__)

# Brands
api.add_url_rule('/brands', 'get_brands', BrandController.get_brands)
api.add_url_rule('/brands/<int:id>', 'get_brand',
                 BrandController.get_brand)

# Manufacturer
api.add_url_rule('/manufacturers', 'get_manufacturers',
                 ManufacturerController.get_manufacturers)
api.add_url_rule('/manufacturers/<int:id>', 'get_manufacturer',
                 ManufacturerController.get_manufacturer)
