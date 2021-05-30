from random import choice

greeting = ['Olá! Gostaria de ver nosso cardápio?',
            'Oi! Que tal dar uma olhada no nosso cardápio?',
            'Oi, oi! Deseja conferir nosso cardápio?']

farewell = ['Obrigado pela preferência! Volte sempre! :D',
            'Teve uma boa experiência? Volte sempre! :)',
            'Até mais! Volte sempre! :3']

endOrder = ['Carrinho preenchido! Como você gostaria de efetuar o pagamento?',
            'Carrinho finalizado! Qual será a forma de pagamento?']

menu = {'x-salada': 6, 'suco': 3, 'pastel': 5,
        'refrigerante': 5, 'fritas': 4, 'pudim': 30}

order = ''

database = {'oi|ola|olá': choice(greeting),
            
            'sim|olhar|ver|cardapio|cardápio': 'Esse é o maravilhoso cardápio de hoje:\n'+\
	                                           ' reais\n'.join([f'{i} - {j}' for i, j in menu.items()])+' reais',
            
            'x-salada': 'O item x-salada foi adicionado ao seu carrinho!',
            'suco': 'O item suco foi adicionado ao seu carrinho!',
            'pastel': 'O item pastel foi adicionado ao seu carrinho!',
            'refrigerante': 'O item refrigerante foi adicionado ao seu carrinho!',
            'fritas': 'O item fritas foi adicionado ao seu carrinho!',
            'pudim': 'O item pudim foi adicionado ao seu carrinho!',

            'apenas|somente' : choice(endOrder),

            'dinheiro': 'Certo! Prepare suas cédulas para o entregador! Onde ele deve entregar?',
            'cartao|cartão': 'Ok! Levaremos a maquininha para você! Qual será o endereço da entrega?',

            'rua': 'Tudo certo! Endereço definido! Deseja confirmar ou descartar o pedido a seguir?\n',

			'confirmar': 'Pedido confirmado com sucesso. Aguarde a entrega. Até a próxima!',
			'descartar': 'Pedido descartado. Que tal recomeçar? Deseja ver o cardápio de novo?',

            'tchau|adeus|encerrar|fim': choice(farewell),
            
            'default':'Sinto muito. Não entendi. :('}
