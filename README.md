# controlecurso_ad1-fadam
Esse aplicativo foi desenvolvido para servir de avaliação 1 na disciplina de programação de computadores

## Cenário e Menu de Ações
Faça um programa que realiza o gerenciamento dos alunos da disciplina de Programação de computadores. O programa deve possui o menu abaixo:

- Cadastrar Aluno
- Buscar Aluno
- Editar Dados do Aluno
- Excluir Aluno
- Lançar Notas
  - Avaliação Diagnóstica 1 (AD1)
  - Avaliação Diagnóstica 2 (AD2)
  - Nota Recuperação
- Relatórios
  - Gerar Lista de Frequencia
  - Gerar Relatório de Notas
  - Gerar Relatário Final da Disciplina

## Regras de negócio

- Para a cadastro dos alunos o programa deve inserir: nº de matrícula, nome, teelefone, endereço;
- A busca do aluno, pode ser efetuada por matrícula e devem ser exibidos os dados do aluno buscado, inclusive notas AD1, AD2, Média ((AD1 + AD2) / 2), mais nota de recuperação caso ele tenha realizado esta prova;
- As funcionalidades de edição e esclusão são autoexplicativas e realizam essas funções a que se propõe;
- Só deve ser possível lançar nota de recuperação caso o aluno já tenha nota AD1 e AD2 e tiver média inferior a 7.0;
- A lista de frequência deve apresentar número de matrícula, nome completo e linha para assinatura;
- O relatório de notas deve apresentar número de matrícula, nome e notas dos alunos, inclusive média final e nota de recuoeração caso tenha realizado esta prova;
- O relatório final da disciplina deve apresentar:
  - A proporção de alunos (%) aprovados;
  - A proporção de alunos (%) reprovados;
  - A matrícula do aluno que teve a maior média final;
  - Média geral da turma na disciplina.

## Informações

O trabalho pode ser feito em duplas, devendo ser entregue até dia 16/11/2021
