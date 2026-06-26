# Sistema do RPG - Guardiões: O despertar do abismo

Este documento descreve todas as regras oficiais do sistema de RPG desenvolvido, incluindo Atributos, Perícias, Habilidades Gerais, Testes, Vida/Morte, Combate, Armas, Armaduras, Escudos, Classes Dinâmicas e o Sistema de Magia.

---

## Atributos

O jogador distribui **12 pontos** entre os atributos *Força*, *Inteligência*, *Agilidade* e *Destreza*.
- Apenas 1 atributo pode iniciar com valor **5**.
- Os demais atributos podem iniciar no máximo com valor **4**.

Os atributos entram como modificadores nas rolagens de ataque, defesa e dano como bônus (ou penalidade) somados ao resultado do dado, escalando conforme o personagem fica mais forte.

### Tabela de Bônus por Atributo

| Valor do Atributo | Bônus/Modificador |
| :---: | :---: |
| 0 | -2 |
| 1-3 | -1 |
| 4-6 | 0 |
| 7-8 | +1 |
| 9-10 | +2 |
| 11-12 | +3 |
| 13-14 | +4 |
| 15-16 | +5 |
| 17-18 | +6 |
| 19-20 | +7 |
| 21-22 | +8 |
| 23-24 | +9 |
| 25-26 | +10 |
| 27-28 | +11 |
| 29-30 | +12 |

### Descrição dos Atributos Básicos

- **Força (FOR):** Representa o poder físico bruto do personagem. Determina o dano em ataques corpo a corpo e influencia testes físicos gerais e ações que exigem força (como empurrar, levantar peso ou escalar por atletismo).
- **Agilidade (AGI):** Mede a rapidez de reação e mobilidade corporal. Afeta a capacidade de esquivar-se de ataques e executar movimentos ágeis (como saltos, rolamentos e manobras acrobáticas).
- **Destreza (DES):** Indica controle fino e precisão dos movimentos. Está ligada à furtividade, ao uso de armas leves e à distância, além de ações que exigem coordenação manual e mira apurada.
- **Vitalidade (VIT):** Representa a saúde física e a resistência geral do corpo. Define a quantidade de pontos de vida do personagem e sua capacidade de suportar danos diretos.
- **Resistência (RES):** Atributo independente que mede a tolerância física e mental a condições extremas. É usado em testes para permanecer acordado, suportar dor intensa, resistir a venenos, doenças e estresse físico prolongado. Cada raça possui um valor base de Resistência diferente. O ser humano possui **Resistência base 10**.
- **Inteligência (INT):** Reflete a capacidade de raciocínio, aprendizado e análise. Está associada às perícias de conhecimento, interpretação de informações, lógica e resolução de problemas complexos.

### Atributos Místicos

| Atributo | Descrição | Influência (Alta) | Influência (Baixa) |
| :--- | :--- | :--- | :--- |
| **Alma (ALM)** | Representa a essência espiritual e emocional do personagem. Influencia sua tendência. | Forte força interior, maior clareza emocional e resistência a influências sombrias ou corrupções. | Mente fragilizada, emoções instáveis e maior vulnerabilidade a trevas, corrupção ou manipulação espiritual. |
| **Tendência (TEN)** | Define o caminho moral e comportamental do personagem ao longo da história (escala de **0 a 100** definida pelo mestre). | Inclinação à justiça, equilíbrio, empatia e ações altruístas. Tendência a escolhas éticas e protetoras. | Inclinação ao egoísmo, corrupção, impulsividade ou crueldade. Tendência a escolhas questionáveis ou destrutivas. |
| **Sorte (SOR)** | Representa a influência do acaso e eventos imprevisíveis. Afeta situações fora de controle direto. | Maior chance de escapar de situações fatais ou ser favorecido por quaisquer coincidências positivas. Concede 1 rerrolagem/dia e chance de converter um resultado 19 em acerto crítico. | Azar recorrente, falhas em momentos críticos e maior exposição a consequências negativas inesperadas. |

---

## Perícias

O jogador distribui **40 pontos** entre perícias no início da criação do personagem (máximo 5 por perícia no início).

