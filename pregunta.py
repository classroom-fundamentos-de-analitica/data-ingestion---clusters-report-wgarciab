"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():

    #
    # Inserte su código aquí
    #

    with open("clusters_report.txt", mode='r') as clusters_report, open("clean_report.txt", mode='w') as clean_report:
        header1 = clusters_report.readline()
        header2 = clusters_report.readline()
        cluster = header1[0:9].strip().lower()
        cantidad = (header1[9:25].strip() + " " + header2[9:25].strip()).lower().replace(" ", "_")
        porcentaje = (header1[25:41].strip() + " " + header2[25:41].strip()).lower().replace(" ", "_")
        palabras = header1[41:].strip().lower().replace(" ", "_")
        clean_report.write(cluster + ";" + cantidad + ";" + porcentaje + ";" + palabras + "\n")

        next(clusters_report)
        next(clusters_report)

        while True:
            line = clusters_report.readline()

            if not line:
                break

            if (line.strip(" ") == "\n"):
                clean_report.write(cluster + ";" + cantidad + ";" + porcentaje + ";" + palabras + "\n")

            elif not (line[0:9].isspace()):
                cluster = line[0:9].strip()
                cantidad = line[9:25].strip()
                porcentaje = line[25:41].strip().replace(" %", "").replace(",", ".")
                palabras = line[41:].strip()
                palabras = ' '.join(palabras.split())

            else:
                palabras = palabras + " " + line.strip().replace(".", "")
                palabras = ' '.join(palabras.split())

    df = pd.read_table("clean_report.txt", header = 0, sep = ';')

    return df

print(ingest_data())