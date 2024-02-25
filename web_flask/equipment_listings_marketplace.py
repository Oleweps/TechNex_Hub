#!/usr/bin/python3
"""
Contains the admin dashboard routes
"""
from flask import Flask, render_template, request, redirect, url_for
from models.equipment_listings_marketplace import EquipmentListing, EquipmentListingForm
from models import storage

app = Flask(__name__)
storage = Storage()

@app.route('/equipment_listings_marketplace', methods=['GET', 'POST'])
def equipment_listings_marketplace():
    form = EquipmentListingForm()

    if request.method == 'POST' and form.validate_on_submit():
        # Retrieve form data
        equipment_name = form.equipment_name.data
        description = form.description.data
        condition = form.condition.data
        price = form.price.data
        contact_details = form.contact_details.data

        # Create a new equipment listing instance
        new_listing = EquipmentListing(
            user_id='user_id_placeholder',  # Replace with the actual user ID
            equipment_name=equipment_name,
            description=description,
            condition=condition,
            price=price,
            contact_details=contact_details
        )

        # Add the new equipment listing to the database
        storage.new(new_listing)
        storage.save()

        return redirect(url_for('equipment_listings_marketplace'))

    # Retrieve equipment listings from storage
    equipment_listings = storage.all(EquipmentListing).values()

    return render_template('equipment_listings_marketplace.html', form=form, equipment_listings=equipment_listings)

if __name__ == '__main__':
    app.run(debug=True)
