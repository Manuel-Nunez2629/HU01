import sqlite3
import xml.etree.ElementTree as ET


# Crear la base de datos y la tabla de usuarios
def crear_base_datos():
    conexion = sqlite3.connect('database.db')
    cursor = conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                      (nombre TEXT, edad INTEGER, extranjero INTEGER)''')
    cursor.close()
    conexion.close()

# Insertar usuarios en la base de datos
def insertar_usuarios(usuarios):
    conexion = sqlite3.connect('database.db')
    cursor = conexion.cursor()
    for usuario in usuarios:
        nombre = usuario['nombre']
        edad = usuario['edad']
        extranjero = int(usuario['extranjero'])
        cursor.execute("INSERT INTO usuarios (nombre, edad, extranjero) VALUES (?, ?, ?)",
                       (nombre, edad, extranjero))
    conexion.commit()
    cursor.close()
    conexion.close()

# Obtener todos los usuarios de la base de datos
def obtener_usuarios():
    conexion = sqlite3.connect('database.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    cursor.close()
    conexion.close()
    return usuarios


def exportar_a_xml():
    conexion = sqlite3.connect('database.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios")
    resultados = cursor.fetchall()
    print(f'va bien')
    root = ET.Element("Usuarios")
    for fila in resultados:
        usuario = ET.SubElement(root, "Usuario")
        ET.SubElement(usuario, "Nombre").text = fila[0]
        ET.SubElement(usuario, "Edad").text = str(fila[1])
        ET.SubElement(usuario, "Extranjero").text = str(fila[2])
        
    print(f'va bien')
    tree = ET.ElementTree(root)
    tree.write("usuarios.xml", encoding='utf-8', xml_declaration=True)
    print(f'va bien')

    cursor.close()
    conexion.close()


