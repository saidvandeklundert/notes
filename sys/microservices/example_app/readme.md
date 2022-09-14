
The orders service consists of 3 packages:
- core business logic (implements the capabilities of the service)
- API layer: allows clients to interact with the service over HTTP
- data layer: allws the service to interact with the database


SQLAlchemy models live in oders/repository/models.py. These modesl interface with the database.