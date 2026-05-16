import random
import streamlit as st

# ====== Datos de identidad ======
NOMBRE_APP = "📚 MathLife Tutor"
AUTORA = "Magíster Carmen Alvis"
MISION = "Inspirar y guiar a estudiantes de secundaria para que descubran cómo las matemáticas se aplican en su vida diaria, desarrollando habilidades de razonamiento, resolución de problemas y pensamiento crítico de forma divertida e interactiva."
VISION = "Convertirse en la plataforma educativa más accesible y motivadora para jóvenes, donde las matemáticas dejen de ser abstractas y se conviertan en una herramienta práctica para tomar decisiones y entender el mundo."

# ====== Generadores de problemas ======
def problema_descuento():
    precio = random.randint(20, 100)
    descuento = random.choice([10, 15, 20, 25, 30])
    impuesto = random.choice([5, 8, 10])
    precio_desc = precio * (1 - descuento/100)
    precio_final = precio_desc * (1 + impuesto/100)
    return (f"Una chaqueta cuesta ${precio} con un {descuento}% de descuento "
            f"y un impuesto del {impuesto}%. ¿Cuánto pagarías al final?",
            precio_final,
            f"Paso 1: Precio con descuento = {precio} × (1 - {descuento}/100) = {precio_desc:.2f}\n"
            f"Paso 2: Precio final con impuesto = {precio_desc:.2f} × (1 + {impuesto}/100) = {precio_final:.2f}\n"
            f"Respuesta: ${precio_final:.2f}")

def problema_receta():
    personas = random.randint(2, 6)
    tazas = random.randint(1, 3)
    objetivo = random.randint(8, 15)
    tazas_necesarias = tazas * objetivo / personas
    return (f"Una receta para {personas} personas necesita {tazas} tazas de arroz. "
            f"Si quieres cocinar para {objetivo} personas, ¿cuántas tazas necesitas?",
            tazas_necesarias,
            f"Paso 1: Relación = {tazas} / {personas} = {tazas/personas:.2f} tazas por persona\n"
            f"Paso 2: Multiplicamos por {objetivo} personas = {tazas_necesarias:.2f} tazas\n"
            f"Respuesta: {tazas_necesarias:.2f} tazas")

def problema_velocidad():
    distancia = random.randint(80, 150)
    tiempo = random.randint(1, 3) + random.choice([0.5, 1.0, 1.5])
    velocidad = distancia / tiempo
    objetivo = random.randint(200, 400)
    tiempo_objetivo = objetivo / velocidad
    return (f"Un autobús recorre {distancia} km en {tiempo} horas. "
            f"Si mantiene la misma velocidad, ¿cuánto tardará en recorrer {objetivo} km?",
            tiempo_objetivo,
            f"Paso 1: Velocidad = {distancia} / {tiempo} = {velocidad:.2f} km/h\n"
            f"Paso 2: Tiempo para {objetivo} km = {objetivo} / {velocidad:.2f} = {tiempo_objetivo:.2f} horas\n"
            f"Respuesta: {tiempo_objetivo:.2f} horas")

# Lista de generadores
generadores = [problema_descuento, problema_receta, problema_velocidad]

# ====== Interfaz con Streamlit ======
st.set_page_config(page_title=NOMBRE_APP, page_icon="📚")

# Encabezado
st.title(NOMBRE_APP)
st.markdown(f"**Autora:** {AUTORA}")
st.markdown(f"**Misión:** {MISION}")
st.markdown(f"**Visión:** {VISION}")
st.markdown("---")

# Estado inicial
if "problema" not in st.session_state:
    st.session_state.problema, st.session_state.respuesta_correcta, st.session_state.solucion = random.choice(g