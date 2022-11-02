-- Середня температура в містах на протязі 1980-2013
SELECT c.name, avg(r.temperature) FROM city c
INNER JOIN records r
ON c.id = r.id_city
GROUP BY c.name;

-- Розподіл північних міст на захід/схід
SELECT e.name, COUNT(*) FROM city c
INNER JOIN eastwest e
ON e.id = c.id_eastwest
GROUP BY e.name;

-- Середня температура в місті Рейкявік в залежності від року
SELECT r.year, r.temperature FROM city c
INNER JOIN records r
ON c.id = r.id_city
WHERE c.name = 'Reykjavik'
ORDER BY r.year;
