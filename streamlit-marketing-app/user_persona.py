import streamlit as st

def app():
    st.title('Erstellung einer User Persona')

    # Eingabefelder für grundlegende Informationen der User Persona
    with st.form(key='user_persona_form'):
        name = st.text_input("Name der Persona")
        alter = st.slider("Alter", 18, 90, 20)  # Min, Max, Default
        geschlecht = st.radio("Geschlecht", ["Männlich", "Weiblich", "Diverse"])
        standort = st.text_input("Standort")

        # Psychografische Daten
        interessen = st.text_area("Was sind Interessen und Hobbys?")
        werte = st.text_area("Welche Werte sind wichtig?")
        beruf = st.radio("Bildungsgrad",["Angestellter", "Selbstständig", "Student", "in der Ausbildung", "Schüler"])

        # Verhaltensdaten
        nutzung_sozialer_medien = st.markdown("Welche Social Media Plattformen wird regelmäßig genutzt?")
        instagram = st.checkbox("Instagram")
        facebook = st.checkbox("Facebook")
        tiktok = st.checkbox("TikTok")
        twitter = st.checkbox("Twitter")
        linkedin = st.checkbox("LinkedIn")
        pinterest = st.checkbox("Pinterest")
        snapchat = st.checkbox("Snapchat")

        markenpraferenzen = st.text_area("Gebe 2 Lieblingsmarken ein")

        

    
        content_vorlieben = st.multiselect(
            "Wähle deine Vorlieben für Arten von Inhalten aus:",
            options=["Videos", "Fotos", "Texte", "Podcasts", "Infografiken"]
        )

        # Knopf zum Absenden des Formulars
        submit_button = st.form_submit_button("User Persona erstellen")

        if submit_button:
            # Speichern der Persona-Daten im session_state
            st.session_state['persona_data'] = {
                "name": name,
                "alter": alter,
                "geschlecht": geschlecht,
                "standort": standort,
                "interessen": interessen,
                "werte": werte,
                "beruf": beruf,
                "nutzung_sozialer_medien": {
                    "Instagram": instagram,
                    "Facebook": facebook,
                    "TikTok": tiktok,
                    "Twitter": twitter,
                    "LinkedIn": linkedin,
                    "Pinterest": pinterest,
                    "Snapchat": snapchat,
                "markenpraferenzen": markenpraferenzen,
                "content_vorlieben": content_vorlieben,
                },
               
            }

            st.success("User Persona wurde erstellt!")

# Dieser Teil ist für Testzwecke, wenn Sie dieses Skript einzeln laufen lassen.
if __name__ == "__main__":
    app()

