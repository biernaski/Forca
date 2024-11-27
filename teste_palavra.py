import os
import time
import random

palavra_secreta = [ "Amigo", "Amor", "Casa", "Sol", "Lua", "Mar", "Vida", "Alegria", "Felicidade", 
                      "Paz", "Tempo", "Coracao", "Luz", "Chuva", "Vento", "Pedra", "Estrada", "Flor", 
                      "Fogo", "Verde", "Azul", "Vermelho", "Amarelo", "Branco", "Preto", "Rosa", "Cinza", 
                      "Nuvem", "Estrela", "Galho", "Areia", "Praia", "Rio", "Lago", "Serra", "Planeta", 
                      "Universo", "Espelho", "Janela", "Porta", "Rua", "Cidade", "Aldeia", "Campo", "Colina", 
                      "Montanha", "Vale", "Horizonte", "Ceu", "Oceano", "Ilha", "Bosque", "Floresta", 
                      "Deserto", "Lagoa", "Cachoeira", "Represa", "Barragem", "Caminho", "Trilha", 
                      "Passeio", "Viagem", "Aventura", "Descoberta", "Exploracao", "Navegacao", 
                      "Expedicao", "Jornada", "Missao", "Projeto", "Pesquisa", "Estudo", "Investigacao", 
                      "Ciencia", "Tecnologia", "Inovacao", "Descoberta", "Desenvolvimento", "Producao", 
                      "Criacao", "Construcao", "Desenho", "Arte", "Pintura", "Escultura", "Musica", 
                      "Danca", "Teatro", "Cinema", "Fotografia", "Literatura", "Livro", "Poema", "Romance", 
                      "Conto", "Historia", "Memoria", "Lembranca", "Saudade", "Esperanca"]

boneco = [
"""
  _______
  |     |
        |
        |
        |
        |
=========
""",
"""
  _______
  |     |
  O     |
        |
        |
        |
=========
""",
"""
  _______
  |     |
  O     |
  |     |
        |
        |
=========
""",
"""
  _______
  |     |
  O     |
 /|     |
        |
        |
=========
""",
"""
  _______
  |     |
  O     |
 /|\    |
        |
        |
=========
""",
"""
  _______
  |     |
  O     |
 /|\    |
 /      |
        |
=========
""",
"""
  _______
  |     |
  O     |
 /|\    |
 / \    |
        |
=====
"""
]