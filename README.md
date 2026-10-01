# Employee Portal – Spring Boot Microservices API Demo

A simple GitHub-ready Spring Boot microservices project demonstrating:

- Microservices architecture
- REST APIs
- API-to-API communication using `RestClient`
- Full CRUD operations
- H2 in-memory database by default
- External RDBMS configuration through environment variables
- JPA/Hibernate
- Maven multi-module project
- Docker Compose for PostgreSQL (optional)

## Architecture

```text
                    +----------------------+
                    |     API Gateway      |
                    |      :8080           |
                    +----------+-----------+
                               |
                 +-------------+-------------+
                 |                           |
                 v                           v
       +-------------------+       +-------------------+
       | Employee Service  |       | Department Service|
       |      :8081        |       |      :8082        |
       +---------+---------+       +---------+---------+
                 |                           |
                 v                           v
              H2 / RDBMS                 H2 / RDBMS
```

The Employee Service also calls the Department Service through REST API to validate the department.

## Project Structure

```text
employee-microservices-demo/
├── pom.xml
├── README.md
├── docker-compose.yml
├── api-gateway/
├── employee-service/
└── department-service/
```

## Requirements

- Java 17+
- Maven 3.9+
- Git
- Optional: Docker Desktop for PostgreSQL

## Run with H2

H2 is the default database, so no database installation is required.

### Start Department Service

```bash
mvn -pl department-service spring-boot:run
```

### Start Employee Service

In another terminal:

```bash
mvn -pl employee-service spring-boot:run
```

### Start API Gateway

In another terminal:

```bash
mvn -pl api-gateway spring-boot:run
```

Services:

- Gateway: http://localhost:8080
- Employee Service: http://localhost:8081
- Department Service: http://localhost:8082
- H2 Console - Employee: http://localhost:8081/h2-console
- H2 Console - Department: http://localhost:8082/h2-console

## Employee CRUD APIs

### Create

```http
POST http://localhost:8080/api/employees
Content-Type: application/json

{
  "name": "Priya Kulkarni",
  "email": "priya@example.com",
  "designation": "Python Developer",
  "salary": 45000,
  "departmentId": 1
}
```

### Get all

```http
GET http://localhost:8080/api/employees
```

### Get by ID

```http
GET http://localhost:8080/api/employees/1
```

### Update

```http
PUT http://localhost:8080/api/employees/1
Content-Type: application/json

{
  "name": "Priya Kulkarni",
  "email": "priya@example.com",
  "designation": "AI Engineer",
  "salary": 55000,
  "departmentId": 1
}
```

### Delete

```http
DELETE http://localhost:8080/api/employees/1
```

## Department CRUD APIs

```http
POST   http://localhost:8080/api/departments
GET    http://localhost:8080/api/departments
GET    http://localhost:8080/api/departments/{id}
PUT    http://localhost:8080/api/departments/{id}
DELETE http://localhost:8080/api/departments/{id}
```

Example:

```http
POST http://localhost:8080/api/departments
Content-Type: application/json

{
  "name": "Artificial Intelligence",
  "location": "Bengaluru"
}
```

## API-to-API Communication

When an employee is created, the Employee Service calls:

```text
GET http://localhost:8082/api/departments/{departmentId}
```

The Employee Service does not directly access the Department Service database.

This demonstrates a basic microservice principle:

```text
Employee Service
      |
      | REST API
      v
Department Service
      |
      v
Department Database
```

## Switch from H2 to an External RDBMS

The project has two profiles:

- `h2` – default, in-memory
- `rdbms` – external database

Example using PostgreSQL:

```bash
mvn -pl department-service spring-boot:run \
  -Dspring-boot.run.profiles=rdbms \
  -Dspring-boot.run.arguments="--DB_URL=jdbc:postgresql://localhost:5432/departments --DB_USERNAME=postgres --DB_PASSWORD=postgres"
```

For Employee Service:

```bash
mvn -pl employee-service spring-boot:run \
  -Dspring-boot.run.profiles=rdbms \
  -Dspring-boot.run.arguments="--DB_URL=jdbc:postgresql://localhost:5432/employees --DB_USERNAME=postgres --DB_PASSWORD=postgres"
```

You can also use environment variables:

```bash
DB_URL=jdbc:postgresql://localhost:5432/employees
DB_USERNAME=postgres
DB_PASSWORD=postgres
DB_DRIVER=org.postgresql.Driver
DB_DIALECT=org.hibernate.dialect.PostgreSQLDialect
```

### Supported example JDBC configurations

#### PostgreSQL

```text
DB_URL=jdbc:postgresql://localhost:5432/employees
DB_DRIVER=org.postgresql.Driver
DB_DIALECT=org.hibernate.dialect.PostgreSQLDialect
```

#### MySQL

```text
DB_URL=jdbc:mysql://localhost:3306/employees
DB_DRIVER=com.mysql.cj.jdbc.Driver
DB_DIALECT=org.hibernate.dialect.MySQLDialect
```

The matching JDBC driver is included in the Maven build.

For another RDBMS, add its JDBC driver dependency and provide its JDBC URL/driver/dialect.

## Optional PostgreSQL

```bash
docker compose up -d
```

This creates:

- employees database on port 5432
- departments database on port 5433

Then run both services with the `rdbms` profile.

## Important Note

There is no single JDBC driver that can connect to every RDBMS. The application intentionally accepts the database-specific parameters through configuration, while Maven contains common PostgreSQL and MySQL drivers.

For production, database credentials should be stored in environment variables or a secret manager, not committed to GitHub.

## Useful GitHub Description

> A simple Spring Boot microservices Employee Portal demonstrating REST APIs, CRUD operations, service-to-service communication, H2 in-memory persistence, and configurable external RDBMS connectivity.
