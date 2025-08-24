# Automação

Os dados coletados neste projetos são classificados de forma estruturada:

```
<zona funcional> <zona física> <subzona*> <dispositivo> <metrica>
```

- Zona funcional: Classifica o tipo de dado. Em um primeiro momento, definimos as seguintes classes: 
  - infra: considera as condições de tudo que for construído e suas partes
    - Estruturas (galpão, cisterna, casa, postes)
    - Equipamentos (bombas, iluminação, painéis, portões)
    - Eletricidade e hidráulica
  - ambiencia: Representa o ambiente natural
    - Chuva, vento, radiação solar, umidade, temperatura
  - seguranca: interações de humanos e animais com a área
    - Câmeras, Porteiras e cercas, Presença, Rastreamento de movimento
  - producao: dados diretamente relacionados à atividade agrícola ou pecuária em si
    - contagem de ovos, tomates, produção de leite, etc.
  - logistica: controle de fluxo, armazenamento e distribuição
    - armazenamento de sementes, estoque de agua, etc
- Zona física: saf_2, casa_1, potreiro_3, nucleo_7
- Subzonas\*: sala, cozinha, porteira_leste
  - subzonas é recursivo, uma subzona pode ter subzonas: por exemplo, uma casa (zona) pode ter uma cozinha (subzona) que pode ter armarios (sub-subzona); um saf pode ter uma linha que é subdividida em canteiros ou croquis.
- Dispositivo: sensor_umidade, lampada_teto, bomba_1
- Métrica: temperatura, pressao, velocidade, umidade, movimento, stream, etc.
