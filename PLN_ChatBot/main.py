import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import json


# Baixando stop words em português
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

# Stop words em português
stop_words = set(stopwords.words('portuguese'))

# Dicionário de perguntas e respostas da clínica odontológica
faq_dict = {
    "quais são os horários de atendimento?": "Nosso horário de atendimento é de segunda a sexta-feira, das 8h às 18h.",
    "quais os tipos de tratamento que vocês oferecem?": "Oferecemos limpeza, clareamento, implantes, restaurações, tratamentos ortodônticos e muito mais.",
    "vocês aceitam plano de saúde?": "Sim, aceitamos diversos planos de saúde odontológicos. Entre em contato para mais informações.",
    "como faço para agendar uma consulta?": "Para agendar uma consulta, você pode ligar para nossa recepção ou fazer o agendamento online pelo nosso site.",
    "quanto custa uma consulta de avaliação?": "A consulta de avaliação custa R$ 150, mas pode variar dependendo do plano de saúde.",
    "vocês fazem clareamento dental?": "Sim, fazemos clareamento dental. Entre em contato para agendar uma avaliação.",
    "vocês fazem implantes dentários?": "Sim, realizamos implantes dentários com profissionais especializados.",
    "quanto tempo dura o tratamento ortodôntico?": "A duração do tratamento ortodôntico varia de acordo com o caso, mas geralmente dura entre 12 e 24 meses.",
    "posso pagar em parcelas?": "Sim, oferecemos opções de parcelamento. Converse com nossa equipe para mais detalhes.",
    "quais são as formas de pagamento aceitas?": "Aceitamos cartões de crédito, débito, boleto e transferências bancárias.",
    "como posso saber se preciso de um tratamento ortodôntico?": "Agende uma consulta para que possamos fazer uma avaliação e recomendar o melhor tratamento."
}

def load_faq(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)
    
# Função para remover stop words de uma frase
def remove_stop_words(sentence):
    words = word_tokenize(sentence.lower())
    filtered_sentence = [w for w in words if w not in stop_words]
    return filtered_sentence

# Função para encontrar a melhor resposta com base na similaridade de palavras
def get_response(user_input):
    user_input_tokens = remove_stop_words(user_input)
    
    best_match = None
    highest_similarity = 0
    
    # Verifica a similaridade entre a entrada do usuário e as perguntas no dicionário
    for question, answer in faq_dict.items():
        question_tokens = remove_stop_words(question)
        
        # Conta quantas palavras coincidem entre a pergunta e a entrada do usuário
        similarity = len(set(user_input_tokens) & set(question_tokens))
        
        if similarity > highest_similarity:
            highest_similarity = similarity
            best_match = answer
    
    if best_match:
        return best_match
    else:
        return "Desculpe, não entendi sua pergunta. Pode reformular?"

# Função principal do bot
def chat():
    print("Olá! Sou o assistente virtual da clínica odontológica. Como posso ajudá-lo hoje?")
    
    while True:
        user_input = input("Você: ")
        
        if user_input.lower() in ['sair', 'encerrar', 'tchau']:
            print("Bot: Obrigado por conversar conosco! Tenha um ótimo dia!")
            break
        
        response = get_response(user_input)
        print(f"Bot: {response}")

# Inicia o chat
if __name__ == "__main__":
    faq_dict = load_faq('./dicionario.json')
    chat()
