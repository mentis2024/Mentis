# **Mentis**

## **Overview**
Mentis è un progetto che combina tecnologia e psicologia per offrire un supporto al benessere mentale attraverso un'interfaccia user-friendly. Integra funzionalità di intrattenimento e strumenti di intelligenza artificiale avanzati per migliorare la consapevolezza interiore degli utenti.

---

## **Features**
### **1. Interactive Game: Guess the Number**
- Un mini-gioco per rompere il ghiaccio.
- Gli utenti devono indovinare un numero segreto tra 1 e 10.
- Feedback immediato:
  - **Congratulazioni:** Se il numero è corretto.
  - **Soluzione corretta:** In caso di errore.
- Semplice da giocare, costruito con **Streamlit**.

### **2. Multi-Agent AI Support System**
- **Conversazioni empatiche:** Risposte generate dinamicamente tramite il modello "llama3-8b-8192" (Groq API).
- **Rilevamento di emergenze:** 
  - Analisi del linguaggio per identificare situazioni di violenza o pensieri suicidi.
  - Suggerisce interventi o risorse in caso di rilevamento.
- **Geolocalizzazione simulata:** Un sistema di tracciamento iniziale (dimostrativo) per ampliare le funzionalità.
- **Facilità di accesso:** Interfaccia intuitiva per utenti con background diversi.

---

## **How to Use**
1. **Prerequisiti:**
   - Installare Python 3.8 o superiore.
   - Assicurarsi di avere Streamlit installato. Se non lo hai, puoi installarlo con:  
     ```bash
     pip install streamlit
     ```
   - Altre dipendenze (ad esempio librerie usate nei file) verranno installate automaticamente al bisogno.

2. **Scarica i file:**
   - Scarica i file `game.py` e `multiagente.py` dal repository o dal link fornito.

3. **Esegui i file:**
   - Per avviare il gioco "Guess the Number", esegui:  
     ```bash
     streamlit run game.py
     ```
   - Per avviare il sistema multiagente AI, esegui:  
     ```bash
     streamlit run multiagente.py
     ```

4. **Accedi all'applicazione:**
   - Una volta eseguito, accedi tramite il browser all'indirizzo locale (es. [http://localhost:8501](http://localhost:8501)) per interagire con l'app.

---

## **Technology Stack**
- **Python** - Linguaggio di programmazione principale.
- **Streamlit** - Per la creazione dell'interfaccia grafica.
- **Groq API** - Per l'intelligenza artificiale multiagente.
- **Librerie Python:**
  - `random` - Per il gioco.
  - `re` - Per l'analisi del linguaggio.

---

## **Functionality Details**
### **game.py**
- Implementa il gioco "Guess the Number".
- Fornisce feedback visivo per migliorare l'interazione utente.
- Include un'opzione per passare alla pagina del sistema multiagente.

### **multiagente.py**
- Sistema multiagente AI con le seguenti funzionalità:
  - Generazione di risposte basate sul modello "llama3-8b-8192".
  - Rilevamento di situazioni di emergenza tramite parole chiave (es. "suicidio", "violenza").
  - Simulazione di geolocalizzazione per espandere future capacità di personalizzazione.

---

## **Known Issues and Challenges**
- **Rilevamento di emergenze:** La sensibilità può generare falsi positivi o negativi.
- **Latenza AI:** Dipende dalla connessione e dalla capacità di elaborazione del modello.
- **Geolocalizzazione:** La funzionalità attuale è solo simulativa.

---

## **Future Improvements**
- Migliorare il rilevamento del linguaggio con tecniche NLP avanzate.
- Integrare funzionalità di mindfulness guidata.
- Creare una versione mobile per un accesso più ampio.
- Aggiungere il supporto multilingue per raggiungere una comunità globale.
- Collaborare con esperti in psicologia per perfezionare i contenuti.

---

## **Contributors**
- Nome del creatore: Campo Filippo, Salvatore Campisano
- Contatti: filippocampo98@outlook.it, scampisano50@gmail.com
