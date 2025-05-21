import mysql.connector
connection=mysql.connector.connect(host='localhost',user='root',password='varsha',database='grocery')
def get_uoms(connection):
    cursor = connection.cursor()
    query = ("select * from uom")
    cursor.execute(query)
    response = []
    for (uom_id, uom_name) in cursor:
        response.append({
            'uom_id': uom_id,
            'uom_name': uom_name
        })
    return response

print(get_uoms(connection))
