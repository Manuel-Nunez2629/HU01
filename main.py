import insertarDatos
import database
import xml.etree.ElementTree as ET
from database import exportar_a_xml
import http.server
import socketserver
import json

# Crear la base de datos al iniciar la aplicación
database.crear_base_datos()

# Iniciar el servidor web
insertarDatos.procesar_datos_desde_json()
exportar_a_xml()

# Definir el puerto para el servidor
puerto = 8000

# Crear una clase para el manejador de peticiones
class MiHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Exportar datos a XML
        exportar_a_xml()
        # Leer el contenido del XML
        with open("usuarios.xml", "r", encoding='utf-8') as archivo:
            xml_archivo = archivo.read()
        
        # Enviar una respuesta exitosa
        self.send_response(200)
        # Establecer las cabeceras de la respuesta
        self.send_header('Content-type', 'text/xml')
        self.end_headers()
        # Enviar el contenido del XML como respuesta
        self.wfile.write(xml_archivo.encode('utf-8'))

# Configurar el servidor con el manejador de peticiones
with socketserver.TCPServer(('', puerto), MiHandler) as servidor:
    print(f'Servidor web iniciado en el puerto {puerto}.')
    # Entrar en el bucle de servicio
    servidor.serve_forever()