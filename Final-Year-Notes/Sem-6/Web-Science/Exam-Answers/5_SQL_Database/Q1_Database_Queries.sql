-- SQL Database Setup & Queries - Slip 7 Q1

CREATE TABLE Emp (
  eno INT PRIMARY KEY, name VARCHAR(50), dno INT, salary DECIMAL(10,2)
);

CREATE TABLE Project (
  pno INT PRIMARY KEY, pname VARCHAR(50), control_dno INT, budget DECIMAL(10,2)
);

CREATE TABLE Works_On (
  eno INT, pno INT, hours_worked INT, PRIMARY KEY(eno,pno),
  FOREIGN KEY(eno) REFERENCES Emp(eno), FOREIGN KEY(pno) REFERENCES Project(pno)
);

-- Insert data
INSERT INTO Emp VALUES (1,'John',101,50000), (2,'Jane',102,60000), (3,'Bob',101,55000);
INSERT INTO Project VALUES (1,'WebApp',101,25000), (2,'MobileApp',102,30000), (3,'BigData',101,50000);
INSERT INTO Works_On VALUES (1,1,100), (2,2,120), (3,1,80);

-- Queries
-- Q1: Project budget > 10000
SELECT pname FROM Project WHERE budget > 10000;

-- Q2: Projects controlled by dno 101
SELECT pname FROM Project WHERE control_dno = 101;

-- Q3: Second max budget
SELECT * FROM Project WHERE budget = (SELECT MAX(budget) FROM Project WHERE budget < (SELECT MAX(budget) FROM Project));

-- Q4: Max budget
SELECT * FROM Project ORDER BY budget DESC LIMIT 1;

-- Q5: Employees in E&TC dept
SELECT e.name FROM Emp e WHERE e.dno = 101;