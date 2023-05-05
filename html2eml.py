import os
import sys
import argparse
import email.utils
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Definir los argumentos de línea de comando
parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="Archivo HTML de entrada")
args = parser.parse_args()

# Leer el archivo HTML de entrada
with open(args.input_file, "r") as f:
    html = f.read()

# Crear el mensaje de correo electrónico
msg = MIMEMultipart()
msg["To"] = "%To%"
msg["From"] = "%To_Name%"
msg["Subject"] = "Envio"
msg["Date"] = email.utils.formatdate(localtime=True)

# Añadir el archivo HTML como parte del mensaje
html_part = MIMEText(html, "html")
msg.attach(html_part)

# Guardar el mensaje como archivo EML
output_file = os.path.splitext(args.input_file)[0] + ".eml"
with open(output_file, "w") as f:
    f.write(msg.as_string())

print("Archivo EML creado con éxito.")
