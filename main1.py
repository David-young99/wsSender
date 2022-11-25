import pywhatkit
import datetime
from google.protobuf import message
import streamlit as st

def button_main():
    try:
        now = datetime.datetime.now()

        hour_cu = now.hour
        min = now.minute

        hour_mod = hour_cu - 6
        min_mod = min + 1
        sec = now.second

        msg ="Alerta generada automáticamente por " "David Young " + "david@email.com " + "Alerta por inundación" + "En los sectores de Turrialba centro " + str(hour_mod) + "h : " + str(min) + "min : " + str(sec) + "sec Hora de Costa Rica"

        #str(name) + str(emaill) + str(disaster) + str(message)

        pywhatkit.sendwhatmsg_to_group(
                "KShmZDAcfxFCdDbEjCIgs1",
                msg,
                hour_cu,
                min_mod, 
                20)
         

    except:
        print("Intentando nuevamente...")
        button_main()
    

st.title("Complete la información sobre la alerta que desea enviar")
st.subheader("Atención, recuerde que este formulario es únicamente para alertas de emergencia, los datos se enviarán al grupo de whatsapp de los líderes comunitarios y gestores de riesgo")
st.subheader("Introduzca los datos solicitados en la parte inferior: ")


with st.form("Myform1", clear_on_submit=True):
    name = st.text_input("Introduzca el nombre del emisor de la alerta:")
    emaill = st.text_input("introduzca su correo electrónico")
    disaster = st.selectbox("Seleccione una opción con base al desastre observado", ["Alerta por deslizamiento", "Alerta por inundación", "Alerta por ambas amenazas"])
    message = st.text_input("Introduzca más detalles sobre la emergencia")


    button = st.form_submit_button("Submit", on_click= button_main)

        
    

