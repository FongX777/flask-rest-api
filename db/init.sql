CREATE DATABASE flask_web;
use flask_web;

CREATE TABLE tasks (
  id SERIAL PRIMARY KEY,
  name VARCHAR(20),
  status INTEGER
);
