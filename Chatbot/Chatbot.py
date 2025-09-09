
import streamlit as st
import groq #api

#st.title("pagina chatbot")

#tener nuestros modelos de IA

modelos = ['llama3-8b-8192', 'llama3-70b-8192','mixtral-8x7b-32768']


#funcion para configurar la pagina
def configurar_pagina ():
    st.set_page_config(page_title="Pagina con python",page_icon="🫡")# page_title para cambiar el nombre de la pagina y page icon para el icono
    st.title ("Pagina para el chatbot")                  

#mostrar el sidebar con los modelos
def mostrar_sidebar ():
    st.sidebar.title("Elegi tu IA")
    modelo = st.sidebar.selectbox("Cual elegis?",modelos, index=0)
    st.write(f"Elegiste el modelo:{modelo}")
    return modelo
    

#un cliente groq

def crear_cliente_groq():
    groq_api_key = st.secrets["GROQ_API_KEY"] #almacenar la api key de groq
    return groq.Groq(api_key = groq_api_key)

#INICIALIZAR EL ESTADO DE LOS MENSAJES

def inicializacion_estado_chat():
    if "mensajes" not in st.session_state:
        st.session_state["mensajes"] = []   # lista vacía para iniciar el chat
    
    if "usuario" not in st.session_state:
        st.session_state["usuario"] = None  # o "" si preferís string vacío
    
    if "bot_respuestas" not in st.session_state:
        st.session_state["bot_respuestas"] = []

#muestra mensajes previos


#Historial del chat 

def mostrar_historial ():
    for mensaje in st.session_state.mensaje:
        with st.chat_message(mensaje["role"]): #quien lo envia
            st.markdown(mensaje["content"]) #que envia

#Obtener mensaje de usuario
def obtener_mensaje():
    return st.chat_input("Envia un mensaje", key="chat_input")

#Agregar los mensajes al estado

def agregar_mensaje_historial (role,content):
    st.session_state.mensajes.append({"role":role,"content":content})

#Mostrar los mensajes en pantalla

def mostrar_mensaje (role,content):
    with st.chat_message(role):
        st.markdown (content)
    

# LLAMAR AL MODELO DE GROQ
def obtener_respuesta_modelo(cliente, modelo, mensajes):
    respuesta = cliente.chat.completions.create(
        model=modelo,
        messages=mensajes,
        stream = False
    )
    return respuesta.choices[0].message.content

#flujo de la app

def ejecutar_app():
    configurar_pagina()
    modelo = mostrar_sidebar()
    cliente = crear_cliente_groq()
    #inicializacion_estado_chat
    inicializacion_estado_chat()
    mensaje_usuario = obtener_mensaje()
    obtener_mensaje()

#ejecutar la api
if __name__ == "__main__": #si este archivo es el principal entonces ejecuta
    ejecutar_app()







