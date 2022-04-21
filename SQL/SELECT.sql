-- Create school database to store our data (tables)
DROP DATABASE IF EXISTS `school`;
CREATE DATABASE `school`;
USE `school`;

-- Create a table for students
CREATE TABLE `students` (
  `student_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `gender` varchar(20) NOT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- add data entries (rows) in our students table
INSERT INTO students VALUES (1, 'Henry', 'henry@gmail.com', "Male");
INSERT INTO students VALUES (2, 'Annie', 'annie@gmail.com', "Femle");
INSERT INTO students VALUES (3, 'Leon', 'leon@gmail.com', "Male");
INSERT INTO students VALUES (4, 'Charlie', 'charlie@gmail.com', "Male");

SELECT student_name, student_email
FROM school
WHERE gender = "Male"