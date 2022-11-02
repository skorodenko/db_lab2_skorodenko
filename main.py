import psycopg2

username = 'skorodenko'
password = '1234321'
database = 'postgres'
host = 'localhost'
port = '5432'

query_1 = '''
SELECT c.name, avg(r.temperature) FROM city c
INNER JOIN records r
ON c.id = r.id_city
GROUP BY c.name;
'''
query_2 = '''
SELECT e.name, COUNT(*) FROM city c 
INNER JOIN eastwest e 
ON e.id = c.id_eastwest 
GROUP BY e.name;
'''
query_3 = '''
SELECT r.year, r.temperature FROM city c 
INNER JOIN records r 
ON c.id = r.id_city
WHERE c.name = 'Reykjavik'
ORDER BY r.year;
'''
queries = [query_1, query_2, query_3]

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    for q in queries:
        cur = conn.cursor()
        cur.execute(q)
        print([i for i in cur])