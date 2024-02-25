#!/usr/bin/python3
"""
Contains the admin dashboard routes
"""
import uuid
from flask import Flask, render_template, request, redirect, url_for, jsonify
from models.suggestion import Suggestion, User, SuggestionForm
from models import storage
from datetime import datetime

app = Flask(__name__)

@app.route('/suggestions', methods=['GET', 'POST'])
def suggestions():
    suggestion_form = SuggestionForm()

    if request.method == 'POST' and suggestion_form.validate_on_submit():
        # Handle submitting a new suggestion
        user_id = suggestion_form.user_id.data  # Assuming you have a hidden input in your form for user_id
        content = suggestion_form.content.data

        # Create a new suggestion
        new_suggestion = Suggestion(
            user_id=user_id,
            content=content,
            timestamp=datetime.now(),
            title=suggestion_form.title.data,
            category=suggestion_form.category.data,
            status=suggestion_form.status.data
        )

        # Add and save the new suggestion to the storage
        storage.new(new_suggestion)
        storage.save()

        # Return a JSON response indicating successful suggestion submission
        return jsonify({'message': 'Suggestion submitted successfully'})

    # Retrieve suggestions from storage (you may need to filter suggestions based on the logged-in user)
    suggestions = storage.all(Suggestion).values()

    # Generate a UUID (cache_id)
    cache_id = str(uuid.uuid4())

    return render_template('suggestions.html', suggestions=suggestions, suggestion_form=suggestion_form, cache_id=cache_id)

if __name__ == '__main__':
    app.run(debug=True)
