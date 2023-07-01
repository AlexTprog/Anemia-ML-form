from math import e
from joblib import load
import pandas as pd
import streamlit as st

MODEL = load("./data/model/modelo_entrenado.joblib")
ANEMIATYPE = {
    0: "Normal",
    1: "Anemia Leve",
    2: "Anemia Moderada",
    3: "Anemia Severa",
}

st.set_page_config(page_title="Prediccion de Anemia", page_icon="💉")


st.markdown("# Prediccion de Anemia 💉")

st.markdown(
    """
            El formulario hace uso de un modelo predictivo entrenado usando datos proporcionados por la Dirección de Redes Integradas de Salud (DIRIS)."""
)

with st.form(key="form_anemia"):
    age = st.number_input(
        label="Ingrese la edad del menor en meses",
        min_value=1,
        max_value=60,
        step=1,
    )

    hbgbn = st.number_input(
        label="Indique su nivel de Hemoglobina (g/dl)?",
        min_value=0.0,
        max_value=20.0,
        step=0.1,
    )

    pg_juntos = st.selectbox(
        label="Es beneficiario de juntos?",
        options=("Si", "No"),
    )
    pg_sis = st.selectbox(
        label="Esta inscrito en SIS?",
        options=("Si", "No"),
    )
    pg_qwrm = st.selectbox(
        label="Esta inscrito en Qaliwarma?",
        options=("Si", "No"),
    )

    spltmc = st.selectbox(
        label="Cuenta con suplementacion alimentica?",
        options=("Si", "No"),
    )

    cnsj = st.selectbox(
        label="Ha recibido consejeria?",
        options=("Si", "No"),
    )

    sexo = st.selectbox(
        label="Indique su sexo",
        options=("M", "F"),
    )

    input_form = {
        "EdadMeses": int(age),
        "Juntos": 1 if pg_juntos == "Si" else 0,
        "SIS": 1 if pg_sis == "Si" else 0,
        "Qaliwarma": 1 if pg_qwrm == "Si" else 0,
        "Hemoglobina": hbgbn,
        "Suplementacion": 1 if spltmc == "Si" else 0,
        "Consejeria": 1 if cnsj == "Si" else 0,
        "Sexo_M": sexo == "M",
    }

    submit_button = st.form_submit_button(label="Predecir")

    if submit_button:
        input_form = pd.DataFrame(input_form, index=[0])
        result = MODEL.predict(input_form)[0]

        if hbgbn > 5 and hbgbn <= 10:
            result = 2

        if hbgbn <= 5:
            result = 3

        if result == 0:
            st.balloons()
            st.success(f"Estado: {ANEMIATYPE[result]}", icon="✅")
        elif result == 1 or result == 2:
            st.warning(f"Estado: {ANEMIATYPE[result]}", icon="⚠️")
        elif result == 3:
            st.error(f"Estado: {ANEMIATYPE[result]}", icon="🚨")
