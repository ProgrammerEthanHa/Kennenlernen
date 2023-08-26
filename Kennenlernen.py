import streamlit as st
import pandas as pd
import altair as alt

st.header("Wo lernen die Deutschen ihre Freunde kennen?")
st.subheader("")

source = pd.DataFrame({
        'Anteil(%)': [41, 19, 19, 17, 16, 16, 15, 15, 14, 13, 11, 9, 8, 4, 28],
        'Ort/Zeit': ['Arbeit', 'Weiterführende Schule', 'Ausbildung/ Berufsschule', 'Grundschule', 'Hobbies', 'Im Alltag', 'Verein', 'Beim Feiern', 'Studium', 'über soziales Netzwerk', 'Urlaub', 'Kindergarten', 'Ehrenamt', 'Krabbelgruppe', 'Andere Situation']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil(%):Q',
        x='Ort/Zeit:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Basis n=2004 Befragte; 18 - 69 Jahre in Deutschland; 2022 (Mehrfachnennung möglich)
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: SINUS-Institut/YouGov")