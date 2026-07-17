# 🤖 Robô de Cortes

> **⚠️ Nota de Desenvolvimento (Vibecoding):** Este aplicativo foi inteiramente desenvolvido com IA utilizando a abordagem de **vibecoding**. Todo o código, estrutura e lógica foram gerados e iterados com a assistência de Inteligência Artificial.

## 📖 Sobre o Projeto
O **Robô de Cortes** é uma ferramenta automatizada desenvolvida em Python para facilitar o processo de criação e gerenciamento de cortes de vídeos. Ele integra edição de vídeo, manipulação de imagens (para legendas ou thumbnails) e sincronização com o Notion para o gerenciamento inteligente do fluxo de trabalho.

## ⚙️ Funcionalidades Principais
- 🎬 **Edição de Vídeo (`video_utils.py`)**: Processamento e corte automatizado de arquivos de mídia.
- 🖼️ **Processamento de Imagem (`image_utils.py`)**: Geração ou manipulação de elementos visuais, textos e overlays, utilizando fontes personalizadas.
- 📝 **Integração com Notion (`notion_utils.py`)**: Leitura e atualização de tarefas, pautas, ou status de vídeos diretamente em bancos de dados do Notion.

## 📂 Estrutura do Projeto
```text
robo-de-cortes/
├── assets/
│   ├── fonts/           # Fontes utilizadas para textos e legendas (ex: Poppins)
│   └── images/          # Imagens base, assets visuais e overlays
├── src/
│   ├── config.py        # Configurações gerais, parâmetros e credenciais
│   ├── image_utils.py   # Módulo responsável pela manipulação de imagens
│   ├── notion_utils.py  # Módulo de conexão e interação com a API do Notion
│   └── video_utils.py   # Módulo encarregado do processamento e corte de vídeos
├── main.py              # Ponto de entrada e orquestrador da aplicação
├── requirements.txt     # Dependências e bibliotecas Python do projeto
└── README.md            # Documentação do projeto
```

## 🚀 Como Executar

1. **Instale as dependências:**
   Certifique-se de ter o Python instalado. Execute o comando abaixo na raiz do projeto:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure o ambiente:**
   Ajuste as chaves de API (como o token de integração do Notion) e os caminhos de pastas necessários no arquivo `src/config.py` ou através de variáveis de ambiente.

3. **Inicie o bot:**
   ```bash
   python main.py
   ```

---
*Desenvolvido com 🧠 IA (Vibecoding)*
