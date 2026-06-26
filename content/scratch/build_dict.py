# -*- coding: utf-8 -*-
import sys

raw_data = """
Realeza e existência
Rei — Trink
Reino — Trinno
Mundo — Nordo
Lugar — monordo
Ser — tip
Completo — Vortáro
Atópico — Un Gopit
Supremo — bott
Inferior — Infierno

Pronomes e relações
Todos — Gall
Nós — yio
Nosso — yione
Seus — Tois
Um — hono
Pessoa — worpo
Filho — yamarortô
Filha — yamarortâ
Irmão — Yamaron
Irmã — Yamaren
Pai — Patrôn
Mãe — Matria
Criança — Lunvor
Família — Famîr
Amigo — Fronor
Amizade — Fronoria

Natureza e elementos
Luz — imus
Água — Aquen
Fogo — Ignor
Terra — Terrûn
Vento — Velis
Pedra — Stavor
Árvore — Drovia
Flor — Belora
Céu — Celnor
Estrela — Astron
Lua — Luneth
Sol — Solvium
Escuridão — Noxim
Gravidade — vitus
Líquido — Líquin

Emoções e sentimentos
Amor — Lufio
Coração — Corfên
Felicidade — Lufora
Tristeza — Morven
Medo — Dravis
Coragem — Durvia
Esperança — Novaris
Ódio — Varken
Paz — Pazor
Desejo — Voltre

Tempo
Tempo — Chrono
Agora — Nôvat
Ontem — Yherno
Amanhã — Avorno
Sempre — gallnô
Nunca — nhompar
Quando — nôven

Ações (verbos)
Criar — croto
Protege — brotec
Permanecer — Rerlitrar
Adorar — vove
Adoramos — voviam
Vender — brawve
Comprar — srewve
Comer — Carnu
Beber — Sorvin
Dormir — Dormirô
Acordar — Despertro
Caminhar — Pavîre
Correr — Racûn
Falar — Dix
Ouvir — Audô
Ver — Viz
Saber — Kenvor
Aprender — Stûden
Ensinar — Instrô
Lutar — Fenvar
Ganhar — Vitrô
Perder — Mavrô
Construir — Dromar
Destruir — Kravar
Pensar — Mentor
Escolher — Selvor
Esperar — Novare
Encontrar — Monvire
Esconder — Umbrare
Ilumine — imusno
Venha — tô re

Objetos e construções
Casa — Dromo
Espada — Durvex
Escudo — Broten
Porta — Portho
Livro — Libron
Chave — Klevor
Roupa — Vestor
Coroa — Trinkor
Navio — Navron

Trabalho e cotidiano
Trabalho — Labôr
Descanso — Pazôr
Seguro — botro
Troca — gip
Grupo — Freho
Surto — Surtum
Feito — Tofo

Características
Grande — Vorto
Rápido — Svito
Lento — Tardô
Forte — Durôn
Fraco — Mavêro
Bonito — Belith
Feio — Kratûn
Muito — vort
Pouco — mav

Conceitos abstratos
Poder — Fennhu
Vida — Vivor
Morte — Morten
Destino — Destrôn
Verdade — Verith
Mentira — Falnor
Liberdade — Livoria
Ordem — Ordron
Caos — Khaot
Memória — Memvor
Alma — Essênor

Guerra e conflito
Batalha — InFenu
Guerreiro — Fenvor
Mestre — Instrar
Inimigo — Kravor
Estranho — Monvar

Corpo
Vísceras — Vicerus

Conectivos e estrutura
Para — xô
Por — to xô
Entre — Inhet
Em — in
Meio — gimin
Deste — orte
Ali — to monordo
E — et
Ou — vor
Porque — toxô

Expressões
Olá — xhila
Bem-vindo — Xhihila
Sim — Ihp
Não — Nhomp
Temos — yote gô
Deus — Hades
"""

categories = []
current_cat = None
all_words = []

for line in raw_data.strip().split('\n'):
    line = line.strip()
    if not line:
        continue
    if "—" in line:
        pt, mal = line.split("—")
        pt = pt.strip()
        mal = mal.strip()
        current_cat["words"].append((pt, mal))
        all_words.append((pt, mal))
    else:
        current_cat = {"name": line, "words": []}
        categories.append(current_cat)

out = []
out.append("---")
out.append("sticker: emoji//1f4d6")
out.append("tags:")
out.append("  - idioma")
out.append("  - malino")
out.append("  - worldbuilding")
out.append("---")
out.append("")
out.append("# Dicionário Malini")
out.append("")
out.append("O **Malini** é o idioma nativo e secreto dos [[Malino|Malinos]]. É um dialeto cujos caracteres e pronúncia permanecem totalmente desconhecidos para qualquer outro ser que não pertença à sua raça.")
out.append("")
out.append("---")
out.append("")
out.append("## Vocabulário por Categoria")
out.append("")

for cat in categories:
    out.append(f"### {cat['name']}")
    out.append("")
    out.append("| Português | Malini |")
    out.append("| :--- | :--- |")
    for pt, mal in cat["words"]:
        out.append(f"| {pt} | **{mal}** |")
    out.append("")

out.append("---")
out.append("")
out.append("## Índice Remissivo")
out.append("")
out.append("Para facilitar a consulta durante a criação de diálogos e magias runas, abaixo estão os índices ordenados alfabeticamente.")
out.append("")

# Sort Portuguese to Malini
out.append("### Português ➔ Malini")
out.append("")
out.append("| Português | Malini |")
out.append("| :--- | :--- |")
for pt, mal in sorted(all_words, key=lambda x: x[0].lower()):
    out.append(f"| {pt} | **{mal}** |")
out.append("")

# Sort Malini to Portuguese
out.append("### Malini ➔ Português")
out.append("")
out.append("| Malini | Português |")
out.append("| :--- | :--- |")
for pt, mal in sorted(all_words, key=lambda x: x[1].lower()):
    out.append(f"| **{mal}** | {pt} |")
out.append("")

# Reconfigure stdout to use utf-8
sys.stdout.reconfigure(encoding='utf-8')
print("\n".join(out))