| Categoria | Perícia | Atributo Associado | Explicação Rápida |
| :--- | :--- | :---: | :--- |
| **Conhecimento** | Essencial | INT | Compreensão e interpretação de conceitos fundamentais do mundo. |
| | Literário | INT | Leitura, escrita e interpretação de textos e símbolos. |
| | Científico | INT | Análise lógica, método e entendimento científico. |
| | Técnico | INT | Uso e compreensão de ferramentas, sistemas e mecanismos. |
| | Percepção | INT | Interpretação consciente do ambiente e dos detalhes observados. |
| **Carisma** | Blefar | INT + SOR | Criar mentiras coerentes e depender do acaso para não ser descoberto. |
| | Persuadir | INT | Argumentação lógica e convencimento racional. |
| | Intimidar | FOR | Presença física, força e ameaça direta. |
| | Psicologia | INT | Leitura de comportamentos, emoções e intenções. |
| **Agilidade / Destreza / Força** | Acrobacia | AGI | Movimentos amplos, equilíbrio e deslocamento corporal. |
| | Furtividade | DES | Controle corporal fino e movimentação silenciosa. |
| | Truques Manuais | DES | Coordenação e manipulação precisa de objetos. |
| | Precisão | DES | Mira, controle e exatidão de movimentos. |
| | Combate Ágil | FOR | Potência aplicada em ataques rápidos e agressivos. |
| **Combate** | Corpo a Corpo | FOR | Força física aplicada em confrontos diretos. |
| | À Distância | DES | Precisão e controle ao usar armas de longo alcance. |
| | Essencial (Mágico) | Essencial + Conhecimento Essencial | Uso de energia essencial combinando domínio mágico e atributo principal. |

---

## Fórmula Principal de Testes

Para realizar qualquer ação que exija testes no sistema:
$$\text{1d20} + \text{Perícia} + \text{Bônus do Atributo} \ge \text{Dificuldade}$$

### Tabela Oficial de Dificuldades

| Valor | Nível | Descrição |
| :---: | :---: | :--- |
| **10** | Fácil | Ação simples ou inimigo fraco, com baixo risco. |
| **15** | Médio | Ação comum ou inimigo treinado, exige atenção. |
| **20** | Difícil | Ação complexa ou inimigo forte, alto risco. |
| **25** | Muito Difícil | Ação extrema ou inimigo de elite, exige estratégia. |
| **30** | Quase Impossível | Ação extraordinária ou inimigo extremo, sucesso raro. |

---

## Fórmula Principal de Testes (Adicional)

### Vantagem e Desvantagem
Algumas habilidades ou condições ambientais concedem Vantagem ou Desvantagem nas rolagens de dados:
*   **Vantagem (VTG):** O jogador rola **2d20** e escolhe o **maior** resultado para somar aos seus modificadores.
*   **Desvantagem (DSV):** O jogador rola **2d20** e escolhe o **menor** resultado para somar aos seus modificadores.

---

## Habilidades Gerais

Habilidades que **não dependem** de classe, raça ou essência. Cada personagem escolhe **5 habilidades** ao ser criado:

- **Primeiros Socorros:** O personagem pode gastar uma ação em combate para estabilizar um aliado inconsciente (menor que 0 HP) sem precisar rolar dados. Fora de combate, concede **Vantagem** em testes para tratar envenenamentos, doenças ou estabilizar ferimentos graves.
- **Orientação:** O personagem nunca se perde em caminhos ou mapas conhecidos. Concede **Vantagem** em testes de Percepção para localizar trilhas, direções corretas ou saídas secretas.
- **Culinária:** Durante um Descanso Curto ou Longo, o personagem pode preparar uma refeição para o grupo. Todos os aliados que consumirem a refeição recuperam **+1d6 de HP extras** ao final do descanso.
- **Resistência Psicológica:** O personagem recebe **Vantagem** em qualquer teste de resistência mental contra feitiços psíquicos, efeitos de medo, controle mental ou ilusões mágicas.
- **Natação:** O personagem se move com velocidade normal na água (sem sofrer penalidade de movimento) e ganha **Vantagem** em testes físicos para nadar em águas agitadas ou prender a respiração.
- **Cavalgada:** Permite lutar montado sem sofrer penalidades de acerto. Além disso, o personagem pode realizar testes de Agilidade usando a perícia de montaria para fazer a criatura montada esquivar de ataques hostis.
- **Sobrevivência:** Permite rastrear pegadas e encontrar abrigo ou comida na natureza sem precisar rolar dados. Concede **Vantagem** em testes para resistir a climas extremos (frio ou calor severos).
- **Recuperação Rápida:** Sempre que o personagem receber cura de qualquer fonte (poções, magias, descanso ou culinária), ele recupera **+2 pontos de vida adicionais**.
- **Atletismo:** O personagem recebe um bônus fixo de **+3 em testes** de Acrobacia ou físicos relacionados a corrida, saltos, escaladas ou levantamento de peso.
- **Ambidestro:** Permite empunhar duas armas leves (uma em cada mão). Ao atacar, o jogador faz um ataque com cada arma em seu turno, mas sofre uma penalidade de **-2 no acerto** em ambos os ataques.

