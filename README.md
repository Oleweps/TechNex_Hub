# DLA Instrumentation Hub

**Empowering Industries through Precision and Efficiency**

## Table of Contents
- [Project Proposal](#0-share-your-project-proposal)
- [Project Name and Tagline](#1-project-name-and-tagline)
- [Team Members](#2-team-members)
- [Technologies](#3-technologies)
- [Challenge Statement](#4-challenge-statement)
- [Risks](#5-risks)
- [Infrastructure](#6-infrastructure)
- [Existing Solutions](#7-existing-solutions)
- [Inspiration](#8-inspiration)
- [Built With](#9-built-with)
- [Getting Started](#10-getting-started)
- [Features](#11-features)
  - [Service and Calibration Requests](#service-and-calibration-requests)
  - [Installation, Commissioning, and Training](#installation-commissioning-and-training)
  - [Equipment Marketplace](#equipment-marketplace)
- [API](#12-api)
- [Future](#13-future)
- [Attributions](#14-attributions)
- [Author](#15-author)

## 0. Project Proposal
[Project Proposal Document](link-to-your-google-document)

## 1. Project Name and Tagline
**Project Name:** DLA Instrumentation Hub
**Tagline:** Empowering Industries through Precision and Efficiency

## 2. Team Members
**Team:**
- **[Daniel Nyongesa Wabwile]:** Project Lead & Developer
  - *Role:* Responsible for overall project management, development, and technical decisions.
- *Explanation:* As a solo project, you will handle all aspects of development and management to ensure a cohesive and focused approach.

## 3. Technologies
**Technologies:**
- *Languages:* Python, HTML, CSS, JavaScript
- *Frameworks:* Flask (for web development)
- *Libraries:* Pandas (for data handling), Plotly (for data visualization)
- *Database:* SQLite (for simplicity and ease of deployment)
- *Alternate Option:* Django instead of Flask for web development
  - *Trade-offs:* Django offers more built-in features, but Flask provides greater flexibility. Chose Flask for simplicity and alignment with project scope.

## 4. Challenge Statement
**Challenge:**
- *Problem:* Lack of a centralized platform for equipment service, calibration, and market visibility.
- *Not Solve:* Full-scale e-commerce platform or in-depth CRM functionalities.
- *Users:* Technicians, engineers, and businesses in Kenya's industrial sector.
- *Locale:* Primarily relevant to Kenya but scalable for broader use.

## 5. Risks
**Risks:**
- *Technical Risks:* Potential API integration issues; safeguard by using well-documented APIs.
- *Non-Technical Risks:* Limited user adoption; strategy includes targeted marketing and user training.

## 6. Infrastructure
**Infrastructure:**
- *Branching and Merging:* Follow GitHub Flow for simplicity.
- *Deployment Strategy:* Use Heroku for initial deployment.
- *Data Population:* Manually input initial data, later implement user data uploads.
- *Testing:* Employ automated unit testing with PyTest.

## 7. Existing Solutions
**Existing Solutions:**
- *Similar Products:* Equipment management software, e-commerce platforms.
- *Comparison:* DLA Instrumentation Hub focuses on niche services (calibration, maintenance) specific to the industrial sector.

## 8. Inspiration
DLA Scientific Ltd, being a leader in distributing industrial and laboratory items, inspired the creation of the DLA Instrumentation Hub to address the need for a centralized platform for equipment services, calibration, and marketplace visibility within the industrial sector.

## 9. Built With
### Tools
- Python
- HTML, CSS, JavaScript
- Flask (for web development)
- Pandas (for data handling)
- Plotly (for data visualization)
- SQLite (for database)
### Architecture
- GitHub Flow for version control
- Heroku for deployment
- PyTest for automated testing

## 10. Getting Started
To start using DLA Instrumentation Hub, visit [DLA Instrumentation Hub](https://dlainstrumentationhub.com). To install it, simply clone this repository. You can start the app by running `app.py` as a Python module in a terminal window. Please note, in order to run this app, you will need to install necessary dependencies.

## 11. Features

### Service and Calibration Requests
- Users can submit service and calibration requests for their equipment.
- Technicians can view and manage service requests, updating the status and providing necessary details.

### Installation, Commissioning, and Training
- The platform offers services for equipment installation, commissioning, and training.
- Users can schedule these services and receive confirmation details.

### Equipment Marketplace
- DLA Instrumentation Hub serves as a marketplace for industrial equipment.
- Users can list their equipment for sale, and potential buyers can browse and make inquiries.

## 12. API

I built an internal RESTful API for this web application so that data can be flexibly retrieved from the MySQLdb. All available endpoints can be found in the `api.v1.views` directory.

Here's a description of each endpoint:

- `/api/v1/service-requests/`: GET all service requests and POST to create a new service request
- `/api/v1/service-requests/<request_id>`: GET, PUT, DELETE service request by ID
- `/api/v1/services/`: GET all available services and POST to create a new service
- `/api/v1/services/<service_id>`: GET, PUT, DELETE service by ID
- `/api/v1/equipment-listings/`: GET all equipment listings and POST to create a new listing
- `/api/v1/equipment-listings/<listing_id>`: GET, PUT, DELETE equipment listing by ID

## 13. Future
Beyond this initial MVP, I would like to continue to add many more features to DLA Instrumentation Hub.

- Implement an authentication system for users and technicians
- Enable users to track the progress of their requests and services
- Integrate a messaging system for communication between users and technicians

## 14. Attributions
Attributions and credits to the DLA group of companies for providing inspiration and domain knowledge.

## 15. Author
[Daniel Nyongesa Wabwile]
[weps6179@gmail.com]
