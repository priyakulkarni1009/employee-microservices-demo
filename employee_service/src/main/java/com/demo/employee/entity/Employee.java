package com.demo.employee.entity;

import jakarta.persistence.*;

@Entity
@Table(name = "employees")
public class Employee {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String name;

    @Column(nullable = false, unique = true)
    private String email;

    private String designation;
    private Double salary;
    private Long departmentId;

    public Employee() {}

    public Employee(String name, String email, String designation,
                    Double salary, Long departmentId) {
        this.name = name;
        this.email = email;
        this.designation = designation;
        this.salary = salary;
        this.departmentId = departmentId;
    }

    public Long getId() { return id; }
    public String getName() { return name; }
    public String getEmail() { return email; }
    public String getDesignation() { return designation; }
    public Double getSalary() { return salary; }
    public Long getDepartmentId() { return departmentId; }

    public void setId(Long id) { this.id = id; }
    public void setName(String name) { this.name = name; }
    public void setEmail(String email) { this.email = email; }
    public void setDesignation(String designation) { this.designation = designation; }
    public void setSalary(Double salary) { this.salary = salary; }
    public void setDepartmentId(Long departmentId) { this.departmentId = departmentId; }
}