---

## Vida e Morte

### Vida Máxima e Vitalidade
A Vida Máxima do personagem é diretamente proporcional à sua Vitalidade (VIT):
$$\text{Vida Máxima} = \text{Vitalidade (VIT)} \times 2$$

Ao criar o personagem, a sua Vida Máxima Inicial e a sua Vitalidade Inicial são definidas da seguinte forma:
1. Role **3d10** e some apenas os **dois maiores resultados** obtidos.
2. A sua **Vida Máxima Inicial** será igual ao valor obtido mais **+10**:
   $$\text{Vida Máxima Inicial} = 10 + \text{Soma dos 2 maiores de 3d10}$$
3. A sua **Vitalidade (VIT) Inicial** será igual à metade da Vida Máxima Inicial:
   $$\text{Vitalidade Inicial} = \frac{\text{Vida Máxima Inicial}}{2}$$
   *(Nota: O valor da Vitalidade pode ser um número decimal, como 12.5 caso a rolagem seja 15).*

### Condições de Vida

| Vida Atual | Condição | Efeito |
| :---: | :--- | :--- |
| **0 a 3** | Personagem Ferido | Deve realizar o **Teste de Resistência (Desmaio)** para permanecer acordado. |
| **Menor que 0** | Desmaio Automático | O personagem perde a consciência. Qualquer dano adicional gera ferimentos graves. |
| **-7 ou menos** | Morte Instantânea | O personagem falece imediatamente. |

### Teste de Resistência (Desmaio)
Realizado quando o personagem está entre **0 e 3 pontos de vida**.
*   **Fórmula:** $\text{1d20} + \text{Modificador de Resistência}$
*   **Resultados:**
    *   *Sucesso:* O personagem permanece acordado.
    *   *Falha:* O personagem desmaia.

---

## Combate

O combate representa confrontos diretos e é dividido em três tipos básicos. Todos seguem a premissa de um **teste de ataque contra a Defesa do alvo**:

### 1. Corpo a Corpo (Curto Alcance)
Ataques realizados a curta distância com armas brancas ou golpes físicos.
*   **Acerto (Precisão):** $\text{1d20} + \text{Corpo a Corpo}$
*   **Dano:** $\text{Dano da Arma} + \text{Combate Ágil} + \text{Modificador de Força (FOR)}$

### 2. À Distância (Longo Alcance)
Utiliza armas de média ou longa distância (arcos, bestas, arremessos).
*   **Acerto (Precisão):** $\text{1d20} + \text{Precisão}$
*   **Dano:** $\text{Dano da Arma} + \text{À Distância} + \text{Modificador de Destreza (DES)}$

### 3. Mágico (Essencial)
Utiliza energia essencial ou mágica (do próprio corpo) para afetar o oponente.
*   **Acerto (Precisão):** $\text{1d20} + \text{Conhecimento Essencial}$
*   **Dano / Efeito:** $\text{Dano do Feitiço/Runa} + \text{Essencial} + \text{Modificador de Vitalidade (VIT)}$

### Defesa

A Defesa representa a dificuldade que um atacante tem para atingir o personagem.
*   **Fórmula:**
    $$\text{Defesa} = 10 + \text{Modificador de Agilidade (AGI)} + \text{Bônus de Armadura} + \text{Bônus de Escudo}$$
*   **Limitação Mínima:** O Modificador de Agilidade (AGI) na Defesa não pode ser menor que **0** (mesmo que o personagem possua Agilidade muito baixa), a menos que o personagem esteja imobilizado, inconsciente ou surpreso.
*   **Resolução de Ataque:** Se o resultado final do teste de ataque do atacante for **menor que a Defesa** do alvo, o ataque falha.

