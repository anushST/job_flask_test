from flask import Blueprint

from app.controllers import BrandController, ManufacturerController

client = Blueprint('client', __name__)

client.add_url_rule('/brands', 'admin_brands',
                    BrandController.brands_view,
                    methods=('GET', 'POST',))
client.add_url_rule('/manufacturer', 'admin_manufacturers',
                    ManufacturerController.manufacturers_view,
                    methods=('GET', 'POST',))
