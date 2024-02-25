#!/usr/bin/python3
"""
Contains the admin dashboard routes
"""
from flask import Flask, render_template
from models import storage
from models.service import Service

app = Flask(__name__)

@app.route('/services-marketplace')
def services_marketplace():
    services = storage.all(Service).values()
    return render_template('services_marketplace.html', services=services)

if __name__ == '__main__':
    app.run(debug=True)
