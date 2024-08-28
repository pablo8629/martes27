#datos para la conexion de la   base de datos
dataBase ="gestordb"
userName = "root"
userPassword = ""
Connectionport =3306
server = "localhost"


#creando la conexion de datos
dataBaseConection=f"mysql+mmysqlconnector://{userName}:{userPassword}@{server}:{Connectionport}/{dataBase}"

print(dataBaseConection)


