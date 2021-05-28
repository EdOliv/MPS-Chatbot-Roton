from random import choice

greeting = ['> Olá! Gostaria de ver nosso cardápio?',
            '> Oi! Que tal dar uma olhada no nosso cardápio?']

farewell = ['> Obrigado pela preferência! Volte sempre! :D',
            '> Teve uma boa experiência? Volte sempre! :)',
            '> Até mais! Volte sempre! :3']

menu = {'x-salada': 6, 'suco': 3.5, 'pastel': 5,
        'refrigerante': 4.5, 'fritas': 4, 'pudim': 30}

database = {'oi': choice(greeting),
            'ola': choice(greeting),
            
            'olhar': '> Olha só o maravilhoso cardápio de hoje:\n  '+'\n  '.join(menu.keys()),
            'ver': '> Olha só o maravilhoso cardápio de hoje:\n  '+'\n  '.join(menu.keys()),
            'cardapio': '> Olha só o maravilhoso cardápio de hoje:\n  '+'\n  '.join(menu.keys()),
            
            'x-salada': '> O item x-salada foi adicionado ao seu carrinho!',
            'suco': '> O item suco foi adicionado ao seu carrinho!',
            'pastel': '> O item pastel foi adicionado ao seu carrinho!',
            'refrigerante': '> O item refrigerante foi adicionado ao seu carrinho!',
            'fritas': '> O item fritas foi adicionado ao seu carrinho!',
            'pudim': '> O item pudim foi adicionado ao seu carrinho!',

            'apenas': '> Carrinho preenchido! Como você gostaria de efetuar o pagamento?',
            'somente': '> Carrinho finalizado! Qual será a forma de pagamento?',

            'dinheiro': '> Certo! Prepare suas cédulas para o entregador! Onde ele deve entregar?',
            'cartao': '> Ok! Levaremos a maquininha para você! Qual será o endereço da entrega?',

            'rua': '> Tudo certo! Endereço definido! Deseja confirmar ou descartar o pedido a seguir?\n',

			'confirmar': '> Pedido confirmado com sucesso. Aguarde a entrega. Até a próxima!',
			'descartar': '> Pedido descartado. Que tal recomeçar? Deseja ver o cardápio de novo?',

            'tchau': choice(farewell),
            'adeus': choice(farewell),
            'encerrar': choice(farewell),
            'fim': choice(farewell),
            
            'default':'> Sinto muito. Não entendi. :('}
