# Khodnevis Project

Khodnevis is a Django-based project that provides content and rating management APIs, along with user authentication. 

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [API Endpoints](#api-endpoints)
- [Serializers and ViewSets](#serializers-and-viewsets)
- [Redis Usage](#redis-usage)
- [Celery Tasks](#celery-tasks)

## Features
- Content management: Create, list, update, and delete content items.
- Rating system: Rate content and asynchronously produce the rating to Kafka.
- User authentication and management.
- Asynchronous tasks using Celery.
- Redis integration for caching.

## Technologies Used
- Django
- Django REST Framework (DRF)
- PostgreSQL
- Redis
- Celery
- Docker and Docker Compose

## API Endpoints

### Content API
- **List all content**: `GET /api/contents/`
- **Create content**: `POST /api/contents/`
- **Retrieve a single content**: `GET /api/contents/{id}/`
- **Update content**: `PUT /api/contents/{id}/`
- **Delete content**: `DELETE /api/contents/{id}/`

### Rating API
- **List all ratings**: `GET /api/ratings/`
- **Create a rating**: `POST /api/ratings/`  
  When a rating is created, it is asynchronously sent to Kafka for further processing.
- **Retrieve a single rating**: `GET /api/ratings/{id}/`
- **Update a rating**: `PUT /api/ratings/{id}/`
- **Delete a rating**: `DELETE /api/ratings/{id}/`

### User API
- **User registration**: `POST /api/users/`
- **User login**: `POST /api/users/login/`

## Serializers and ViewSets

### ViewSets
Django REST Framework (DRF) uses **ViewSets** to handle common operations like listing, creating, retrieving, updating, and deleting resources. In this project, the `ContentViewSet` and `RatingViewSet` classes inherit from `ModelViewSet` to provide these functionalities for the `Content` and `Rating` models, respectively.

- **ContentViewSet**:
  - The `ContentViewSet` automatically handles the creation, listing, and updating of content objects. It uses the appropriate serializer based on the request type (list or detail view).

- **RatingViewSet**:
  - The `RatingViewSet` manages the creation and updating of ratings. When a new rating is submitted, instead of saving it immediately, the data is produced to a Kafka topic for asynchronous processing. This approach decouples the task of storing ratings, improving scalability and responsiveness of the application.

### Serializers
**Serializers** in DRF are responsible for transforming complex data types (like Django models) into JSON or other content types that can be rendered into a response. They also handle the deserialization of input data into Django model instances.

- **ContentSerializer**: This serializer handles the conversion of `Content` objects into a format that can be easily returned via the API. It includes all the necessary fields of the content.
  
- **RatingSerializer**: Similar to `ContentSerializer`, the `RatingSerializer` is responsible for converting `Rating` model instances into JSON. It validates and transforms user input into a format suitable for creating or updating `Rating` objects.

By using these **ViewSets** and **Serializers**, the project minimizes boilerplate code, leveraging DRF’s powerful, built-in features for handling CRUD operations.

## Redis Usage

Redis is used in this project for **caching** and **asynchronous task management**.

1. **Caching**:
   - Redis acts as an in-memory data store for caching frequently accessed data. For example, once the average rating for a content object is calculated, the result can be stored in Redis. This reduces the need to perform the same calculation repeatedly, improving performance.
   
2. **Task Management (Celery Backend)**:
   - Redis is also used as the **backend for Celery**, where task results are stored. When background tasks (such as processing ratings or calculating averages) are executed, Redis stores the task results, making them easily retrievable.

## Celery Tasks

Celery is used for background task processing. It offloads time-consuming operations (like computing averages, or handling messages from Kafka) from the main Django application to background workers, ensuring the application remains responsive.

### Example Celery Task: Calculating Average Rating
- When the average rating for content is calculated, the result is stored in Redis for quick access in future API requests.
  
