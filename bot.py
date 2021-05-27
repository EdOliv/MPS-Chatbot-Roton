import regex as re
from database import database

def GenerateAnswer(question):
  keyword = GetKeyWord(question)
  try:
    answer = database[keyword]
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
  


#debug
def main():
  question = input()
  answer = GenerateAnswer(question)
  print(answer)

if __name__ == "__main__":
  main()
#debug