'''
Project Description.

Whenever you’re tackling a new project, it can be tempting to dive right into writing code. 
But more often than not, it’s best to take a step back and consider the bigger picture. 
I recommend first drawing up a high-level plan for what your program needs to do. 
Don’t think about the actual code yet—you can worry about that later. Right now, stick to broad strokes.

For example, your phone and email address extractor will need to do the following:

- Get the text off the clipboard.
- Find all phone numbers and email addresses in the text.
- Paste them onto the clipboard.

Now you can start thinking about how this might work in code. The code will need to do the following:

- Use the pyperclip module to copy and paste strings.
- Create two regexes, one for matching phone numbers and the other for matching email addresses.
- Find all matches, not just the first match, of both regexes.
- Neatly format the matched strings into a single string to paste.
- Display some kind of message if no matches were found in the text.
'''

import re, pyperclip


phone = re.compile(r'\d{3}\s?\d{4}')

mail = re.compile(r'(\w+@\w+\.\w+(\.\w+)?)')

phoneR = phone.findall(pyperclip.paste())

mailR = mail.findall(pyperclip.paste())

print(phoneR)
print(mailR)

'''
Example text, copy it before launching the script

Contáctenos
Usted puede formular peticiones, quejas, reclamos, sugerencias y denuncias (PQRSD),
 relacionados con la gestión o con temas de competencia del Departamento.
 
Nos puede contactar a través de los siguientes canales de atención:
 
Presencial: En nuestras oficinas ubicadas en la ciudad de Bogotá en la Carrera 6 No 12-62, 
en jornada continua de lunes a viernes de 7:30 a.m. a 6:00 p.m. 
para el Grupo de Servicio al Ciudadano Institucional y en las demás dependencias de la Entidad de 8:00 a.m a 5:30 p.m.
Igualmente por el correo electrónico: presencial@funcionpublica.gov.co
 

Telefónico: A través del PBX (57+1) 739 5656 opción 3, 
Línea Gratuita Nacional 018000 917770 de lunes a viernes en horario de 8:00 a.m. a 5:00 p.m.

 

Mesa de ayuda SIGEP: PBX (57+1) 7395656 opción 2.

Mesa de ayuda SUIT: PBX (57+1) 7395656 opción 1. 

 

Virtual: Chat EVA, ingresando a nuestro portal www.funcionpublica.gov.co, 
opción "Chat Virtual", de lunes a viernes en horario de 8:00 a.m. a 5:00 p.m.
 Facebook: Departamento Administrativo de la Función Pública. Twitter: @DAFP_COLOMBIA
Igualmente por el correo electrónico: virtual@funcionpublica.gov.co
 

Escrito: A través de la ventanilla de recepción de documentos ubicada en la carrera 6 No.
 12-62, 4to piso, se podrán radicar en forma física o a través de correo postal las peticiones, 
 quejas, reclamos, sugerencias y denuncias por actos de corrupción en jornada continua de 8:00 a.m. a 4:00 p.m.

 

Igualmente por el correo electrónico: eva@funcionpublica.gov.co,
 o diligenciando el "Formulario de PQRS"
  disponible en nuestro portal www.funcionpublica.gov.co, 
  en el siguiente enlace: Servicio al Ciudadano "Formule su PQRS". 

 

También puede enviar sus peticiones a través del  FAX: (57+1) 7395657.
'''