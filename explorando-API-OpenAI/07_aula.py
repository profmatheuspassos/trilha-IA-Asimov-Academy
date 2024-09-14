import openai
from dotenv import load_dotenv, find_dotenv

# Carrega as variáveis de ambiente a partir de um arquivo .env
_ = load_dotenv(find_dotenv())

# Cria uma instância do cliente da API OpenAI
client = openai.Client()

# Função responsável por gerar texto com base nas mensagens enviadas pelo usuário
def geracao_texto(mensagens):

    # Faz uma chamada à API da OpenAI para gerar uma resposta usando o modelo especificado
    resposta = client.chat.completions.create(
        messages=mensagens,           # As mensagens que foram enviadas no chat até agora
        model='gpt-4o-mini',          # Modelo de linguagem usado para gerar as respostas
        temperature=0,                # Define a criatividade da resposta; 0 significa respostas mais previsíveis e objetivas
        max_tokens=1000,              # Número máximo de tokens (unidades de palavras) na resposta gerada
        stream=True,                  # Habilita o modo de streaming, que retorna a resposta de forma gradual
    )

    print('\nAssistente: ', end='')    # Exibe o início da resposta do assistente no console
    texto_completo = ''                # Variável para armazenar o texto gerado pelo assistente
    
    # Loop para processar o streaming da resposta
    for resposta_stream in resposta:
        texto = resposta_stream.choices[0].delta.content  # Extrai o conteúdo do stream de respostas
        if texto:                     # Se houver conteúdo no stream, exibe e armazena
            print(texto, end='')      # Exibe o texto gerado em tempo real no console
            texto_completo += texto   # Adiciona o texto gerado à variável que armazena a resposta completa
    print('\n')                       # Imprime uma nova linha ao final da resposta
    
    # Adiciona a resposta completa do assistente à lista de mensagens
    mensagens.append({'role': 'assistant', 'content': texto_completo})
    return mensagens                  # Retorna a lista de mensagens atualizada


if __name__ == '__main__':

    print('Bem-vindo ao chatBot com Python da Asimov :)')
    print('----------------------------------------------------------------------')
    print('Lembre-se de que você pode sair a qualquer momento digitando \"sair\".')
    
    # Inicializa uma lista vazia para armazenar as mensagens trocadas no chat
    mensagens = []
    
    # Loop principal do chat para interagir com o usuário
    while True:
    
        # Captura a entrada do usuário
        input_usuario = input('\nUsuário: ')
    
        # Verifica se o usuário digitou 'sair', e encerra o loop
        if input_usuario.lower() == "sair":
            print("\nObrigado por utilizar o Assistente!")
            break
    
        # Adiciona a entrada do usuário à lista de mensagens com o papel 'user'
        mensagens.append({'role': 'user', 'content': input_usuario})
    
        # Chama a função para gerar texto e atualiza a lista de mensagens
        mensagens = geracao_texto(mensagens)
