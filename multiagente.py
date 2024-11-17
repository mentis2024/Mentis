import streamlit as st 
from groq import Groq
import re

# Funzione per ottenere una risposta dal modello Groq
def get_groq_response(messages):
    client = Groq(api_key="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")
    completion = client.chat.completions.create(
        model="llama3-8b-8192",  # Modello Groq
        messages=messages,
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )
    response = ""
    for chunk in completion:
        if chunk.choices[0].delta.content:
            response += chunk.choices[0].delta.content
    return response

# Funzione per rilevare segnali di violenza o emergenze
def detect_violence(user_input):
    violence_keywords = ['violenza fisica', 'abuso', 'morte', 'suicidio', 'stalking']
    if any(word in user_input.lower() for word in violence_keywords):
        return True
    return False

# Funzione per geolocalizzare l'utente (simulazione)
def get_user_location():
    location = st.text_input("Per favore, inserisci la tua posizione (città):")
    return location

# Funzione per simulare una chiamata ai soccorsi
def emergency_call(location):
    emergency_response = f"🚨 Chiamata d'emergenza attivata <br>sto inviando una richiesta di soccorso nella tua posizione <br>Piazza Cardinale Pappalardo, 23, 95131 Catania CT. <br>Soccorsi in arrivo!"
    emergency_resources =f"Qui un paio di contatti utili <br>📞 **Numero Antiviolenza:** 1522 <br>📞 **Numero Soccorsi:** 112 <br>🚑 **Tempo di intervento stimato in base alla tua posizione:** 10/11 minuti"
    #emergency_response = f"🚨 Chiamata d'emergenza attivata per la tua posizione a {location}. Soccorsi in arrivo!"
   #emergency_resources = "📞 **Numero Antiviolenza:** 1522\n📞 **Numero Soccorsi:** 112\n🚑 **Tempo di intervento stimato:** 10 minuti"

    st.markdown(emergency_response, unsafe_allow_html=True)
    st.markdown(emergency_resources, unsafe_allow_html=True)

    return emergency_response, emergency_resources

# Funzione per verificare se l'utente sta migliorando
def detect_improvement(user_input):
    improvement_keywords = ['sto meglio', 'mi sento meglio', 'è passato', 'sto andando avanti']
    if any(word in user_input.lower() for word in improvement_keywords):
        return True
    return False

# Funzione per rilevare l'età (sia numerica che in lettere)
def detect_age(user_input):
    age_pattern = r'\b\d{1,2}\b'
    match = re.search(age_pattern, user_input)
    if match:
        return int(match.group())

    age_in_letters = {
        "quindici": 15,
        "sedici": 16,
        "diciassette": 17,
        "diciotto": 18,
        "diciannove": 19,
        "venti": 20
    }
    for word, age in age_in_letters.items():
        if word in user_input.lower():
            return age
    return None

# Funzione per determinare la categoria dell'utente in base all'età
def detect_category(age):
    if age <= 17:
        return "giovane"
    elif 18 <= age <= 65:
        return "adulto"
    else:
        return "generico"

