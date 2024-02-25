#!/usr/bin/python3
"""
Contains the admin dashboard routes
"""
from flask import Flask, render_template, request, redirect, url_for, jsonify
from models.equipment_listing import EquipmentListing, EquipmentListingForm
from models import storage
import uuid

app = Flask(__name__)

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

        # Generate a UUID as the cache_id
        cache_id = str(uuid.uuid4())

        return redirect(url_for('equipment_listings_marketplace', cache_id=cache_id))

    # Retrieve equipment listings from storage
    equipment_listings = storage.all(EquipmentListing).values()

    # Generate a UUID as the cache_id
    cache_id = str(uuid.uuid4())

    return render_template('equipment_listings_marketplace.html', form=form, equipment_listings=equipment_listings, cache_id=cache_id)

@app.route('/inquire-equipment', methods=['POST'])
def inquire_equipment():
    if request.method == 'POST':
        equipment_id = request.form.get('equipment_id')

        # Fetch equipment details from the database based on equipment_id
        equipment = storage.get(EquipmentListing, id=equipment_id)

        # You can now implement the logic to handle the equipment inquiry
        # For demonstration purposes, we'll just return a success message with equipment details
        response_data = {
            'message': 'Inquiry sent successfully',
            'equipment_name': equipment.equipment_name,
            'equipment_description': equipment.description,
            'equipment_price': equipment.price,
            'contact_details': equipment.contact_details,
        }
        return jsonify(response_data)

@app.route('/search-equipment', methods=['GET'])
def search_equipment():
    search_query = request.args.get('query', '').strip()

    if search_query:
        # Perform search logic based on your requirements
        # For example, you can query the database for equipment matching the search query
        equipment_results = EquipmentListing.query.filter(
            EquipmentListing.equipment_name.ilike(f"%{search_query}%")
        ).all()

        # Prepare the results to be sent as JSON
        results = [{
            'equipment_name': equipment.equipment_name,
            'description': equipment.description,
            'condition': equipment.condition,
            'price': equipment.price,
            'contact_details': equipment.contact_details
        } for equipment in equipment_results]

        return jsonify({'message': 'Search successful', 'query': search_query, 'results': results})
    else:
        return jsonify({'message': 'Invalid search query'})

# ... (existing code)

if __name__ == '__main__':
    app.run(debug=True)
