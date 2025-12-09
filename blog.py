import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_icon="💰", page_title="Reforma Tributária")


st.markdown(''' 
 # WEBINAR REFORMA TRIBUTÁRIA
## TOTVS CONSINCO
---
### Anotações

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
---
**Ativando o parâmetro:**
1. Monitor -> Configurações -> Cargas -> Cargas para Monitor;
2. Monitor -> Configurações -> Cargas -> Cargas para PDV;
3. Monitor -> Configurações -> Configurações de PDVs -> DF-e -> Geral -> Ativa Reforma Tributária
(recomenda-se fazer em um PDV inicialmente como teste, e posteriormente faz-se nos demais) 

---
##### Obs:
* o resultado da atualização é transparente para o operador(a) de caixa;
* atualizar os PDVs;
* necessária 25.11.006;
* nossa versão atualmente 25.9.0.4;
* prazo 05/02/2026.
---
##### Informações da comunidade Whatsapp
473 TOTVS Informa - Descontinuação da Versão 25.01 prorrogada

Prezados(as) Clientes,

A versão 26.01 dos produtos TOTVS Varejo Supermercados - Linhas Consinco, RMS e WMS será disponibilizada em janeiro de 2026 e trará importantes evoluções estruturais.

Entre elas, destaca-se a adequação ao novo padrão de CNPJ Alfanumérico, cuja vigência inicia-se em julho de 2026.

Diante disso, recomendamos o planejamento da atualização para esta versão ainda no primeiro semestre de 2026, garantindo assim plena conformidade com a nova legislação. Ressaltamos que essa adequação não está contemplada nas versões 25.01 e 25.07.

Adicionalmente, entendendo o impacto da Reforma Tributária prevista para entrar em vigor em 01/01/2026, informamos que, de forma excepcional , prorrogaremos o encerramento do suporte para correções de bugs e atualizações legais da versão 25.01 até 28/02/2026 .

Em resumo:

* Até 28/02/2026 , é necessário que sua empresa esteja utilizando, no mínimo, a versão 25.07 .
* Até 30/06/2026 , será obrigatório estar na versão 26.01 .

Caso sua operação envolva customizações ou integrações , recomendamos antecipar o planejamento para garantir a compatibilidade com a versão 26.01.
https://tdn.totvs.com/pages/releaseview.action?pageId=1014650613

Permanecemos à disposição para esclarecer quaisquer dúvidas e para apoiá-lo(a) nesse processo de atualização.

Atenciosamente,
Equipe TOTVS Varejo Supermercados
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
