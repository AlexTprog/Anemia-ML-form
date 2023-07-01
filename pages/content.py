import streamlit as st

st.set_page_config(page_title="Anemia en el Peru ", page_icon="🩸")

st.markdown(
    """
            # Anemia en el Peru 🩸
            
            La anemia es una afección muy común que puede ser causada por diferentes factores, pero una de las principales causas es la falta de hierro en la dieta. El hierro es esencial para la producción de glóbulos rojos saludables, por lo que una falta de hierro puede llevar a la anemia. Además de la falta de hierro, otras causas comunes de anemia incluyen pérdida de sangre y enfermedades que afectan la capacidad del cuerpo para absorber hierro, como la enfermedad celíaca y la enfermedad de Crohn.                        
            """
)

col1, col2 = st.columns(2)

st.image(
    image="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Flive.staticflickr.com%2F4436%2F36449801804_cbdcdae945_b.jpg&f=1&nofb=1&ipt=3d11f744cecd3885ea49b18cef0cb3baf711ab0267d1a0e0f0ad3242acaada62&ipo=images",
)

st.markdown(
    """
        Estudios previos han identificado características como la condición socioeconómica, los hábitos nutricionales y el historial de vacunación como factores importantes en la detección de la enfermedad. No obstante, es importante tener en cuenta que existen limitaciones en la obtención de datos precisos y en la aplicación de árboles de decisión para el diagnóstico de anemia.
    """,
)



