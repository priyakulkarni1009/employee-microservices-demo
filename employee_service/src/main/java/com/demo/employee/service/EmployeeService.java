package com.demo.employee.service;

import com.demo.employee.entity.Employee;
import com.demo.employee.repository.EmployeeRepository;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestClient;

import java.util.List;

@Service
public class EmployeeService {

    private final EmployeeRepository repository;
    private final RestClient restClient;

    public EmployeeService(EmployeeRepository repository, RestClient.Builder builder) {
        this.repository = repository;
        this.restClient = builder.baseUrl("http://localhost:8082").build();
    }

    public Employee create(Employee employee) {
        validateDepartment(employee.getDepartmentId());
        return repository.save(employee);
    }

    public List<Employee> getAll() {
        return repository.findAll();
    }

    public Employee getById(Long id) {
        return repository.findById(id)
                .orElseThrow(() -> new RuntimeException("Employee not found: " + id));
    }

    public Employee update(Long id, Employee input) {
        validateDepartment(input.getDepartmentId());

        Employee employee = getById(id);
        employee.setName(input.getName());
        employee.setEmail(input.getEmail());
        employee.setDesignation(input.getDesignation());
        employee.setSalary(input.getSalary());
        employee.setDepartmentId(input.getDepartmentId());

        return repository.save(employee);
    }

    public void delete(Long id) {
        repository.deleteById(id);
    }

    private void validateDepartment(Long departmentId) {
        if (departmentId == null) {
            return;
        }

        restClient.get()
                .uri("/api/departments/{id}", departmentId)
                .retrieve()
                .toBodilessEntity();
    }
}
