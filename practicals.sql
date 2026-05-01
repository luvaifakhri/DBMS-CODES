=======================================
1 - Demonstration of creating database.
=======================================
CREATE DATABASE School;

=========================================
2 - Create table insert 10 records in it.
=========================================
-- Create Table
CREATE TABLE student (
 id NUMBER PRIMARY KEY,
 name VARCHAR2(50),
 age NUMBER
);
-- Insert Records
INSERT INTO student (id, name, age) VALUES (1, 'Rahul', 20);
(2, 'Amit', 21);
(3, 'Neha', 19);
(4, 'Priya', 22);
(5, 'Rohan', 20);
(6, 'Sneha', 21);
(7, 'Karan', 23);

================================================================
3 - Demonstrate to INSERT, UPDATE, and DELETE, Records in Table.
================================================================
-- Insert records
INSERT INTO student VALUES (11, 'Arjun', 21);
INSERT INTO student VALUES (12, 'Meena', 20);
-- Update record
UPDATE student
SET age = 22
WHERE id = 1;
-- Delete record
DELETE FROM student
WHERE id = 2;
-- Save changes
COMMIT;
-- Display table
SELECT * FROM student;

==================================================================================
4 - Demonstrate to Alter Table (Add Column, Delete Column, Rename, Modify Column).
==================================================================================
-- Add column
ALTER TABLE student
ADD email VARCHAR2(50);
-- Modify column
ALTER TABLE student
MODIFY name VARCHAR2(100);
-- Rename column
ALTER TABLE student
RENAME COLUMN email TO student_email;
-- Delete column
ALTER TABLE student
DROP COLUMN student_email;
-- Display table structure
DESC student;

=================================================================
5 - Demonstrate to SELECT with clauses (Simple and Parameterize).
=================================================================
-- Simple SELECT
SELECT * FROM student;
SELECT name, age FROM student;
-- WHERE clause
SELECT * FROM student
WHERE age > 20;
-- ORDER BY clause
SELECT * FROM student
ORDER BY age ASC;
-- GROUP BY clause
SELECT age, COUNT(*)
FROM student
GROUP BY age;
-- WHERE with AND condition
SELECT * FROM student
WHERE age > 20 AND name LIKE 'A%';

=======================================================================
6 - Demonstrate: i. WHERE Clause ii. GROUP BY clause iii. HAVING Clause
=======================================================================
-- WHERE Clause
SELECT * FROM student
WHERE age > 20;
-- GROUP BY Clause
SELECT age, COUNT(*) AS total_students
FROM student
GROUP BY age;
-- HAVING Clause
SELECT age, COUNT(*) AS total_students
FROM student
GROUP BY age
HAVING COUNT(*) > 1;

=============================================================================================
7 - Demonstrate integrity constraints: PRIMARY KEY, FOREIGN KEY, CHECK, NOT NULL, and DEFAULT
=============================================================================================
-- Create Department table
CREATE TABLE department (
 dept_id NUMBER PRIMARY KEY,
 dept_name VARCHAR2(50) NOT NULL
);
-- Create Student table with constraints
CREATE TABLE student (
 id NUMBER PRIMARY KEY,
 name VARCHAR2(50) NOT NULL,
 age NUMBER CHECK (age >= 18),
 city VARCHAR2(50) DEFAULT 'Shahada',
 dept_id NUMBER,
 FOREIGN KEY (dept_id) REFERENCES department(dept_id)
);
-- Insert records in department
INSERT INTO department VALUES (1, 'Computer');
INSERT INTO department VALUES (2, 'IT');
-- Insert records in student
INSERT INTO student (id, name, age, dept_id) VALUES (1, 'Rahul', 20, 1);
(2, 'Neha', 19, 2);
(3, 'Amit', 22, 1);
-- Save changes
COMMIT;


