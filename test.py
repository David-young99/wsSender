import pywhatkit
import datetime
import pytz

def button_main():
        now = datetime.datetime.now()
        now_cr = datetime.datetime.now(pytz.timezone("America/Costa_Rica"))
        

        hour_cu = now.hour
        min = now.minute
        min_mod = min + 1

        hour_cr = now_cr.hour
        min_cr = now_cr.minute
        sec_cr = now_cr.second

        

        user = "David Young"
        email = "david@email.com"
        alert = "Alerta por inundacion"
        details = "En los sectores de Turrialba centro"

        msg = "Alerta enviada automáticamente por el usuario: " + user + " de email: " + email + " ,Tipo de alerta: " + alert + " ,mas detalles " + details + " . Alerta generada a las " + str(hour_cr) + "h : " + str(min_cr) + "min : " + str(sec_cr) + "sec Hora de Costa Rica"

        #str(name) + str(emaill) + str(disaster) + str(message)

        pywhatkit.sendwhatmsg_to_group(
                "KShmZDAcfxFCdDbEjCIgs1",
                msg,
                hour_cu,
                min_mod, 
                20)
try:
    button_main()
except:
    print("Intentando nuevamente...")
    button_main()

