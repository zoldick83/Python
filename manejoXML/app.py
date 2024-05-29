import xml.etree.ElementTree as ET

xml_file = open('ejemplo.xml')
xml_data = ET.fromstring(xml_file.read())
lista = xml_data.findall('Encabezado')
for listado in lista:
    print(f"Nombre: {listado.find('id_mensaje').text}")
    print(f"Nombre: {listado.find('recaudador').text}")
    print(f".........................................")
