import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_icon="💰", page_title="Reforma Tributária")


st.markdown(''' 
 # WEBINAR REFORMA TRIBUTÁRIA
## TOTVS CONSINCO

### Anotações

#### Agenda 
1. Como preparar o PDV para a Reforma Tributária
    ##### Estrutura e Motor Tributário
    	a) Estrutura
    	    * Adequando os processos da nova importação e exportação de vendas, alinhada à nova estrutura tributária.
    
          
2. Pré-requisitos para instalar
* Ter acesso ao Monitor de PDVs;
* Ter realizado as configurações de emissão de NFC-e no PDV;
* definir o ambiente de emissão: homologação ou produção;
* Integrações para linhas Consinco e RMS: ter acesso ao Configurador de Cenários Tributários e configurado cenários tributários;
* Realizar o envio de cargas;
* Ativar o parâmetro da Reforma Tributária
            
##### Obs:
* atualizar os PDVs;
* nossa versão atualmente 25.9.0.4;
''')

st.html("""
        <h3>Conteudo Suplementar</h3> 
        <ul>
            <li>
                <a href='https://tdn.totvs.com/pages/releaseview.action?pageId=1003982193'>Documentação Auxiliar</a>
            </li>
        </ul>
        
        """)

st.image(
    'Captura de tela de 2025-11-30 14-04-40.png',
    caption='https://chat.whatsapp.com/DZEtVKJQto41I1Z9TUCCkL ',
    width=300
)
#st.write("https://chat.whatsapp.com/DZEtVKJQto41I1Z9TUCCkL")
