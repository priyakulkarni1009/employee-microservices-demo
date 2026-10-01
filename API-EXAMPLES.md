# API Examples

Start all three services, then use the gateway on port 8080.

## 1. Create department

```bash
curl -X POST http://localhost:8080/api/departments \
-H "Content-Type: application/json" \
-d '{"name":"Artificial Intelligence","location":"Bengaluru"}'
```

## 2. Create employee

```bash
curl -X POST http://localhost:8080/api/employees \
-H "Content-Type: application/json" \
-d '{"name":"Priya Kulkarni","email":"priya@example.com","designation":"Python Developer","salary":45000,"departmentId":1}'
```

## 3. Read employees

```bash
curl http://localhost:8080/api/employees
```

## 4. Read one employee

```bash
curl http://localhost:8080/api/employees/1
```

## 5. Update employee

```bash
curl -X PUT http://localhost:8080/api/employees/1 \
-H "Content-Type: application/json" \
-d '{"name":"Priya Kulkarni","email":"priya@example.com","designation":"AI Engineer","salary":55000,"departmentId":1}'
```

## 6. Delete employee

```bash
curl -X DELETE http://localhost:8080/api/employees/1
```