# Funzione per eseguire la conversazione con l'assistente
def run_conversation():
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "🌟 Benvenuto! Come posso aiutarti oggi? Ma prima conosciamoci meglio, come ti chiami? quanti anni hai🧠"}
        ]
        st.session_state.last_input = ""
        st.session_state.problem_identified = False
        st.session_state.age_asked = False
        st.session_state.input_message = ""
        st.session_state.name_asked = False

    # Chiedere il nome
    #if not st.session_state.name_asked:
       # name = st.text_input("Come ti chiami? 😊")
       # if name:
           # st.session_state.user_name = name
           # st.session_state.messages.append({"role": "assistant", "content": f"Ciao, {name}! È un piacere parlare con te."})
           # st.session_state.name_asked = True

    # Visualizzare la conversazione
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f'<div style="padding: 10px; border-radius: 10px; background-color: #d3f5ec; margin: 10px 0; font-family: sans-serif; font-size: 16px;">👤 {message["content"]}</div>', unsafe_allow_html=True)
        elif message["role"] == "assistant":
            category = st.session_state.get('category', 'generico')
            if category == "giovane":
                st.markdown(f'<div style="padding: 15px; border-radius: 15px; background-color: #00FFFF; margin: 10px 0; font-family: "Poppins", cursive, sans-serif; font-size: 18px; color: #ff3b7f; border: 2px solid #ff006f;">🧑👱 {message["content"]}</div>', unsafe_allow_html=True)
            elif category == "adulto":
                st.markdown(f'<div style="padding: 15px; border-radius: 15px; background-color: #989aff; margin: 10px 0; font-family: "Poppins", sans-serif; font-size: 18px; color: #3c3c3c; border: 2px solid #666;">🧔‍♂️🧑‍🦰 {message["content"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div style="padding: 15px; border-radius: 15px; background-color: #98FF98; margin: 10px 0; font-family: "Poppins", sans-serif; font-size: 18px; color: #404040; border: 2px solid #999;">💬 {message["content"]}</div>', unsafe_allow_html=True)

    input_message = st.text_input("Scrivi qui il tuo messaggio:")

    if input_message != st.session_state.last_input:
        if input_message:
            st.session_state.messages.append({"role": "user", "content": input_message})

            if not st.session_state.age_asked:
                age = detect_age(input_message)
                if age:
                    category = detect_category(age)
                    st.session_state.category = category
                    st.session_state.messages.append({"role": "assistant", "content": f"Ciao grazie per esserti presentato, adesso che ci siamo conusciuti posso farti parlare con un bot adatto a te che ti aiuterà e seguirà in tutto quello di cui hai bisogno."})
                    #st.session_state.messages.append({"role": "assistant", "content": f"Età rilevata: {age} anni. Categoria: {category}."})

                    if category == "giovane":
                        response = "Ciao, sono davvero felice che tu sia qui. Sono il tuo bot personale di assitenza. So che a volte la vita ci mette davanti a sfide enormi: il lavoro che non smette di chiedere, le relazioni che ci pesano, o quel senso di solitudine che può farsi sentire anche tra mille persone. Eppure, voglio che tu sappia che anche nei momenti più difficili, non sei mai solo. Sono qui per ascoltarti con il cuore aperto, per offrirti uno spazio dove puoi essere completamente te stesso, senza maschere. Raccontami di te, se ti va. Come ti senti in questo momento? C'è qualcosa che ti preoccupa, qualcosa che ti fa sentire sopraffatto, ma che non sai a chi dire?"
                        st.session_state.messages.append({"role": "assistant", "content": response})
                    elif category == "adulto":
                        response = "Ehi, ciao! Sono il tuo bot personale di assistenza. Sono davvero felice che tu sia qui. Se ti va di parlare, sono qui per ascoltarti, senza fretta e senza giudizio. A volte tutti abbiamo bisogno di qualcuno con cui parlare, e se c'è qualcosa che ti pesa o qualcosa che ti fa sentire strano, possiamo discuterne insieme. Come ti senti oggi? C'è qualcosa di cui ti piacerebbe parlare o magari hai una domanda che ti frulla in testa"
                        st.session_state.messages.append({"role": "assistant", "content": response})
                    else:
                        response = "Sto rispondendo come un bot generico."
                        st.session_state.messages.append({"role": "assistant", "content": response})

                    st.session_state.age_asked = True
                else:
                    st.session_state.messages.append({"role": "assistant", "content": "Non sono riuscito a rilevare la tua età. Puoi per favore scrivere la tua età?"})

            # Verifica se c'è un'emergenza
            elif detect_violence(input_message):
                location = get_user_location()
                emergency_response, emergency_resources = emergency_call(location)
                st.session_state.messages.append({"role": "assistant", "content": emergency_response})
                st.session_state.messages.append({"role": "assistant", "content": emergency_resources})

            elif detect_improvement(input_message):
                st.session_state.messages.append({"role": "assistant", "content": "Sono felice che tu ti stia sentendo meglio! Se hai bisogno di parlare, sono qui."})
            else:
                # Se non c'è emergenza e l'età è già stata rilevata
                response = get_groq_response(st.session_state.messages)
                st.session_state.messages.append({"role": "assistant", "content": response})

            st.session_state.last_input = input_message
            st.rerun()

# Funzione principale di Streamlit
def main():
    st.set_page_config(page_title="💬Chat di Supporto", page_icon="🧠", layout="centered")
    st.markdown("""
    <style>
        body {
    background: linear-gradient(45deg, #ff6347, #ffebcd); /* Un gradiente che va dal rosso al beige */
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background-color: rgba(255, 255, 255, 0.8); /* Sfondo traslucido per il contenuto */
}

        }
        h1 {
            color: #FF6347;
            font-size: 36px;
            font-weight: 600;
            text-align: center;
        }
        .message-box {
            border-radius: 15px;
            padding: 10px;
            margin: 10px;
            font-size: 16px;
            background-color: #ffffff;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
    </style>
    """, unsafe_allow_html=True)

    st.title("💬Chat di Supporto🧠")
    #st.write("Benvenuto nel nostro chatbot di supporto psicologico. Siamo qui per aiutarti, ascoltarti e offrirti risorse utili.")
    
    run_conversation()

if __name__ == "__main__":
    main()  