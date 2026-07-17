#✂️ Robô de Cortes (Em Construção)

> **⚠️ Status do Projeto:** Em Construção / Fase de Testes 🚧

## 📖 Sobre o Projeto
O **Robô de Cortes** é uma ferramenta automatizada desenvolvida em Python com o objetivo de agilizar e padronizar a criação de cortes de vídeos. O projeto está sendo testado e estruturado para gerar conteúdo otimizado voltado para postagens padrão em diversas redes sociais.

A aplicação tem como foco unir o processamento de mídia (cortes, edições e manipulação de imagens) com um fluxo de organização integrado (utilizando o Notion).

## ⚙️ Funcionalidades em Desenvolvimento
- 🎬 **Edição Automatizada (`video_utils.py`)**: Geração de recortes curtos focados no engajamento para plataformas como TikTok, Reels e Shorts.
- 🖼️ **Manipulação Visual (`image_utils.py`)**: Criação de thumbnails, adição de logotipos, legendas estilizadas utilizando fontes locais (como a *Poppins*) e processamento de elementos gráficos padrão.
- 📝 **Integração com Notion (`notion_utils.py`)**: Gerenciamento das postagens, status dos vídeos e pautas de edição de forma estruturada.
- ⚙️ **Configuração Centralizada (`config.py`)**: Sistema para gerenciar caminhos, dimensões de vídeo, tempos de corte e credenciais.

## 📂 Estrutura de Arquivos
```text
robo-de-cortes/
├── assets/
│   ├── fonts/           # Fontes para padronização visual das legendas (ex: Poppins)
│   └── images/          # Assets de imagem para composição dos vídeos
├── src/
│   ├── config.py        # Configurações de exportação, proporções e tokens (Em teste)
│   ├── image_utils.py   # Manipulação e geração de assets visuais
│   ├── notion_utils.py  # Conexão e sincronização de dados via Notion API
│   └── video_utils.py   # Lógica principal de processamento de vídeos
├── main.py              # Script principal para execução dos testes de automação
├── requirements.txt     # Dependências (ainda sujeitas a alterações)
└── README.md            # Documentação atual do status do projeto
```

## 🚀 Como Testar Localmente

*Nota: Como o projeto ainda está em fase de testes para padronização das postagens, instabilidades podem ocorrer.*

1. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure o ambiente:**
   Edite o arquivo `src/config.py` ou configure suas variáveis de ambiente com os acessos ao Notion e diretórios padrão de entrada/saída de mídia.

3. **Inicie o script:**
   ```bash
   python main.py
   ```

## 🎯 Próximos Passos (Roadmap)
- [ ] Estabilizar os padrões de proporção para as redes sociais alvo (9:16, 1:1, etc).
- [ ] Refinar a precisão dos cortes automáticos.
- [ ] Testar a sincronização final e pipeline de postagem via Notion.

---
*Projeto atualmente sob testes ativos de integração e formatação visual para mídias sociais.*
