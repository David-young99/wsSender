
def button():

    print "Content-type: text/html＼n＼n";

    import pywhatkit
    import datetime
    import cgi
    

    form = cgi.FieldStorage()
    name = form.getvalue("Inserte su nombre")







    now = datetime.datetime.now()

    hour_cu = now.hour
    min = now.minute

    hour_mod = hour_cu - 6
    min_mod = min + 1
    sec = now.second

    msg = "    Alerta generada a las " + str(hour_mod) + "h : " + str(min) + "min : " + str(sec) + "sec Hora de Costa Rica"

    pywhatkit.sendwhatmsg_to_group(
            "KShmZDAcfxFCdDbEjCIgs1",
            name,
            hour_cu,
            min_mod, 
            20)

try:
    button()  

except:
    print("Intentando nuevamente...")
    button()