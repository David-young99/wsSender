import pywhatkit
import datetime

def button_main():
        now = datetime.datetime.now()

        hour_cu = now.hour
        min = now.minute

        hour_mod = hour_cu - 6
        min_mod = min + 1
        sec = now.second

        msg = "Hola" + str(hour_mod) + "h : " + str(min) + "min : " + str(sec) + "sec Hora de Costa Rica"

        #str(name) + str(emaill) + str(disaster) + str(message)

        pywhatkit.sendwhatmsg_to_group(
                "KShmZDAcfxFCdDbEjCIgs1",
                "name",
                hour_cu,
                min_mod, 
                20)
try:
    button_main()
except:
    print("Intentando nuevamente...")
    button_main()

