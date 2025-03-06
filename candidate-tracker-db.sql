CREATE TABLE IF NOT EXISTS candidates (
    id INT PRIMARY KEY,
    title TEXT,
    location TEXT,
    hire_flag BOOLEAN
);

CREATE TABLE IF NOT EXISTS jobs (
    id INT PRIMARY KEY,
    ocupation TEXT,
    dateRange TEXT,
    skills TEXT,
    current_job BOOLEAN,
    occupation_title TEXT,
    start_date DATE,
    end_date DATE,
    candidate_id INT REFERENCES candidates(id)
);

CREATE TABLE IF NOT EXISTS education (
    education_id INT PRIMARY KEY,
    title TEXT,
    description TEXT,
    dateRange TEXT,
    candidate_id INT REFERENCES candidates(id)
);