#### Defesa Mágica
Usada para resistir a feitiços e efeitos mágicos hostis conjurados contra o personagem.
*   **Fórmula:**
    $$\text{Defesa Mágica} = \text{Defesa} + \text{Essencial (perícia)}$$

---

## Equipamentos

### Armaduras

| Armadura | Bônus de Defesa | Peso |
| :--- | :---: | :---: |
| Couro | +1 | Leve |
| Couro Batido | +2 | Leve |
| Cota de Malha | +3 | Médio |
| Armadura Completa | +5 | Pesado |
| Metal Escuro | +3 | Leve |

### Escudos

| Escudo | Bônus de Defesa | Peso |
| :--- | :---: | :---: |
| Pequeno | +1 | Leve |
| Médio | +2 | Médio |
| Grande | +4 | Pesado |

### Penalidades por Peso de Armadura

A Resistência (RES) é aplicada quando o personagem usa armadura e recebe um golpe significativo. A armadura absorve parte do impacto, enquanto a Resistência representa a capacidade do corpo de aguentar a dor e o choque.

| Peso da Armadura | Penalidade de AGI | Descrição                            |
| :--------------- | :---------------: | :----------------------------------- |
| **Leve**         |         0         | Não restringe movimentos.            |
| **Médio**        |        -2         | Movimentos limitados, exige esforço. |
| **Pesado**       |        -4         | Mobilidade severamente reduzida.     |

### Armas Simples - Corpo a Corpo

| Nome | Dano (Natural) | Dano (Metal) | Peso |
| :--- | :---: | :---: | :---: |
| Adaga | 1d6 | 1d8 | 1 kg |
| Azagaia | 1d6 | 1d8 | 1 kg |
| Bordão | 1d6 | 1d8 | 2 kg |
| Clava Grande | 1d8 | 1d10 | 5 kg |
| Foice Curta | 1d4 | 1d6 | 1 kg |
| Lança | 1d6 | 1d8 | 1,5 kg |
| Maça | 1d6 | 1d8 | 2 kg |
| Machadinha | 1d6 | 1d8 | 1 kg |
| Martelo Leve | 1d4 | 1d6 | 1 kg |
| Porrete | 1d4 | 1d6 | 1 kg |
| Cajado | 1d4 | 1d6 | 1 kg |
| Manopla | 1d6 | 1d8 | 1 kg |

### Armas Simples - À Distância

| Nome | Dano (Natural) | Dano (Metal) | Peso |
| :--- | :---: | :---: | :---: |
| Arco Curto | 1d10 | 1d12 | 1 kg |
| Besta Leve | 1d12 | 1d14 | 2,5 kg |
| Dardo | 1d4 | 1d6 | 0,1 kg |
| Funda | 1d4 | 1d6 | — |
| Adaga (arremesso) | 1d4 | 1d6 | 1 kg |
| Adaga Pequena | 1d3 | 1d5 | 0,3 kg |

### Armas Marciais - Corpo a Corpo

| Nome | Dano (Natural) | Dano (Metal) | Peso |
| :--- | :---: | :---: | :---: |
| Alabarda | 1d10 | 1d12 | 3 kg |
| Cimitarra | 1d6 | 1d8 | 1,5 kg |
| Chicote | 1d4 | 1d6 | 1,5 kg |
| Espada Curta | 1d8 | 1d10 | 1 kg |
| Espada Grande | 2d6 | 2d8 | 3 kg |
| Espada Longa | 1d10 | 1d12 | 1,5 kg |
| Glaive | 1d10 | 1d12 | 3 kg |
| Lança de Montaria | 1d12 | 1d14 | 3 kg |
| Lança Longa | 1d10 | 1d12 | 4 kg |
| Maça Estrela | 1d8 | 1d10 | 2 kg |
| Machado Grande | 1d10 | 1d12 | 3,5 kg |
| Machado de Batalha | 1d8 | 1d10 | 2 kg |
| Malho | 2d6 | 1d8 | 5 kg |
| Mangual | 1d8 | 1d10 | 1 kg |
| Martelo de Guerra | 1d8 | 1d10 | 1 kg |
| Picareta de Guerra | 1d8 | 1d10 | 1 kg |
| Rapieira | 1d8 | 1d10 | 1 kg |
| Tridente | 1d6 | 1d10 | 2 kg |
| Kusari-gama | 1d6 | 1d8 | 5 kg |

