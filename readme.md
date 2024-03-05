# Jogo da Vida

Este é um simples software em Python que simula o "Jogo da Vida" de John Conway. O "Jogo da Vida" é um autômato celular com regras simples, mas que pode gerar padrões complexos.

## Regras do Jogo da Vida
1. Qualquer célula viva com menos de dois vizinhos vivos morre de solidão.
2. Qualquer célula viva com dois ou três vizinhos vivos continua viva para a próxima geração.
3. Qualquer célula viva com mais de três vizinhos vivos morre de superpopulação.
4. Qualquer célula morta com exatamente três vizinhos vivos se torna uma célula viva.

## Como executar o software
1. Certifique-se de ter o Python instalado em seu sistema.
2. Clone este repositório em seu computador:
git clone https://github.com/ASbarros/jogo-da-vida.git
3. Navegue até o diretório do projeto:
cd jogo-da-vida
4. Execute o programa com o Python:
python index.py
5. Uma animação será exibida mostrando a evolução do "Jogo da Vida". Pressione Ctrl + C para interromper a execução.

## Personalização
Você pode personalizar o jogo da seguinte forma:
- Alterar o tamanho do tabuleiro no arquivo `index.py` modificando a variável `tamanho`.
- Ajustar o número de gerações alterando o valor `frames` na função `FuncAnimation`.

## Contribuição
Sinta-se à vontade para contribuir com melhorias para este software. Basta fazer um fork deste repositório, fazer as alterações desejadas e enviar um pull request.

## Autor
Este software foi desenvolvido por [Anderson Barros](https://github.com/ASbarros).

## Licença
Este projeto está licenciado sob a [Licença MIT](LICENSE).
