#Flet
#Importar o flet
import flet as ft

#Criar uma funcao principal para rodar o seu sistema
def chat(pagina):
    #criar um titulo
    titulo = ft.Text("HashZap")

    def enviar_msg_tunel(mensagem):
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()

    pagina.pubsub.subscribe(enviar_msg_tunel)


    def enviar_mensagem(evento):
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = campo_mensagem.value
        mensagem = (f"{nome_usuario}: {texto_campo_mensagem}")
        pagina.pubsub.send_all(mensagem)
        #limpar a caixa de enviar mensagem
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(label="Digite aqui a sua mensagem",on_submit=enviar_mensagem)

    botao_enviar = ft.ElevatedButton("Enviar",on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_mensagem, botao_enviar])

    chat = ft.Column()




    def entrar_chat(evento):
        #fechar o popup
        popup.open=False
        #sumir com o titulo
        pagina.remove(titulo)
        #sumir com o botao de iniciar chat
        pagina.remove(botao)
        #carregar o chat 
        pagina.add(chat)
        #carregar o campo de enviar msg
        #carregar o botao de enviar
        pagina.add(linha_enviar)

        #adicionar no chat a mensagem "usuario entrou no chat"
        nome_usuario = caixa_nome.value
        mensagem = (f"{nome_usuario} entrou no chat")
        pagina.pubsub.send_all(mensagem)
        pagina.update()
       

    #criar o popup
    titulo_popup = ft.Text("Bem Vindo ao HashZap")
    caixa_nome = ft.TextField(label=("Digite o seu nome"),on_submit=entrar_chat)
    botao_popup = ft.ElevatedButton("Entrar no chat",on_click=entrar_chat) 

    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome, actions=[botao_popup])  





    #criar um botao inicial
    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open=True
        pagina.update()


    botao = ft.ElevatedButton("Iniciar Chat",on_click=abrir_popup)

    #colocar os elementos da pagina
    pagina.add(titulo)
    pagina.add(botao)

#Executar essa funcao com o flet
ft.app(chat,view=ft.WEB_BROWSER)