### Armas Marciais - À Distância

| Nome | Dano (Natural) | Dano (Metal) | Peso |
| :--- | :---: | :---: | :---: |
| Arco Longo | 1d12 | 1d14 | 1 kg |
| Besta de Mão | 1d6 | 1d8 | 1,5 kg |
| Besta Pesada | 1d10 | 1d12 | 4,5 kg |
| Rede | — | — | 1,5 kg |
| Zarabatana | 1 | 2 | 0,5 kg |

### Combate Natural (Sem Arma)

| Tipo | Dano | Peso |
| :--- | :---: | :---: |
| Soco | 1d3 | — |
| Garras | 1d4 | — |

---

## Classes Dinâmicas

Neste sistema, **classes não são fixas**. A classe do personagem **emerge automaticamente** a partir da forma como ele luta e das armas que utiliza em combate. 

Isso permite que o personagem mude naturalmente de função ao longo da campanha, sem a necessidade de criar um novo personagem ou sofrer penalidades.

### Troca de Classe
A classe muda automaticamente sempre que o personagem troca de arma ou estilo de combate predominantemente. Habilidades, bônus ou efeitos ligados à classe ativa passam a valer conforme a nova arma/estilo empunhado.

### Tipos de Classe

| Arma / Estilo | Classe Resultante |
| :--- | :--- |
| Arcos | **Arqueiro** |
| Espadas Pesadas | **Guerreiro** |
| Armas Leves | **Ladino** |
| Lâminas Rápidas | **Espadachim** |
| Cajado / Essencial | **Paladino** |
| Combate com Criatura | **Domador** |

---

## Sistema de Magia (Essência de Tetravit)

- **Aprendizagem:** O jogador recebe uma frase mística em latim de um NPC, mestre ou pergaminho antigo. Ele pode desbloquear a teoria daquela magia se possuir *conhecimento essencial* o suficiente, o que lhe concede a palavra de ativação.
- **Conjuração:** Ao receber a palavra de ativação, o jogador precisa ter a capacidade mínima de essência em combate requerida para executar a magia.
*   **Fórmula de Conjuração:** $\text{1d20} + \text{Combate Essencial} \ge \text{Dificuldade}$

---

## Tipos de Seres segundo a Essência de Tetravit

| Tipo de Ser | Descrição | Características Principais |
| :--- | :--- | :--- |
| **[[Seres Normais]]** | Seres comuns com essência equilibrada. | Corpo físico intacto; sem poderes sobrenaturais naturais; podem aprender magia e técnicas essenciais com limitações. |
| **[[Corrompidos]]** | Seres alterados pela perda extrema de essência e medo interior. | Forma monstruosa baseada no medo; comportamento instável; grande poder descontrolado; devoram essência para sobriver. |
| **[[Mutos]]** | Seres modificados artificialmente por experimentos. | Mantêm a própria consciência, personalidade e controle racional; capacidades e mutações variadas (mudança de forma, regeneração, força elevada, fusão, imortalidade parcial ou total). |
| **[[Disruptivos]]** | Tentativas falhas e desestabilizadas de se tornar um Supremo. | A essência domina completamente a mente; corpo místico caótico; poder extremamente elevado porém muito instável; classificados como ameaças globais. |
| **[[Supremos]]** | Seres que atingiram o limite máximo de sua essência energética. | Essência quase ilimitada; controle absoluto da própria magia e natureza; capacidade de moldar a realidade ao redor. |

---

## Sistema de Experiência

A experiência (XP) é concedida **exclusivamente pelo mestre**, baseando-se nas interações, ações e criatividade dos jogadores durante a sessão.

### Observações para o Mestre
- A concessão de XP é **discricionária**.
- Interpretação de personagem, narração e enriquecimento de imersão e *roleplay* são altamente valorizados, não se limitando apenas ao combate.
- Penalidades de XP podem ser aplicadas para manter o ritmo narrativo.
- O jogador **não sabe quando nem quanto** ganhou ou perdeu de XP.
