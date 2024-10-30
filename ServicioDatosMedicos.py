import requests
import json

class ServicioDatosMedicos:
    def __init__(self, fuente="api", url=None, db_conn=None):
        """
        Constructor de la clase ServicioDatosMedicos.
        
        Args:
            fuente (str): Tipo de fuente de datos ("api" o "db").
            url (str): URL del endpoint de la API (si se usa API).
            db_conn (obj): Conexión a la base de datos (si se usa BD).
        """
        self.fuente = fuente
        self.url = url
        self.db_conn = db_conn

    def obtener_datos_medicos(self, parametros=None):
        """
        Obtiene datos médicos de una fuente especificada.

        Args:
            parametros (dict): Parámetros para la consulta de datos (si se usa API).
        
        Returns:
            dict: Datos médicos obtenidos.
        """
        if self.fuente == "api":
            return self._obtener_datos_api(parametros)
        elif self.fuente == "db":
            return self._obtener_datos_db()
        else:
            raise ValueError("Fuente de datos no soportada.")

    def _obtener_datos_api(self, parametros):
        """
        Obtiene datos médicos desde una API.

        Args:
            parametros (dict): Parámetros para la consulta de datos.
        
        Returns:
            dict: Datos médicos obtenidos de la API.
        """
        try:
            response = requests.get(self.url, params=parametros)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener datos de la API: {e}")
            return None

    def _obtener_datos_db(self):
        """
        Obtiene datos médicos desde una base de datos.

        Returns:
            list[dict]: Lista de registros médicos obtenidos de la BD.
        """
        try:
            cursor = self.db_conn.cursor()
            cursor.execute("SELECT * FROM datos_medicos")  # Ajusta la consulta según la estructura de tu BD
            registros = cursor.fetchall()
            return [dict(zip([column[0] for column in cursor.description], row)) for row in registros]
        except Exception as e:
            print(f"Error al obtener datos de la base de datos: {e}")
            return None
