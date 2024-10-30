# Ejemplo con API
api_service = ServicioDatosMedicos(fuente="api", url="https://api.example.com/datos_medicos")
datos = api_service.obtener_datos_medicos(parametros={"id_paciente": 123})

# Ejemplo con Base de Datos
import sqlite3  # Usar la librería de tu base de datos
conn = sqlite3.connect("nombre_base_datos.db")
db_service = ServicioDatosMedicos(fuente="db", db_conn=conn)
datos = db_service.obtener_datos_medicos()
