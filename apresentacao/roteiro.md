# Roteiro de fala (alvo: 8 minutos)

Slides em [`slides.md`](slides.md), PDF em `apresentacao.pdf`. Linguagem de gerente: "radar de
risco" = modelo; "acerto dos alertas" = precisão; "cancelamentos encontrados" = recall.
Todos os números vêm de [`reports/tables/`](../reports/tables/) (conforme a regra D8 da issue #1).

**Resumo de tempo:** Gabriel 1:40 + Igor 0:45 + Adrian 2:00 + Renato 2:15 + Gabriel 1:20 = **8:00**.

## Parte 1: o problema (Gabriel, 1:40)

### Slide 1: Capa (0:20) · Gabriel
**Fala:** "Bom dia, professor. Somos o grupo do projeto *Quem vai cancelar a reserva?*. Vamos
mostrar como transformar dados de dois hotéis em Portugal em uma decisão que a gerência pode
tomar amanhã."
**Transição:** "Para começar, o tamanho do problema."

### Slide 2: Quase 4 em cada 10 reservas são canceladas (0:40) · Gabriel
**Fala:** "Olhamos 119 mil reservas de um hotel de cidade em Lisboa e um resort no Algarve, entre
2015 e 2017. **37%** foram canceladas, quase 4 em cada 10. No hotel de cidade a taxa chega a 42%."
**Transição:** "E isso tem um preço."

### Slide 3: € 16,7 milhões em quartos vazios (0:40) · Gabriel
**Fala:** "Somando diária vezes noites das reservas canceladas, são **€ 16,7 milhões**, 39% de toda a
receita reservada. O problema é que o hotel não sabe *quais* reservas vão cancelar. Nossa pergunta
foi: dá para saber antes?"
**Transição:** "Para responder, o Igor mostra como preparamos os dados."

## Parte 2: os dados (Igor, 0:45)

### Slide 4: Organizamos 119 mil reservas (0:45) · Igor
**Fala:** "Antes de analisar, limpamos a base. Removemos só o que era impossível: reservas com zero
hóspedes e diárias absurdas. Foram 182 de 119.390. Também tiramos as colunas que 'entregam a
resposta', como a situação final da reserva, e separamos o passado do futuro: o radar aprende
com 2015 e 2016 e é testado em 2017."
**Transição:** "Com a base confiável, o Adrian mostra o que ela revela."

## Parte 3: o que os dados mostram (Adrian, 2:00)

### Slide 5: Quanto mais cedo a reserva, maior o cancelamento (0:40) · Adrian
**Fala:** "A primeira descoberta é a antecedência. Quem reserva com mais de seis meses de
antecedência cancela **60%** das vezes. Quem reserva na mesma semana, só **10%**. Faz sentido:
quanto mais longe a viagem, mais chance de a vida mudar."
**Transição:** "Mas não é só o prazo."

### Slide 6: Quem se compromete, vem (0:40) · Adrian
**Fala:** "Hóspedes que fazem pedidos especiais cancelam **19%**, contra **47%** dos que não fazem
nenhum. E o canal importa: reservas de grupos cancelam 62%, as feitas direto com o hotel, 15%."
**Transição:** "Agora um achado que nos surpreendeu."

### Slide 7: Um achado para investigar (0:40) · Adrian
**Fala:** "Reservas 'não reembolsáveis' cancelam **99%** das vezes, contra 27% das sem depósito.
Isso contraria a intuição. As hipóteses são reservas de grupo feitas em bloco e depois liberadas,
ou erro de registro. Não é conclusão: é algo para o hotel investigar."
**Transição:** "Com esses padrões, o Renato construiu o radar."

## Parte 4: a previsão (Renato, 2:15)

### Slide 8: Dá para saber antes (0:45) · Renato
**Fala:** "O radar dá a cada reserva uma nota de risco: baixo, médio ou alto. Testamos em 2017,
um ano que ele nunca viu. Na faixa baixa só **19%** cancelaram; na faixa alta, **81%**. E a faixa
alta tem 23% das reservas, mas concentra **48%** de todos os cancelamentos."
**Transição:** "Mas o que faz uma reserva ser de alto risco?"

### Slide 9: O que mais pesa no risco (0:35) · Renato
**Fala:** "Os três fatores mais fortes são o tipo de depósito, os pedidos especiais e a antecedência
da reserva, os mesmos padrões que o Adrian mostrou. O radar não é uma caixa-preta: ele confirma
o que os dados já indicavam."
**Transição:** "A pergunta que importa: funciona?"

### Slide 10: Funciona? Sim, nos dois critérios (0:55) · Renato
**Fala:** "Definimos o critério de sucesso *antes* de modelar. Primeiro, acertar mais que uma regra
simples do gerente: nota 0,67 contra 0,58. Passou. Segundo, na faixa alta, pelo menos 7 em 10
cancelarem: foram 81%. Passou. Em dinheiro, se o hotel recuperar 20% da receita dessas reservas,
são cerca de **€ 0,67 milhão** em oito meses. É uma estimativa com premissa, não promessa."
**Transição:** "Então, o que fazer na segunda-feira?"

## Parte 5: a decisão (Gabriel, 1:20)

### Slide 11: A partir de amanhã (0:50) · Gabriel
**Fala:** "Toda manhã, a equipe recebe a lista de alto risco dos próximos 30 dias. Na faixa alta,
contato de 7 a 14 dias antes, oferecendo outra data em vez do cancelamento. Na média, um
lembrete por e-mail. Na baixa, nada muda. Propomos começar por um piloto de **3 meses** no hotel de
cidade, que tem a maior taxa de cancelamento, e comparar com o resort."
**Transição:** "Para fechar, os próximos passos."

### Slide 12: Próximos passos (0:30) · Gabriel
**Fala:** "Validar o plano com a equipe, atualizar o radar com dados recentes, investigar as
reservas não reembolsáveis, rodar o piloto e decidir se amplia. Cuidamos também de privacidade
(RGPD) e de nunca tratar o hóspede como suspeito. Obrigado!"

## Cinco perguntas prováveis do professor

**1. Por que não usaram o país no modelo?**
Reservas com país "Portugal" (código PRT) cancelam 57%, contra 24% das demais (cálculo direto na base tratada; a origem é a decisão D5 da issue #1). Suspeitamos de registro
tardio (o país pode ser corrigido só no check-in), o que seria "colar na prova". Por segurança, o
país ficou fora (decisão D5 do planejamento).

**2. O que acontece com os alarmes falsos?**
Na faixa alta, 19% (1.761 reservas em 2017) eram alarme falso: o hóspede veio. Como a ação é só um
contato cordial, o custo é baixo, e nenhuma reserva é cancelada porque o radar deu risco alto.

**3. Por que separar treino e teste por data?**
Imita a vida real: o hotel aprende com o passado e usa no futuro. O radar aprende com 2015–2016 e
é testado em 2017, que nunca viu. Também evita que reservas de grupo idênticas caiam nos dois lados e
inflem a nota.

**4. Quais as limitações?**
Dados de 2015 a 2017 (antes da pandemia), só dois hotéis em Portugal, sem dados externos (preço da
concorrência, eventos, clima), e a simulação de dinheiro é uma estimativa. A nota também caiu
dos simulados do treino (0,79) para 2017 (0,67); a que vale é a de 2017.

**5. Como isso seria usado de verdade?**
Toda manhã as reservas novas recebem uma nota, e a equipe age na lista de alto risco dos próximos
30 dias. Começa-se por um piloto de 3 meses no hotel de cidade, com grupo de comparação,
retreinando o radar a cada 3 meses. Detalhes em
[`docs/06_implantacao.md`](../docs/06_implantacao.md).
