# Sobre

Este site foi criado com o intuito de documentar a evolução do projeto agroflorestal em Umburanas, compartilhar informações, e fornecer um meio de contato de forma simples e sem custo.
Acreditando que esta ferramenta pode ser de interesse para outras pessoas, decidimos documentar os principais processos que usamos para reduzir o trabalho.

- GitHub: o site é hospedado no GitHub, permitindo o armazenamento sem custo e a possibilidade de gerenciamento de versões, para garantir que nada é perdido. 
- Markdown: escrevemos o site em formato simples, e que não requer o usuário a ter um conhecimento técnico avançado para editar ou criar novas páginas. 
- Geração de thumbnails: para facilitar a visualização de imagens, criamos um script que gera automaticamente thumbnails para as imagens que são inseridas nas páginas.

````bash
#!/bin/bash

# Este script automatiza a criacao de thumbnails atraves dos seguintes passos
# 1. Procura todas as fotos, ignorando as que ja tem thumbnails
# 2. Cria o diretorio thumbnails, se ainda nao existe no mesmo diretorio que a foto
# 3. Cria uma copia temporaria no formato 16:9 no diretorio de thumbnails
# 4. Reduz a foto para 400x400
# 5. Apaga o arquivo temporario

for format in jpg png; do
  for picture in $(find . -name *.$format); do
    # ignore as fotos que ja sao thumbnails
     if [[ "$picture" == *"thumbnails"* ]]; then
       continue
     fi
    # salva o nome do diretorio em que a foto encontrada esta
    dir_name=$(dirname $picture)
    pic_name=$(basename $picture)
    mkdir -p $dir_name/thumbnails
    target_pic=$dir_name/thumbnails/${pic_name}
    # corta o thumbnail para um tamanho padrao, com proporcao 4:3
    convert $picture -gravity center -crop 16:9 +repage ${target_pic}.tmp
    # redimensiona para ter um tamanho menor do que a original
    convert ${target_pic}.tmp -resize 300x300 "$target_pic"
    rm -f ${target_pic}.tmp
  done
done````
