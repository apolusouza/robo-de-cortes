
Readme · MD
# 🎬 Sistema de Corte Automático de Vídeo
 
Script em Python que automatiza o processo de **padronização e composição de vídeos verticais**, combinando redimensionamento inteligente, corte centralizado, sobreposição de imagem e geração automática de legendas — pensado para produção de conteúdo em formato de vídeo curto (Reels, Shorts, TikTok).
 
## Funcionalidades
 
- **Normalização automática de dimensões**: ajusta qualquer vídeo de entrada para a resolução alvo (1080x900), decidindo dinamicamente entre redimensionar por largura ou por altura conforme a proporção original.
- **Corte centralizado (center crop)**: quando o redimensionamento ultrapassa as dimensões alvo, o vídeo é cortado a partir do centro, evitando distorções.
- **Geração de legenda em imagem**: cria uma legenda a partir de um texto, quebrando as linhas automaticamente (`textwrap`) e renderizando como imagem PNG com fonte customizada via PIL.
- **Composição em camadas**: monta o vídeo final combinando uma imagem de capa, a legenda gerada e o vídeo normalizado em posições específicas na tela.
- **Exportação**: gera o vídeo final (`novo_video.mp4`) pronto para uso.
## 🛠️ Tecnologias
 
- [Python 3](https://www.python.org/)
- [MoviePy](https://zulko.github.io/moviepy/) — edição e composição de vídeo
- [Pillow (PIL)](https://python-pillow.org/) — geração da imagem de legenda
- [ImageMagick](https://imagemagick.org/) — renderização de texto (usado pelo MoviePy)
- Desenvolvido e testado em **Google Colab**
## 📋 Pré-requisitos
 
```bash
pip install moviepy pillow
```
 
Arquivos necessários no diretório de execução:
- `video.mp4` — vídeo de entrada a ser processado
- `imagem.jpg` — imagem de capa/fundo
- `Poppins-Regular.ttf` — fonte usada na legenda (ou substitua por outra de sua preferência)
- 
## ▶️ Como usar
 
1. Coloque o vídeo de entrada como `video.mp4` no mesmo diretório do script.
2. Defina o texto da legenda na variável `texto`.
3. Ajuste `WIDTH` e `HEIGHT` se quiser outra resolução de saída (padrão: 1080x900).
4. Execute o script (célula por célula, se estiver no Colab/Jupyter).
5. O vídeo final será salvo como `novo_video.mp4`.
6. 
## ⚙️ Como funciona (visão geral)
 
1. **Leitura do vídeo**: carrega o `video.mp4` e extrai duração, largura e altura.
2. **Preparação da legenda**: o texto é quebrado em linhas com `textwrap.fill()` e desenhado em uma imagem transparente com `PIL.ImageDraw`.
3. **Normalização geométrica**:
   - Se a largura for diferente do alvo, o vídeo é redimensionado pela largura; se após isso a altura ultrapassar o alvo, aplica-se um corte centralizado na altura.
   - Se a altura for menor que o alvo, redimensiona pela altura e corta a largura se necessário.
   - Se a altura já for maior que o alvo, corta diretamente pela altura.
4. **Composição final**: a imagem de capa, a legenda e o vídeo normalizado são posicionados como camadas (`CompositeVideoClip`) e exportados em um único arquivo.
## 🐛 Problemas conhecidos / melhorias futuras
 
Este script foi extraído de um notebook exploratório do Colab e ainda tem pontos a organizar antes de ser considerado "produção":
 
- [ ] Há imports duplicados e um erro de digitação (`TextClipi` em vez de `TextClip`, `textWrap` em vez de `textwrap`) que precisam ser corrigidos para rodar de forma limpa em um ambiente novo.
- [ ] O texto da legenda e os nomes dos arquivos (`video.mp4`, `imagem.jpg`) estão hardcoded — o ideal é transformar em parâmetros de função ou argumentos de linha de comando.
- [ ] A lógica de posicionamento da legenda (`espace_li = legenda.size[1] + 395`) usa valores fixos que dependem da resolução escolhida; vale documentar ou generalizar essa conta.
- [ ] Falta tratamento de erro (ex: arquivo de vídeo ou fonte não encontrados).
- [ ] Refatoração em funções reutilizáveis (`gerar_legenda()`, `normalizar_video()`, `compor_video()`) para facilitar testes e reuso.
