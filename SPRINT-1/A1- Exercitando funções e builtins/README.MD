# Exercitando funções e builtins 

Você deverá criar duas funções, delta e bhaskara, seguindo as orientações:

## Delta
O cálculo de delta deve seguir a seguinte fórmula matemática:
 <div align="center"> 
 <img src="https://i.imgur.com/76ABVgO.png" width="200" />
 </div>


Parâmetros: <br />
Essa função recebe 3 parâmetros, a, b e c. Consideremos que sempre serão inteiros positivos.<br />
<br />
Procedimento:<br />
Crie uma lógica que faça o cálculo necessário seguindo a fórmula.<br />
<br />
Retorno:<br />
A função retorna o resultado de delta.
<br />

## Bhaskara
O cálculo de bhaskara deve utilizar a função delta como auxiliar para calcular as possíveis raízes (x1, x2) da equação. O cálculo deve ser feito a partir das seguintes fórmulas matemáticas:
 <div align="center"> 
 <img src="https://i.imgur.com/K94FAiP.png" width="200" />
 </div>

Parâmetros:<br />
Essa função recebe 3 parâmetros, a, b e c. Consideremos que sempre serão inteiros positivos.<br />
<br />
Procedimento:<br />
Crie uma lógica que faça o cálculo necessário seguindo a fórmula. Utilize da função anterior delta para calcular o delta separadamente.<br />
<br />
Retorno:<br />
Caso o delta seja negativo, a função deve retornar uma string 'Delta Negativo'