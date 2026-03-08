-- View dataset
SELECT * 
FROM financial_data;

-- Total budget vs actual
SELECT 
    SUM(budget) AS total_budget,
    SUM(actual) AS total_actual
FROM financial_data;

-- Department spending analysis
SELECT 
    department,
    SUM(budget) AS department_budget,
    SUM(actual) AS department_actual,
    SUM(actual - budget) AS variance
FROM financial_data
GROUP BY department;

-- Monthly financial performance
SELECT
    month,
    SUM(budget) AS total_budget,
    SUM(actual) AS total_actual
FROM financial_data
GROUP BY month
ORDER BY month;

-- Departments exceeding budget
SELECT
    department,
    SUM(actual - budget) AS overspend
FROM financial_data
GROUP BY department
HAVING overspend > 0;