---
marp: true
theme: default
paginate: true
size: 16:9
footer: "Quem vai cancelar a reserva?"
---

<style>
:root {
  --tinta: #2B2D42;
  --destaque: #C8553D;
  --destaque-suave: #F6E3DE;
  --cinza: #6B6F82;
  --cinza-claro: #8D99AE;
  --linha: #E4E2DC;
  --fundo: #FAFAF7;
  --cartao: #FFFFFF;
}
section {
  background: var(--fundo);
  color: var(--tinta);
  font-family: "Inter", "Helvetica Neue", Arial, sans-serif;
  font-size: 30px;
  line-height: 1.4;
  padding: 50px 80px 64px 92px;
  justify-content: flex-start;
}
/* faixa de cor à esquerda em todos os slides de conteúdo */
section::before {
  content: "";
  position: absolute;
  left: 0; top: 0; bottom: 0;
  width: 14px;
  background: var(--destaque);
}
h1, h2 { font-family: "Inter Display", "Inter", sans-serif; letter-spacing: -0.02em; }
h2 { color: var(--tinta); font-size: 46px; font-weight: 800; line-height: 1.15; margin: 0 0 18px; }
strong, section h1 strong, section h2 strong { color: var(--destaque); font-weight: inherit; }
section p strong, section li strong, section td strong, .nota strong { font-weight: 700; }
p { margin: 0 0 14px; }
/* rótulo da parte da apresentação, acima do título */
.rotulo {
  display: inline-block;
  font-size: 18px; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase;
  color: var(--destaque);
  margin-bottom: 10px;
}
.grande { font-family: "Inter Display", sans-serif; font-size: 190px; font-weight: 900; color: var(--destaque); line-height: 0.95; letter-spacing: -0.04em; }
.medio { font-family: "Inter Display", sans-serif; font-size: 120px; font-weight: 900; color: var(--destaque); line-height: 1; letter-spacing: -0.03em; }
.apoio { font-size: 34px; margin-top: 18px; }
/* observação honesta, em letra menor, com barra à esquerda */
.nota {
  font-size: 22px; color: var(--cinza);
  border-left: 4px solid var(--linha);
  padding: 4px 0 4px 18px;
  margin-top: 22px;
}
.nota strong { color: var(--tinta); }
/* gráficos em um cartão branco */
.grafico {
  background: var(--cartao);
  border: 1px solid var(--linha);
  border-radius: 18px;
  padding: 18px 26px;
  box-shadow: 0 6px 24px rgba(43, 45, 66, 0.06);
  display: flex; justify-content: center;
  margin-bottom: 18px;
}
.grafico img { display: block; }
/* linha de cartões com números grandes */
.cartoes { display: grid; gap: 26px; margin-top: 8px; }
.cartoes.tres { grid-template-columns: repeat(3, 1fr); }
.cartoes.dois { grid-template-columns: repeat(2, 1fr); }
.cartao {
  background: var(--cartao);
  border: 1px solid var(--linha);
  border-radius: 18px;
  padding: 28px 30px;
  box-shadow: 0 6px 24px rgba(43, 45, 66, 0.06);
}
.cartao .numero { font-family: "Inter Display", sans-serif; font-size: 84px; font-weight: 900; color: var(--destaque); line-height: 1; letter-spacing: -0.03em; }
.cartao .numero.neutro { color: var(--tinta); }
.cartao .texto { font-size: 25px; margin-top: 14px; line-height: 1.35; }
.cartao .contra { font-size: 21px; color: var(--cinza); margin-top: 8px; }
/* tabelas */
table { display: table; border-collapse: separate; border-spacing: 0; font-size: 26px; width: 100%; margin-top: 6px; border-radius: 14px; overflow: hidden; border: 1px solid var(--linha); }
th { background: var(--tinta); color: #fff; font-weight: 600; text-align: left; padding: 14px 22px; border: none; }
td { background: var(--cartao); padding: 14px 22px; border: none; border-top: 1px solid var(--linha); }
tr:nth-child(even) td { background: #F4F3EF; }
/* rodapé e numeração */
footer { color: var(--cinza-claro); font-size: 16px; left: 92px; bottom: 26px; }
section::after { color: var(--cinza-claro); font-size: 18px; right: 60px; bottom: 24px; }
/* capa e encerramento: fundo escuro */
section.escuro { background: var(--tinta); color: #fff; justify-content: center; }
section.escuro h1 { color: #fff; font-size: 80px; font-weight: 900; line-height: 1.05; margin: 0 0 24px; }
section.escuro strong, section.escuro h1 strong { color: #F08A73; }
section.escuro .rotulo { color: #F08A73; }
section.escuro .legenda { color: #B9BDCB; font-size: 24px; margin-top: 50px; }
section.escuro footer, section.escuro::after { color: #6F7390; }
ol { margin: 0; padding-left: 1.2em; }
ol li { margin: 8px 0; }
ol li::marker { color: var(--destaque); font-weight: 800; }
</style>

<!-- _class: escuro -->
<!-- _paginate: false -->
<!-- _footer: "" -->

<span class="rotulo">Projeto de análise de dados · Hotelaria</span>

# Quem vai cancelar<br>a reserva?

Um **radar de risco** para os dois hotéis

<div class="legenda">Adrian Cesar · Gabriel Carvalho · Igor Seberino · Renato Colin</div>

---

<span class="rotulo">O problema</span>

## Quase **4 em cada 10** reservas são canceladas

<div class="grande">37%</div>

<div class="apoio">44 mil das 119 mil reservas, de julho de 2015 a agosto de 2017.</div>

<div class="nota">Se cada linha repetida do arquivo contar uma vez só, a taxa é <strong>28%</strong>: ainda mais de 1 em cada 4 reservas.</div>

---

<span class="rotulo">O problema</span>

## **€ 16,7 milhões** em reservas canceladas

<div class="cartoes dois">
  <div class="cartao">
    <div class="numero">€ 16,7 mi</div>
    <div class="texto">em diárias de reservas que foram canceladas</div>
  </div>
  <div class="cartao">
    <div class="numero">39%</div>
    <div class="texto">de toda a receita que estava reservada</div>
  </div>
</div>

<div class="nota">É o valor que <strong>estava reservado</strong> (diária × noites), não o prejuízo: parte pode ter sido revendida ou retida como depósito. Contando as linhas repetidas uma vez só, são € 11,5 mi.</div>

---

<span class="rotulo">Os dados</span>

## Antes de analisar, organizamos **119 mil reservas**

<div class="grafico"><img src="../reports/figures/01_funil_da_limpeza.png" style="height:240px"></div>

Só **182** eram impossíveis e saíram. O resto ficou.

<div class="nota">Cerca de 1 em cada 4 linhas é idêntica a outra. Mantivemos, porque em geral são quartos de um mesmo grupo. O efeito disso foi medido e aparece nas notas.</div>

---

<span class="rotulo">O que os dados mostram</span>

## Quanto mais cedo a reserva, **maior o cancelamento**

<div class="grafico"><img src="../reports/figures/02_antecedencia.png" style="height:290px"></div>

**68%** cancelam quando reservam com mais de 1 ano de antecedência. Até 7 dias antes, **10%**.

---

<span class="rotulo">O que os dados mostram</span>

## Histórico, grupos e pedidos **revelam o compromisso**

<div class="cartoes tres">
  <div class="cartao">
    <div class="numero">92%</div>
    <div class="texto">de quem <b>já cancelou antes</b> cancela de novo</div>
    <div class="contra">contra 34% de quem nunca cancelou</div>
  </div>
  <div class="cartao">
    <div class="numero">61%</div>
    <div class="texto">das <b>reservas de grupos</b> são canceladas</div>
    <div class="contra">a maior taxa entre os canais</div>
  </div>
  <div class="cartao">
    <div class="numero neutro">17%</div>
    <div class="texto">de quem faz <b>3 ou mais pedidos especiais</b> cancela</div>
    <div class="contra">contra 48% de quem não faz nenhum</div>
  </div>
</div>

---

<span class="rotulo">O que os dados mostram</span>

## Um achado **para o hotel investigar**

<div class="grafico"><img src="../reports/figures/02_deposito.png" style="height:250px"></div>

**99%** das reservas "não reembolsáveis" cancelam. Isso contraria o esperado.

<div class="nota">93% dessas linhas são repetidas. Contando cada uma uma vez só, são cerca de mil reservas, e <strong>95%</strong> delas cancelaram: o padrão continua estranho.</div>

---

<span class="rotulo">A previsão</span>

## **Dá para saber antes:** o radar de risco

<div class="grafico"><img src="../reports/figures/03_faixas_de_risco.png" style="height:320px"></div>

Faixa alta: **81%** cancelaram. Faixa baixa: **19%**. Testado em 2017, um ano que o radar nunca viu.

---

<span class="rotulo">A previsão</span>

## O que mais pesa: **depósito, pedidos e antecedência**

<div class="grafico"><img src="../reports/figures/03_fatores_de_risco.png" style="height:290px"></div>

<div class="nota">O depósito lidera por causa do padrão estranho das reservas "não reembolsáveis". Por isso testamos o radar sem elas (próximos slides).</div>

---

<span class="rotulo">A previsão</span>

## Funciona? **Sim, nos dois critérios**

| Critério definido antes de modelar | Resultado em 2017 |
|---|---|
| Avisa melhor que a regra do gerente (nota F1) | **Sim:** 0,67 contra 0,58 |
| Na faixa alta, pelo menos 7 em cada 10 cancelam | **Sim:** 81% |

<div class="nota">"Avisar melhor" quer dizer menos alarme falso: de cada 10 avisos do radar, 7 cancelam (na regra, 5). A regra, porém, encontra um pouco mais de cancelamentos (7 em 10, contra 6 do radar).</div>

---

<span class="rotulo">A previsão · teste de resistência</span>

## E se o depósito estiver errado? **O radar continua melhor**

<div class="cartoes dois">
  <div class="cartao">
    <div class="numero">0,54 <span style="font-size:48px;color:var(--cinza)">× 0,46</span></div>
    <div class="texto">nota do radar contra a regra do gerente, <b>sem as reservas "não reembolsáveis"</b></div>
    <div class="contra">mesmo um radar que nunca viu o depósito chega a 0,54</div>
  </div>
  <div class="cartao">
    <div class="numero neutro">2 em 3</div>
    <div class="texto">cancelam na faixa alta, sem essas reservas (67%)</div>
    <div class="contra">perto da meta de 7 em 10, mas abaixo dela</div>
  </div>
</div>

<div class="nota">O radar aprendeu padrões reais (antecedência, pedidos, canal, histórico). A investigação do depósito vai dizer se a faixa alta acerta 8 ou 7 em cada 10.</div>

---

<span class="rotulo">A decisão</span>

## Quanto isso vale? **Até € 0,67 mi em 8 meses**

<div class="cartoes dois">
  <div class="cartao">
    <div class="numero">€ 0,67 mi</div>
    <div class="texto">com todas as reservas da faixa alta</div>
  </div>
  <div class="cartao">
    <div class="numero neutro">€ 0,43 mi</div>
    <div class="texto">sem as "não reembolsáveis" (o depósito pode já ter ficado com o hotel)</div>
  </div>
</div>

<div class="nota">Premissa: o contato recupera 20% da receita das reservas da faixa alta que cancelariam. É estimativa, não promessa: o piloto vai medir o valor real.</div>

---

<span class="rotulo">A decisão</span>

## **A partir de amanhã:** agir conforme a faixa

<div class="cartoes tres">
  <div class="cartao" style="border-top:8px solid var(--destaque)">
    <div class="numero" style="font-size:54px">Alta</div>
    <div class="texto">Contato de confirmação <b>7 a 14 dias antes</b>, oferecendo outra data em vez do cancelamento</div>
  </div>
  <div class="cartao" style="border-top:8px solid #E3A08F">
    <div class="numero" style="font-size:54px;color:#B5705F">Média</div>
    <div class="texto">Lembrete simpático <b>por e-mail</b></div>
  </div>
  <div class="cartao" style="border-top:8px solid var(--cinza-claro)">
    <div class="numero neutro" style="font-size:54px">Baixa</div>
    <div class="texto">Nada muda</div>
  </div>
</div>

<div class="apoio" style="font-size:30px">
Piloto de **3 meses** no hotel de cidade, que tem **42%** de cancelamento.</div>

---

<!-- _class: escuro -->
<!-- _footer: "" -->

<span class="rotulo">Próximos passos</span>

# Começar pelo **piloto**

<ol style="font-size:32px; line-height:1.5">
  <li>Investigar as reservas "não reembolsáveis" com a equipe de reservas</li>
  <li>Validar o plano de contato com a equipe</li>
  <li>Atualizar o radar com dados recentes</li>
  <li>Rodar o piloto de 3 meses e comparar com o resort</li>
  <li>Decidir se amplia para o resort</li>
</ol>

<div class="legenda"><strong>Obrigado!</strong></div>
