import psycopg2

try:
    connection=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='1234',
        database='Vectores'
    )
    print('Se realizo con exito la conexion')

except Exception as ex:
    print(ex)

finally:
    connection.close()
    print('Conexion finalizada')