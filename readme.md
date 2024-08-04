
# Memorial Descritivo da Implementação e Funcionamento do Simulador

## Introdução

O simulador de gerenciador de processos foi implementado para suportar quatro políticas de escalonamento: FCFS, SJF Não-preemptivo, SJF Preemptivo e Round Robin. O objetivo do simulador é permitir a entrada de processos, definir a política de escalonamento, e calcular a ordem de execução dos processos, o tempo de execução e o tempo médio de espera, conforme exigido.



## Estrutura do Código

### `main.py`

-   **Função `create_process(algorithm)`**: Esta função coleta as entradas dos processos, incluindo PIDs, tempos de rajada e tempos de chegada (quando aplicável). Retorna uma lista de dicionários contendo as informações dos processos.
-   **Função `switch_case_option(op)`**: Mapeia a entrada do usuário para a política de escalonamento correspondente.
-   **Função `main()`**: Coleta a escolha do usuário para a política de escalonamento, cria os processos e invoca a função apropriada para a política escolhida. Para Round Robin, também coleta o quantum.

### `fcfs.py`

-   **Função `fcfs(processes, context_switch_time)`**: Implementa o algoritmo FCFS. Calcula a ordem de execução dos processos, tempos de execução e o tempo médio de espera. Utiliza as funções de visualização `print_table_fcfs` e `print_execution_order` para exibir os resultados.

### `sjf_non_preemptive.py`

-   **Função `sjf_non_preemptive(processes, context_switch_time)`**: Implementa o algoritmo SJF Não-preemptivo. Ordena os processos pelo tempo de chegada e pelo menor tempo de rajada. Calcula a ordem de execução, tempos de execução e o tempo médio de espera. Utiliza as funções de visualização `print_table_sjf` e `print_execution_order` para exibir os resultados.

### `sjf_preemptive.py`

-   **Função `sjf_preemptive(processes, context_switch_time)`**: Implementa o algoritmo SJF Preemptivo. Utiliza uma heap para gerenciar os processos com o menor tempo de rajada restante. Calcula a ordem de execução e tempos de execução. Utiliza as funções de visualização `print_table_sjf` e `print_execution_order` para exibir os resultados.

### `round_robin.py`

-   **Função `round_robin(processes, quantum, context_switch_time)`**: Implementa o algoritmo Round Robin. Mantém a fila de processos e executa cada processo pelo tempo do quantum. Calcula a ordem de execução e tempos de execução. Utiliza as funções de visualização `print_table_round_robin` e `print_execution_order` para exibir os resultados.

### `visualizer.py`

-   **Funções `print_table_fcfs`, `print_table_sjf` e `print_table_round_robin`**: Estas funções são responsáveis por formatar e imprimir os resultados das execuções dos processos, incluindo PIDs, tempos de chegada, tempos de rajada, tempos de espera, tempos de resposta e tempo de término, além do tempo de espera médio e tempo de execução total, conforme a política de escalonamento aplicada.
-   **Função `print_execution_order`**: Formata e imprime a ordem de execução dos processos, utilizando cores para realçar diferentes partes da tabela.



## Funcionamento

O usuário interage com o programa através do terminal, fornecendo as informações dos processos e a política de escalonamento desejada. O programa então processa essas informações e exibe os resultados de acordo com a política selecionada.



## Importações Utilizadas

O código utiliza as seguintes importações para garantir a funcionalidade e a apresentação dos dados do simulador:

-   **`import sys`**: Utilizado para leitura de entradas e argumentos da linha de comando, facilitando a interação com o usuário.
-   **`import numpy as np`**: Utilizado para operações matemáticas avançadas e manipulação eficiente de arrays.
-   **`import heapq`**: Utilizado para implementar uma heap, facilitando a seleção de processos com o menor tempo de execução restante.
-   **`from termcolor import colored`**: Utilizado para adicionar cores ao texto impresso no terminal, melhorando a legibilidade e a apresentação dos dados.
-   **`from utils.visualizer`**: Importa funções do módulo **`visualizer.py`** para formatação e exibição dos resultados dos diferentes algoritmos de escalonamento.



## Estrutura do Código

O código está disponível no [GitHub](https://github.com/JP-Out/scheduler-SO).

[https://github.com/JP-Out/scheduler-SO](https://github.com/JP-Out/scheduler-SO)

A estrutura do projeto é a seguinte:

```markdown
scheduler-SO/
├── utils/
│   └── visualizer.py
├── includes/
│   ├── fcfs.py
│   ├── sjf_non_preemptive.py
│   ├── sjf_preemptive.py
│   └── round_robin.py
└── main.py

```