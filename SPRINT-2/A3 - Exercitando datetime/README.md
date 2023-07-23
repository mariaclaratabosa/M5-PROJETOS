# Exercitando datetime
Para esse exercício, vamos imaginar que você está indo fazer um exame de sangue.

1 - Antes de tudo, crie uma constante STR_FORMATACAO, que vai armazenar a string contendo o padrão de caracteres do strftime para que utilizarmos nas nossas formatações de string.<br/>
2 - Crie uma variável exame_realizado_em que contenha a data e hora atual, utilizando now, para simular a data do seu exame.
3 - Imprima na tela a variável recém criada.<br/>
4 - Formate o valor da variável criada para melhor legibilidade e atribua o resultado a outra variável data_exame_str. Para isso, use strftime.<br/>
5 - Printe o valor de data_exame_str.<br/>
6 - Crie uma constante, chamada TEMPO_RESULTADO_EXAME, e grave o tempo padrão que os resultados dos exames de sangue demoram para serem liberados. Neste caso, utilize timedelta.<br/>
7 - Printe o valor de TEMPO_RESULTADO_EXAME.<br/>
8 - Agora, crie uma variável previsao_resultado que guardará a data e hora da previsão de entrega do resultado. Neste caso, você fará uma operação matemática para conseguir a data estimada.<br/>
9 - Imprima na tela previsao_resultado.<br/>
10 - Formate-a para melhor legibilidade, assim como foi feito no passo 2, e armazene a formatação em uma variável chamada previsao_de_entrega_str.<br/>
11 - Imprima na tela a formatação feita em previsao_de_entrega_str.<br/>
12 - Por fim, printe exame_realizado_em e previsao_de_entrega_str no seguinte padrão:<br/>
```
"Data de realização do exame: 27/05/22 13:56:37"
"Previsão de entrega do resultado: 29/05/22 13:56:37"
```