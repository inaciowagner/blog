import streamlit as st
import pandas as pd
import smtplib
from email.mime.text import MIMEText

def send_email(data):
    # Configurações do e-mail
    sender = 'seu_email@example.com'
    receiver = 'destinatario@example.com'
    password = 'sua_senha'
    subject = 'Resultados da Enquete'

    # Formatar os dados em uma tabela
    df = pd.DataFrame(data)
    html = df.to_html()

    # Criar o corpo do e-mail
    message = MIMEText(html, 'html')
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = subject

    # Conectar ao servidor SMTP e enviar o e-mail
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(sender, password)
        smtp.sendmail(sender, receiver, message.as_string())

# Interface da enquete
st.title("Enquete Simples")
nome = st.text_input("Seu nome:")
idade = st.number_input("Sua idade:")
resposta = st.selectbox("Qual sua linguagem de programação favorita?", ["Python", "R", "JavaScript"])

if st.button("Enviar"):
    data = {'Nome': [nome], 'Idade': [idade], 'Linguagem': [resposta]}
    send_email(data)
    st.success("Dados enviados com sucesso!")