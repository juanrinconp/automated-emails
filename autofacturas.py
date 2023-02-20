import yagmail
import pandas as pd
import datetime
import time

while True:
    if datetime.datetime.now().hour == 10 and datetime.datetime.now().minute == 27:
        df = pd.read_excel('lista.xlsx')

        for index, row in df.iterrows():
            email = yagmail.SMTP(user="info@xxxxxxxx.net", password="xxxxxxxxxxx")
            email.send(to=row['email'],
                       subject=f"Factura Conserjeria {row['mes']}",
                       contents=f"Buenos dias estimados señores del {row['nombre']}, me permito enviarles la factura del servicio de conserjeria para el mes de {row['mes']}. Quedo pendiente a cualquier duda o inquietud. \n\n Atentemente,  \n \n Marcela Cobo \n Gerente Administrativa \n 3118945134",
                       attachments=[f"{row['factura']}.txt" , "contacts.csv"])
            print("Correos Enviados!")
    time.sleep(60)