==================================================================================
8 - Demonstrate use of operators.
==================================================================================
-- Arithmetic Operator
SELECT id, name, age, age + 2 AS future_age
FROM student;
-- Comparison Operator
SELECT * FROM student
WHERE age >= 21;
-- Logical Operators
SELECT * FROM student
WHERE age > 20 AND name LIKE 'A%';
SELECT * FROM student
WHERE age < 20 OR name LIKE 'P%';
-- NOT Operator
SELECT * FROM student
WHERE NOT age = 20;
-- BETWEEN Operator
SELECT * FROM student
WHERE age BETWEEN 20 AND 22;
-- IN Operator
SELECT * FROM student
WHERE name IN ('Rahul', 'Neha');
-- LIKE Operator
SELECT * FROM student
WHERE name LIKE 'R%';

==================================================================================
9 - Demonstrate joins (Inner joins, Equi, Non Equi, Self-join & Outer Joins).
==================================================================================
-- Create tables
CREATE TABLE department (
 dept_id NUMBER PRIMARY KEY,
 dept_name VARCHAR2(50)
);
CREATE TABLE student (
 id NUMBER PRIMARY KEY,
 name VARCHAR2(50),
 age NUMBER,
 dept_id NUMBER
);
-- Insert data (Oracle style)
INSERT INTO department VALUES (1, 'Computer');
INSERT INTO department VALUES (2, 'IT');
INSERT INTO department VALUES (3, 'Mechanical');
INSERT INTO student VALUES (1, 'Rahul', 20, 1);
INSERT INTO student VALUES (2, 'Amit', 21, 2);
INSERT INTO student VALUES (3, 'Neha', 22, 1);
INSERT INTO student VALUES (4, 'Pooja', 20, NULL);
COMMIT;
-- INNER JOIN
SELECT s.name, d.dept_name
FROM student s
INNER JOIN department d
ON s.dept_id = d.dept_id;
-- EQUI JOIN
SELECT s.name, d.dept_name
FROM student s, department d
WHERE s.dept_id = d.dept_id;
-- SELF JOIN
SELECT A.name AS Student1, B.name AS Student2
FROM student A, student B
WHERE A.dept_id = B.dept_id AND A.id <> B.id;
-- NON-EQUI JOIN
SELECT s.name, s.age, d.dept_name
FROM student s, department d
WHERE s.age > d.dept_id;
-- LEFT OUTER JOIN
SELECT s.name, d.dept_name
FROM student s
LEFT OUTER JOIN department d
ON s.dept_id = d.dept_id;
-- RIGHT OUTER JOIN
SELECT s.name, d.dept_name
FROM student s
RIGHT OUTER JOIN department d
ON s.dept_id = d.dept_id;

========================================
10 - Demonstrate the use of Sub-Queries.
========================================
-- Example 1: Single-row Sub-query
SELECT name, age
FROM student
WHERE age = (SELECT MAX(age) FROM student);
-- Example 2: Multiple-row Sub-query
SELECT name
FROM student
WHERE dept_id IN (SELECT dept_id FROM department);
-- Example 3: Sub-query with comparison
SELECT name, age
FROM student
WHERE age > (SELECT AVG(age) FROM student);
-- Example 4: Sub-query in SELECT clause
SELECT name, age,
 (SELECT AVG(age) FROM student) AS average_age
FROM student;

=============================================================================================
11 - Write down SQL by using i. Aggregate functions ii. Date functions iii. String functions.
=============================================================================================
-- Aggregate Functions
SELECT COUNT(*) AS total_students FROM student;
SELECT AVG(age) AS average_age FROM student;
SELECT MAX(age) AS maximum_age FROM student;
SELECT MIN(age) AS minimum_age FROM student;
-- Date Functions
SELECT SYSDATE AS current_date FROM dual;
SELECT SYSDATE AS current_date_time FROM dual;
-- String Functions
SELECT UPPER(name) AS upper_name FROM student;
SELECT LOWER(name) AS lower_name FROM student;
SELECT LENGTH(name) AS name_length FROM student;
SELECT name || ' - Student' AS full_info FROM student;