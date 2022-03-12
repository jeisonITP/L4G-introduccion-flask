from smtplib import SMTP
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content('Este es un mensaje de pruebas')

msg['Subject'] = 'Asunto de prueba'
msg['From'] = "jacalvached17m@itp.edu.co"
msg['To'] = "jacalvached17m@itp.edu.co"

# Reemplaza estos valores con tus credenciales de Google Mail
username = 'jacalvached17m@itp.edu.co'
password = ''

server = SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.send_message(msg)

server.quit()