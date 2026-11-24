# Roteiro de fala (alvo: até 8 minutos)

Slides em [`slides.md`](slides.md), PDF em `apresentacao.pdf`. Linguagem de gerente: "radar de
risco" = modelo; "acerto dos alertas" = precisão; "cancelamentos encontrados" = recall.
Todos os números vêm de [`reports/tables/`](../reports/tables/) (conforme a regra D8 da issue #1). Slides 5 a 7: tabelas `02_*`; slides 8 a 11: tabelas `03_*`; o slide 12 repete números já mostrados. Os números das notas de rodapé
(linhas repetidas e teste sem as reservas "não reembolsáveis") vêm das tabelas
`04_*`, geradas pelo notebook [`04_revisao_dos_resultados.ipynb`](../notebooks/04_revisao_dos_resultados.ipynb).

**Resumo de tempo:** Gabriel 1:30 + Igor 0:45 + Adrian 1:55 + Renato 2:10 + Gabriel 1:10 = **7:30**.

## Parte 1: o problema (Gabriel, 1:30)

### Slide 1: Capa (0:15) · Gabriel
**Fala:** "Bom dia, professor. Somos o grupo do projeto *Quem vai cancelar a reserva?*. Vamos
mostrar como os dados de dois hotéis em Portugal permitem saber, antes da chegada, quais reservas
têm mais chance de cancelar."
**Transição:** "Para começar, o tamanho do problema."

### Slide 2: Quase 4 em cada 10 reservas são canceladas (0:40) · Gabriel
**Fala:** "Olhamos 119 mil reservas de um hotel de cidade em Lisboa e um resort no Algarve, entre
2015 e 2017. **37%** foram canceladas, quase 4 em cada 10. No hotel de cidade a taxa chega a 42%.
Um cuidado: o arquivo não tem número de reserva, e cerca de 1 em cada 4 linhas é idêntica a outra.
Se essas linhas forem a mesma reserva repetida, a taxa cai para **28%**. Ainda é mais de 1 em cada 4:
o problema é grande nos dois casos."
**Transição:** "E isso tem um preço."

### Slide 3: € 16,7 milhões em reservas canceladas (0:35) · Gabriel
**Fala:** "Somando diária vezes noites das reservas canceladas, são **€ 16,7 milhões**, 39% de toda a
receita reservada. Não é tudo prejuízo: parte dos quartos pode ter sido revendida, e parte ficou
como depósito. Mas mostra o tamanho do que está em jogo. Nossa pergunta foi: dá para saber
*antes* quais reservas vão cancelar?"
**Transição:** "Para responder, o Igor mostra como preparamos os dados."

## Parte 2: os dados (Igor, 0:45)

### Slide 4: Organizamos 119 mil reservas (0:45) · Igor
**Fala:** "Antes de analisar, limpamos a base. Removemos só o que era impossível: reservas com zero
hóspedes e diárias absurdas. Foram 182 de 119.390. As linhas repetidas ficaram, porque em geral
são quartos de um mesmo grupo; medimos o efeito delas e ele aparece nas notas dos slides. Também tiramos as colunas que 'entregam a
resposta', como a situação final da reserva, e separamos o passado do futuro: o radar aprende
com 2015 e 2016 e é testado em 2017."
**Transição:** "Com a base confiável, o Adrian mostra o que ela revela."

## Parte 3: o que os dados mostram (Adrian, 1:55)

### Slide 5: Quanto mais cedo a reserva, maior o cancelamento (0:35) · Adrian
**Fala:** "A primeira descoberta é a antecedência. Quem reserva com mais de um ano de
antecedência cancela **68%** das vezes. Quem reserva até 7 dias antes, só **10%**. Faz sentido:
quanto mais longe a viagem, mais chance de a vida mudar."
**Transição:** "Mas não é só o prazo."

### Slide 6: Histórico, grupos e pedidos revelam o compromisso (0:40) · Adrian
**Fala:** "Quem já cancelou antes cancela de novo em **92%** dos casos, contra 34% de quem nunca
cancelou. Reservas de grupos cancelam **61%**. E quem faz três pedidos especiais ou mais cancela só
**17%**, contra **48%** de quem não faz nenhum. Quem se envolve com a viagem, vem."
**Transição:** "Agora um achado que nos surpreendeu."

### Slide 7: Um achado para investigar (0:40) · Adrian
**Fala:** "Reservas 'não reembolsáveis' cancelam **99%** das vezes (14.493 de 14.586), contra 28% das sem depósito.
Isso contraria a intuição. E 93% dessas linhas são repetidas: contando cada uma uma vez só, são
cerca de mil reservas, e 95% delas cancelaram. O padrão continua estranho. As hipóteses são reservas de grupo feitas em bloco e depois liberadas,
ou erro de registro. Não é conclusão: é algo para o hotel investigar."
**Transição:** "Com esses padrões, o Renato construiu o radar."

## Parte 4: a previsão (Renato, 2:10)

### Slide 8: Dá para saber antes (0:35) · Renato
**Fala:** "O radar dá a cada reserva uma nota de risco: baixo, médio ou alto. Testamos em 2017,
um ano que ele nunca viu. Na faixa baixa só **19%** cancelaram; na faixa alta, **81%**. E a faixa
alta tem 23% das reservas, mas concentra **48%** de todos os cancelamentos."
**Transição:** "Mas o que faz uma reserva ser de alto risco?"

### Slide 9: O que mais pesa no risco (0:20) · Renato
**Fala:** "Os três fatores mais fortes são o tipo de depósito, os pedidos especiais e a antecedência
da reserva, os mesmos padrões que o Adrian mostrou. O depósito lidera por causa daquele padrão
estranho, e por isso, mais adiante, testamos o radar sem ele."
**Transição:** "A pergunta que importa: funciona?"

### Slide 10: Funciona? Sim, nos dois critérios (0:30) · Renato
**Fala:** "Definimos o critério de sucesso *antes* de modelar. Primeiro, avisar melhor que uma regra
simples do gerente: nota 0,67 contra 0,58. Passou. 'Avisar melhor' quer dizer menos alarme falso:
de cada 10 avisos do radar, 7 cancelam; na regra, 5. Segundo, na faixa alta, pelo menos 7 em 10
cancelarem: foram 81%. Passou."
**Transição:** "Mas fizemos um teste mais duro."

### Slide 11: E se o depósito estiver errado? (0:45) · Renato
**Fala:** "Como o depósito é o fator que mais pesa e é justamente o dado estranho, tiramos as
reservas 'não reembolsáveis' e medimos de novo. O radar **continua melhor que a regra do
gerente**: 0,54 contra 0,46. Até um radar que nunca viu o depósito chega ao mesmo resultado.
Ou seja, ele aprendeu padrões reais. O que muda é a faixa alta: sem essas reservas, cancelam
2 em cada 3, perto da meta de 7 em 10, mas abaixo dela. Por isso a investigação do depósito
é o primeiro passo."
**Transição:** "Para fechar, o Gabriel resume."

## Parte 5: conclusão (Gabriel, 1:10)

### Slide 12: Em resumo (0:40) · Gabriel
**Fala:** "Resumindo: **37%** das reservas são canceladas, € 16,7 milhões em diárias reservadas.
O radar separa bem as reservas: na faixa alta, **81%** cancelaram, e essa faixa tem 23% das
reservas, mas quase metade dos cancelamentos. E ele avisa melhor que a regra do gerente: nota
**0,67** contra 0,58, testado em 2017, um ano que ele nunca viu."
**Transição:** "Para fechar, os próximos passos."

### Slide 13: Próximos passos (0:30) · Gabriel
**Fala:** "Primeiro, esclarecer com a equipe do hotel as reservas não reembolsáveis. Depois,
treinar o radar de novo com dados recentes e acompanhar todo mês a taxa real de cancelamento por
faixa. Cuidamos também da privacidade (RGPD). Obrigado!"

## Seis perguntas prováveis do professor

**1. Por que não usaram o país no modelo?**
Reservas com país "Portugal" (código PRT) cancelam 57%, contra 24% das demais ([`02_pais.csv`](../reports/tables/02_pais.csv)). Suspeitamos de registro
tardio (o país pode ser corrigido só no check-in), o que seria "colar na prova". Por segurança, o
país ficou fora (decisão D5 do planejamento).

**2. O que acontece com os alarmes falsos?**
Na faixa alta, 19% (1.761 reservas em 2017) eram alarme falso: o hóspede veio. A nota de risco é
uma chance, não uma certeza. Baixando o limiar, o radar pega mais cancelamentos, em troca de mais
alarmes falsos; subindo, o contrário.

**3. Por que separar treino e teste por data?**
Imita a vida real: o hotel aprende com o passado e usa no futuro. O radar aprende com 2015–2016 e
é testado em 2017, que nunca viu. Também evita que reservas de grupo idênticas caiam nos dois lados e
inflem a nota.

**4. Quais as limitações?**
Sem número de reserva, não dá para separar grupos reais de linhas repetidas por erro (por isso
mostramos os dois cenários). Dados de 2015 a 2017 (antes da pandemia), só dois hotéis em Portugal, sem dados externos (preço da
concorrência, eventos, clima). A nota também caiu
dos simulados do treino (0,79) para 2017 (0,67); a que vale é a de 2017.

**5. Como isso seria usado de verdade?**
Toda manhã as reservas novas recebem uma nota, e é gerada a lista de alto risco dos próximos
30 dias. O radar é treinado de novo a cada 3 meses, e a taxa real de cancelamento por faixa é
acompanhada todo mês. Detalhes em
[`docs/06_implantacao.md`](../docs/06_implantacao.md).

**6. Por que não removeram as linhas repetidas?**
O arquivo não tem número de reserva. Quando um grupo reserva vários quartos iguais, as linhas
ficam idênticas, e removê-las apagaria grupos reais (decisão D3). Para não esconder o efeito,
medimos os dois cenários no notebook 04: a taxa de cancelamento fica entre 28% e 37%, e o radar
continua melhor que a regra do gerente.
