CREATE DATABASE web;
use web;

CREATE TABLE tasks (
  id SERIAL PRIMARY KEY,
  name VARCHAR(20),
  status INTEGER
);
