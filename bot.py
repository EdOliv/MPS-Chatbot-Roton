import regex as re
from database import database, menu


def GenerateAnswer(question):
  keyword = GetKeyWord(question)
  order = ConfirmOrder(keyword, question)
  try:
    answer = database[keyword]
    answer += order
  except:
    return database['default'] # se não houver uma resposta pronta, retorna uma resposta padrão, ex: "não entendi"
  else:
    return answer


# recebe a pergunta(str) e retorna uma lista de palavras-chave encontradas na pergunta
def GetKeyWord(question):
  question = question.lower()
  question.translate(question.maketrans("áéíóú", 'aeiou'))
  keyword = ''
  keylist = database.keys()
  for key in keylist:
    if match := re.search(key, question):
      keyword = key
  return keyword


register = {'cart':'', 'total': 0, 'pay': '', 'address': ''}

def ConfirmOrder(keyword, question):
  if keyword in menu.keys():
    register['cart'] += f'{keyword} '
    register['total'] += menu[keyword]
  elif keyword in ['cartao', 'dinheiro']:
    register['pay'] += question
  elif keyword == 'rua':
    register['address'] += question
    order = f"  Carrinho: {register['cart']}\n  Total: {register['total']} reais\n" +\
			      f"  Forma de pagamento: {register['pay']}\n" +\
			      f"  Endereço de entrega: {register['address']}"
    register['cart'] = register['pay'] = register['address'] = ''
    register['total'] = 0
    return order
  return ''



#debug
def main():
  question = ''
  while question != 'fim':
    question = input()
    answer = GenerateAnswer(question)
    print(answer)

if __name__ == "__main__":
  main()
#debug