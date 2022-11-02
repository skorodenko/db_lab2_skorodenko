import psycopg2
import matplotlib.pyplot as plt

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
    cur = conn.cursor()
    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)

    cur.execute(query_1)
    cities = []
    avg_temp = []
    for row in cur:
        cities.append(row[0])
        avg_temp.append(row[1])    
    bar_ax.bar(cities, avg_temp, width=0.5)

    cur.execute(query_2)
    labels = []
    count = []
    for row in cur:
        labels.append(row[0])
        count.append(row[1])
    pie_ax.pie(count, labels=labels)

    cur.execute(query_3)
    year = []
    temp = []
    for row in cur:
        year.append(row[0])
        temp.append(row[1])
    graph_ax.plot(year, temp, marker='o')

plt.show()
