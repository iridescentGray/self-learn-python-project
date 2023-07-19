create database test_sqlalchemy;

CREATE TABLE girls (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    age INT,
    address VARCHAR(255)
);

INSERT INTO girls (name, age, address)
VALUES ('小明', 17, '地灵殿'),
('小红', 16, '地灵殿'),
('小白', 19, '魔法森林'),
('小蓝', 60, '雾之湖');