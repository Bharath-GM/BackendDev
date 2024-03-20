# Card Status Tracking Service
This document outlines the development approach, technology stack, architectural decisions, and potential areas for improvement for the Card Status Tracking Service. The service is designed to provide internal API endpoints for querying the status of users' cards based on data aggregated from various partner companies.

## Overview
The Card Status Tracking Service combines data from different CSV files shared by partner companies to provide a unified view of a user's card status. It supports querying card status by the card ID or user's phone number, offering vital support for customer service agents and internal tracking purposes.

## Technology Stack
### Flask-RESTx and Python
Flask-RESTx, an extension of Flask, was chosen for its simplicity and powerful capabilities in developing RESTful APIs. Python's wide adoption, extensive libraries, and readability make it an ideal choice for rapid development and ease of maintenance. Flask-RESTx enhances Flask by providing built-in support for input validation, serialization, documentation, and more, making it a robust solution for our API service.

### Snowflake
Snowflake is selected as the database solution for its advanced data warehousing capabilities and support for both structured and semi-structured data. Its cloud-native, scalable architecture allows for managing large volumes of data with ease, ensuring high performance and flexibility in data analysis and integration.

### Gunicorn
Gunicorn is used as the WSGI HTTP Server to serve the Flask application in production. It is a Python WSGI HTTP Server for UNIX, offering a powerful and simple interface for deploying Python web applications. Gunicorn provides efficient and robust handling of concurrent requests, making it well-suited for production environments.

## Architectural Decisions
### Sophisticated Data Integration
Our backend leverages Python’s powerful data manipulation libraries, like Pandas, for an advanced data handling strategy. This approach ensures meticulous cleaning, validation, and consolidation of varied CSV datasets from multiple partners. It guarantees the integrity and accuracy of the card status data, seamlessly managing diverse data formats.

### Agile Data Structure Adaptability
By combining Flask-RESTx with SQLAlchemy, our architecture excels in dynamic data model adaptation. The ORM layer allows for swift updates to the database schema, accommodating data variances effortlessly. This agility is pivotal for responding to the changing needs of card status information, keeping our API service responsive and dependable.

### Modular Service Design
Our application’s logic is segmented into distinct layers, each tasked with specific operations from data processing to API responses. This modular design promotes ease of updates, scalability, and enhanced testability, facilitating smooth integration between business logic and data management layers for efficient service delivery.

### Enhanced Operational Resilience
Incorporating advanced error handling and logging mechanisms ensures our service's robustness. These strategically placed safeguards throughout the application not only streamline troubleshooting but also enhance the reliability and user experience of our API, making it a trustworthy tool for internal use.

### Optimized Deployment Strategy
Utilizing Docker for containerization and Gunicorn as the HTTP server underscores our commitment to performance and scalability. This setup ensures efficient request handling and consistent operational environments across different deployment stages, aligning with our goals for a highly available and scalable service.
## Build and Run Instructions

* **Build the Docker Image:** docker build -t card_status_service .

* **Run the Docker Container:** docker run -d -p 8000:8000 card_status_service

* This setup ensures the Flask application is served with Gunicorn, enhancing performance and concurrency handling in production.

## Possible Improvements
* **Caching:** Implement caching mechanisms for frequently requested data to reduce database load and improve response times.

* **Automated Data Pipelines:** Develop automated pipelines for real-time data ingestion and processing from CSV files to the database.

* **Security Enhancements:** Incorporate advanced security measures, including API rate limiting, authentication, and encryption, to protect sensitive data and services.

## Conclusion
The Card Status Tracking Service leverages Flask-RESTx, Snowflake, and Gunicorn, encapsulated within Docker, to provide a robust, scalable, and efficient solution for internal card status tracking. This service embodies a thoughtful approach to technology selection, architectural design, and potential areas for future enhancement, ensuring it remains adaptable and effective in meeting the evolving needs of the organization.