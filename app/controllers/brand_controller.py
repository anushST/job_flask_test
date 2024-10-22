"""Brand controller."""
from flask import (flash, jsonify, redirect, render_template,
                   request, url_for, Response)

from app import db
from app.forms import BrandForm
from app.models import Brand, Manufacturer
from app.settings import ALLOWED_IMAGE_EXTENSIONS, BASE_DIR, UPLOAD_FOLDER
from app.utils import is_file_ext_allowed, FilePath


class BrandController:
    """Controller for handling brand-related operations."""

    @staticmethod
    def brands_view():
        form = BrandForm()
        form.manufacturer_ids.choices = [
            (m.id, m.name,) for m in Manufacturer.query.all()]
        if form.validate_on_submit():
            file = form.logo.data
            if file and is_file_ext_allowed(file.filename,
                                            ALLOWED_IMAGE_EXTENSIONS):
                file_path = FilePath(file.filename, UPLOAD_FOLDER,
                                     BASE_DIR)
                file.save(file_path.abs_path_filename)

                brand = Brand(
                    logo=file_path.url_path_type,
                    name=form.name.data,
                    description=form.description.data,
                    internal_id=form.internal_id.data
                )
                db.session.add(brand)
                db.session.commit()

                for manufacturer_id in form.manufacturer_ids.data:
                    manufacturer = Manufacturer.query.get(manufacturer_id)
                    brand.manufacturers.append(manufacturer)

                db.session.commit()

                flash('Brand successfuly aded.', 'success')
                return redirect(url_for('client.admin_brands'))
        elif request.method == 'POST':
            error_messages = []
            for field, errors in form.errors.items():
                for error in errors:
                    error_messages.append(
                        f'Error in {getattr(form, field).label.text}: {error}')

            if error_messages:
                flash('\n'.join(error_messages), 'error')

        brands = Brand.query.all()
        return render_template('brands.html', form=form, brands=brands)

    @staticmethod
    def get_brands() -> Response:
        """
        Retrieves a list of all brands.

        **Returns**
        - JSON response containing the names of all brands.
        """
        brands = Brand.query.all()
        brand_list = [Brand.serialize_brand(brand)
                      for brand in brands]
        return jsonify(brand_list)

    @staticmethod
    def get_brand(id: int) -> Response:
        """
        Retrieves information about a specific brand by its ID.

        **Params**
        - `id`: The identifier of the brand.

        **Returns**
        - JSON response with brand data or an error message if
        the brand is not found.
        """
        brand = Brand.query.get(id)
        if brand:
            return jsonify(Brand.serialize_brand(brand))
        else:
            return jsonify({'error': 'Brand not found'}), 404
