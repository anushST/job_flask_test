"""Manufacturer controller"""
from flask import (flash, jsonify, redirect, render_template,
                   url_for, Response)

from app import db
from app.forms import ManufacturerForm
from app.models import Manufacturer


class ManufacturerController:
    """Controller for handling manufacturer-related operations."""

    @staticmethod
    def manufacturers_view():
        form = ManufacturerForm()
        if form.validate_on_submit():
            new_manufacturer = Manufacturer(
                name=form.name.data,
                description=form.description.data,
                country=form.country.data,
                certificates=form.certificates.data,
                internal_id=form.internal_id.data
            )
            db.session.add(new_manufacturer)
            db.session.commit()
            flash('Manufacturer successfuly aded', 'success')
            return redirect(url_for('client.admin_manufacturers'))

        manufacturers = Manufacturer.query.all()
        return render_template('manufacturers.html', form=form,
                               manufacturers=manufacturers)

    @staticmethod
    def get_manufacturers() -> Response:
        """
        Retrieves a list of all manufacturers.

        **Returns**
        - JSON response containing the names of all manufacturers.
        """
        manufacturers = Manufacturer.query.all()
        manufacturers_list = [Manufacturer.serialize_manufacturer(manuf)
                              for manuf in manufacturers]
        return jsonify(manufacturers_list)

    @staticmethod
    def get_manufacturer(id: int) -> Response:
        """
        Retrieves information about a specific manufacturer by its ID.

        **Params**
        - `id`: The identifier of the manufacturer.

        **Returns**
        - JSON response with manufacturer data or an error message
        if the manufacturer is not found.
        """
        manufacturer = Manufacturer.query.get(id)
        if manufacturer:
            return jsonify(Manufacturer.serialize_manufacturer(manufacturer))
        else:
            return jsonify({'error': 'Manufacturer not found'}), 404
