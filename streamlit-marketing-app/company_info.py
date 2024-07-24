import streamlit as st

def app():
    st.title('Unternehmensinformationen')

    # Eingabefelder für Unternehmensdaten
    with st.form(key='company_info_form'):
        # Vorab ausgefüllte Daten für Nike
        unternehmensname = st.text_input("Unternehmensname", "Nike, Inc.")
        branche = st.text_input("Branche", "Sportbekleidung und -ausrüstung")
        groesse = st.selectbox(
            "Unternehmensgröße",
            ["Kleinunternehmen", "Mittelständisch", "Großunternehmen"],
            index=2  # Index für "Großunternehmen"
        )

        # Informationen zu USPs und Zielen
        usps = st.text_area(
            "USPs (Unique Selling Points)",
            "Innovative Sportbekleidung, ikonisches Design, hohe Qualität und Nachhaltigkeit."
        )
        
        # Informationen zur Markenpersönlichkeit
        markenpersoenlichkeit = st.text_area(
            "Markenpersönlichkeit und -werte",
            "Sportlich, innovativ, inspirierend und engagiert für soziale Verantwortung."
        )

        # Informationen zu Hauptzielgruppen
        hauptzielgruppen = st.text_area(
            "Hauptzielgruppen des Unternehmens",
            "Sportler und Fitnessbegeisterte, junge Erwachsene und Jugendliche."
        )

        # Informationen zu bevorzugten Content-Formaten (Radio-Buttons)
        content_formate = st.radio(
            "Bevorzugte Content-Formate",
            ["Blogartikel", "Social-Media-Posts"],
            index=0  
        )

        
    
          # Eingabe der wichtigsten Kernbotschaften
        kernbotschaften = st.text_area("Welches Thema soll der Artikel behandeln?")
        
        ziele = st.text_area("Zielsetzungen des Artikels ")
        
        # Informationen zu primären Vertriebskanälen (Radio-Buttons)
        vertriebskanaele = st.radio(
            "Primäre Vertriebskanäle",
            ["Website", "E-Mail", "Social Media", "Messen"]
        )


        # Knopf zum Absenden des Formulars
        submit_button = st.form_submit_button("Unternehmensdaten speichern")

        if submit_button:
            # Speichern der Unternehmensdaten im session_state
            st.session_state['company_data'] = {
                "unternehmensname": unternehmensname,
                "branche": branche,
                "groesse": groesse,
                "usps": usps,
                "ziele": ziele,
                "markenpersoenlichkeit": markenpersoenlichkeit,
                "hauptzielgruppen": hauptzielgruppen,
                "content_formate": content_formate,
                "kernbotschaften": kernbotschaften,
                "vertriebskanaele": vertriebskanaele,
    

            }

            st.success("Unternehmensdaten erfolgreich gespeichert!")

# Dieser Teil ist für Testzwecke, wenn Sie dieses Skript einzeln laufen lassen.
if __name__ == "__main__":
    app()
