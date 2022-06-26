import mysql.connector

midb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '28232410',
    database = 'prueba'
)

cursor = midb.cursor()

cursor.execute('select * from Usuario')
#cursor.execute('show create table Usuario') #! estructura de la tabla


# resultado2 = cursor.fetchone() # ! primer usuario 
# print(resultado)
# print(resultado2)

# cursor.execute(sql,values)
# midb.commit() #! ejecutara la consulta de sql contra la base de datos
#print(cursor.rowcount)

#------------------------------------------
#listar datos mostrar
cursor.execute('select * from Usuario')
resultado = cursor.fetchall() # todos los usarios
print(resultado)

#listar datos limitado mostrar
cursor.execute('select * from Usuario limit 1')
resultado = cursor.fetchall() # todos los usarios
print(resultado)

# ver definiciones de la tabla
cursor.execute('show create table Usuario') 

# insertar datos
sql = 'insert into Usuario(email,username, edad) values(%s,%s,%s)'
values = ('leo@gmail.com','leo514',45)

# actualizar datos
sql = 'update Usuario set email = %s where id = %s'
values = ('jeancar5154@gmail.com',5)
cursor.execute(sql,values)

midb.commit()

print(cursor.rowcount)

#eliminar datos
sql = 'delete from Usuario where id = %s'
values = (5,) # cuando hay un solo valor se coloca asi
cursor.execute(sql,values)
midb.commit()