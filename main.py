import streamlit as st
from st_pages import Page, show_pages, add_page_title



show_pages(
    [
        Page("./pages/present.py", "Integrantes", "💻"),
        Page("./pages/content.py", "Introduccion", "🏥"),
        Page("./pages/predict.py", "Prediccion de anemia", "💉"),
    ]
)
