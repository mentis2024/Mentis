import streamlit as st
import random

# Funzione per il gioco
def guessing_game():
    # Numero casuale tra 1 e 10
    secret_number = random.randint(1, 10)

    # Titolo del gioco
    st.title("🎮 Gioco Interattivo: Indovina il numero! 🎲")
    st.write("Ho scelto un numero tra 1 e 10. Riuscirai a indovinarlo?")

    # Input dell'utente
    user_guess = st.number_input("Inserisci un numero (1-10):", min_value=1, max_value=10, step=1)

    if st.button("Indovina!"):
        if user_guess == secret_number:
            st.success(f"Congratulazioni! Hai indovinato il numero {secret_number}.")
        else:
            st.error(f"Ops! Il numero era {secret_number}. Riprova!")

    # Pulsante con icona del cervello per andare alla pagina dei bot
    if st.button("🧠 Vai alla pagina con i Bot"):
        st.experimental_rerun()  # Questo ricarica la pagina, quindi la logica di navigazione deve essere gestita tramite url o sessione.

# Funzione per la pagina dei bot
def bot_page():
    st.title("💬 Chatbot di Supporto Psicologico")
    st.write("Benvenuto nel sistema di supporto psicologico con i nostri bot. Siamo qui per aiutarti!")

    # Qui va il tuo codice dei bot che gestisce la conversazione.

# Funzione principale di Streamlit per gestire la navigazione
def main():
    st.set_page_config(page_title="Gioco Interattivo", page_icon="🎮", layout="centered")

    # Verifica la pagina corrente
    page = st.sidebar.radio("Vai alla pagina:", ["Gioco Interattivo", "Bot di Supporto"])

    if page == "Gioco Interattivo":
        guessing_game()
    elif page == "Bot di Supporto":
        bot_page()

# Esegui la funzione principale
if __name__ == "__main__":
    main()