from random import choice

cumprimentos = ['> Olá! Gostaria de ver nosso cardápio?',
                '> Oi! Que tal dar uma olhada no nosso cardápio?']

cardapios = [['x-salada', 'suco', 'combo'],
            ['pastel', 'refrigerante', 'fritas'],
            ['sushi', 'sashimi', 'yakisoba'],
            ['sorvete', 'chocolate quente', 'pudim']]

atual = choice(cardapios)
#print(atual)

database = {'oi': f'{choice(cumprimentos)}',
            'ola': f'{choice(cumprimentos)}',
            'olhar': f"> Este é o cardápio de hoje:\n  {' | '.join(atual)}",
            'ver': f"> Este é o cardápio de hoje:\n  {' | '.join(atual)}",
            'cardapio': f"> Este é o cardápio de atual:\n  {' | '.join(atual)}",
            atual[0]: f"> O item {atual[0]} foi adicionado ao seu carrinho!",
            atual[1]: f"> O item {atual[1]} foi adicionado ao seu carrinho!",
            atual[2]: f"> O item {atual[2]} foi adicionado ao seu carrinho!",
            'tchau': f'Até mais! Volte sempre! :D',
            'default':'Sinto muito. Não entendi. :('}
