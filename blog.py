import streamlit as st

# Configuração da página
st.set_page_config(page_title="Casa do Carvalho", layout="wide", page_icon="🌳")

# Barra lateral de navegação
st.sidebar.title("Menu")
menu_options = ["Home", "Sobre", "Posts", "Contato"]
menu_selection = st.sidebar.radio("Navegação", menu_options)

# Função para exibir a página inicial usando HTML
def home():
    st.markdown("""
        <h1>Bem-vindo a Casa do Carvalho</h1>
        <p>Este é um blog de exemplo criado com Streamlit. Aqui você encontrará várias postagens sobre diferentes tópicos.</p>
        <p>Use o menu à esquerda para navegar pelo blog.</p>
        <a href="bit.ly/FalarComInacio">@inaciowagner</a>
    """, unsafe_allow_html=True)

# Função para exibir a página 'Sobre' usando HTML
def about():
    st.markdown("""
        <h1>Sobre o Blog</h1>
        <p>Este blog foi criado para demonstrar como usar Streamlit para criar uma aplicação de blog simples. 
        Você pode adicionar quantas seções quiser e personalizar o conteúdo.</p>
    """, unsafe_allow_html=True)

# Função para exibir a página de posts usando HTML
def posts():
    st.markdown("""
        # Alimentação
        ###### 24.ago.2024 às 13h58
       **Para uma pessoa que precisa evitar açúcar e carboidratos, é importante conhecer os alimentos típicos do Nordeste que devem ser evitados. Aqui estão alguns exemplos:**

        ### Alimentos a Evitar:
        1. **Cuscuz**: Feito de milho, é rico em carboidratos.
        2. **Acarajé**: Bolinho de feijão-fradinho frito, geralmente recheado com vatapá e camarão, contém carboidratos e é frito em óleo.
        3. **Tapioca**: Embora seja uma alternativa sem glúten, a tapioca é rica em carboidratos.
        4. **Bolo de Rolo**: Um doce tradicional feito com açúcar e farinha de trigo.
        5. **Rapadura**: Feita de açúcar de cana, é rica em açúcar.
        6. **Pamonha**: Feita de milho, contém carboidratos.
        7. **Canjica**: Feita de milho e geralmente adoçada com açúcar.
        8. **Baião de Dois**: Prato que combina arroz e feijão, ambos ricos em carboidratos.
        9. **Mungunzá**: Doce feito de milho e leite de coco, geralmente adoçado com açúcar.

        ### Alternativas Saudáveis:
        1. **Carnes e Peixes**: Carne de sol, carne de bode, peixes como tilápia e sururu.
        2. **Ovos**: Uma excelente fonte de proteína sem carboidratos.
        3. **Legumes e Verduras**: Couve, espinafre, alface, rúcula, quiabo, chuchu.
        4. **Frutas com Baixo Teor de Açúcar**: Abacate, coco (em moderação), limão.
        5. **Oleaginosas**: Castanha de caju, amendoim (em moderação).

        Essas alternativas podem ajudar a manter uma dieta equilibrada e saudável, respeitando as restrições de açúcar e carboidratos. Se precisar de mais alguma coisa ou tiver outras dúvidas, estou à disposição! 😊¹²³.

        Fonte: conversa com o Copilot, 24/08/2024
        (1) 20 comidas típicas do Nordeste: as melhores para você experimentar. https://www.worldpackers.com/pt-BR/articles/comidas-tipicas-do-nordeste.
        (2) Comidas Típicas do Nordeste: Conheça 33 Delícias Nordestinas. https://caminhosmelevem.com/comidas-tipicas-nordeste/.
        (3) ALIMENTOS SEM AÇÚCAR: lista completa, dicas para cortar o açúcar e .... https://www.tudoreceitas.com/artigo-alimentos-sem-acucar-lista-completa-8209.html.
        (4) Alimentos sem açúcar: lista | Guia da Alimentação. https://guiadaalimentacao.com/alimentacao-sem-acucar/alimentos-sem-acucar-confira-nossa-lista/.
        (5) 25 Alimentos sem Carboidratos - conheça os melhores! - Guia do Corpo. https://guiadocorpo.com/25-alimentos-sem-carboidratos/.
        (6) undefined. https://www.instagram.com/rafabeatrizzz/.
    """, unsafe_allow_html=True)
    st.html("<hr/>")
    st.markdown('''
        # Guns of Brixton
        ###### 23.ago.2024 às 15h40
        As histórias de opressão se perdem na escuridão de sua própria ignorância e ficam dando voltas as escuras no tempo e no espaço, se repetindo no decorrer da história...

        "The Guns of Brixton" é uma música da banda britânica The Clash, lançada em 1979 no álbum *London Calling*. A canção aborda temas de opressão, resistência e tensão social, especialmente no contexto da comunidade negra em Brixton, um bairro de Londres. Vamos explorar alguns aspectos socioculturais dessa letra:

        ### Contexto Histórico e Cultural
        Brixton, durante as décadas de 1970 e 1980, era um dos epicentros da comunidade afro-caribenha em Londres. Naquela época, havia uma crescente tensão racial entre a polícia e a população local, especialmente a comunidade negra, que frequentemente enfrentava discriminação e brutalidade policial. Essas tensões culminaram em distúrbios e revoltas, como os *Brixton Riots* de 1981.

        A letra reflete esse clima de tensão e opressão, descrevendo uma situação em que alguém é confrontado pela polícia em sua própria casa ("When they kick at your front door, How you gonna come?"). A pergunta feita sugere um dilema: reagir com violência ou se submeter, o que espelha o sentimento de impotência e a necessidade de sobrevivência enfrentados por muitos na época.

        ### Resistência e Identidade
        A referência às "Guns of Brixton" simboliza a resistência contra a opressão, sugerindo que, mesmo que a comunidade seja oprimida e esmagada, haverá uma resposta inevitável. O uso do verbo "crush" (esmagar) e "bruise" (machucar) indica a brutalidade enfrentada, mas a repetição de "you'll have to answer to the guns of Brixton" enfatiza que essa opressão não ficará impune. A arma aqui pode ser vista tanto como literal quanto metafórica, representando a resistência física ou a força da comunidade.

        ### Influências Musicais e Referências Culturais
        A música também faz referência ao filme *The Harder They Come* (1972), estrelado por Jimmy Cliff, que se tornou um marco na cultura popular jamaicana e afro-caribenha. O filme retrata a luta de um homem contra a corrupção e a opressão na Jamaica, ressoando com a realidade das comunidades marginalizadas em lugares como Brixton. A linha "His game is called survivin'" captura essa luta pela sobrevivência em um ambiente hostil.

        A sonoridade da música, influenciada pelo reggae, também reforça a conexão com a cultura jamaicana, que era uma parte significativa da identidade de Brixton naquela época. 

        ### Análise Sociocultural
        A música reflete a realidade de muitas comunidades marginalizadas, onde a violência policial e a discriminação racial eram (e ainda são) uma realidade diária. "The Guns of Brixton" pode ser vista como um hino de resistência, capturando o sentimento de uma geração que enfrentava um sistema que muitas vezes parecia estar contra eles. Ao mesmo tempo, a música também questiona o ciclo de violência e sobrevivência, sugerindo que, independentemente de como se escolha resistir, a luta continuará.

        Assim, *The Guns of Brixton* não é apenas uma música sobre um local ou um evento; é uma representação das tensões sociais e raciais da época, que ainda reverberam em muitas sociedades contemporâneas.
        Mais referências:
        https://en.wikipedia.org/wiki/1981_Brixton_riot



''')

# Função para exibir a página de contato usando HTML
def contact():
    st.markdown("""
        <h1>Contato</h1>
        <p>Entre em contato conosco preenchendo o formulário abaixo:</p>
        <form  method="post" action="mailto:inaciowagner@gmail.com">
            <label for="name">Nome:</label><br>
            <input type="text" id="name" name="name"><br><br>
            <label for="email">Email:</label><br>
            <input type="email" id="email" name="email"><br><br>
            <label for="message">Mensagem:</label><br>
            <textarea id="message" name="message"></textarea><br><br>
            <input type="submit" value="Enviar">
        </form>
    """, unsafe_allow_html=True)

# Lógica de navegação
if menu_selection == "Home":
    home()
elif menu_selection == "Sobre":
    about()
elif menu_selection == "Posts":
    posts()
elif menu_selection == "Contato":
    contact()
