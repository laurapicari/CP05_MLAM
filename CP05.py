import math
import statistics


MEDIA_MINIMA = 6.0
ALPHA = 0.05

alunos = []


def cadastrar_aluno():
    print("=" * 30, "CADASTRO DE ALUNO", "=" * 30)

    nome = input("Nome do aluno: ")
    turma = input("Turma: ")

    while True:
        try:
            nota1 = float(input("Nota 1 (0 a 10): "))
            if 0 <= nota1 <= 10:
                break
            print("A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Digite uma nota válida.")

    while True:
        try:
            nota2 = float(input("Nota 2 (0 a 10): "))
            if 0 <= nota2 <= 10:
                break
            print("A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Digite uma nota válida.")

    while True:
        try:
            nota3 = float(input("Nota 3 (0 a 10): "))
            if 0 <= nota3 <= 10:
                break
            print("A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Digite uma nota válida.")


    media = (nota1 + nota2 + nota3) / 3


    if media >= MEDIA_MINIMA:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    aluno = {
        "nome": nome,
        "turma": turma,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "media": media,
        "situacao": situacao
    }

    alunos.append(aluno)

    print("\nAluno cadastrado com sucesso!")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")


def listar_alunos():
    print("=" * 30, "ALUNOS CADASTRADOS","=" * 30) 

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    for i, aluno in enumerate(alunos, start=1):
        print(f"\nAluno {i}")
        print(f"Nome: {aluno['nome']}")
        print(f"Turma: {aluno['turma']}")
        print(f"Nota 1: {aluno['nota1']:.2f}")
        print(f"Nota 2: {aluno['nota2']:.2f}")
        print(f"Nota 3: {aluno['nota3']:.2f}")
        print(f"Média: {aluno['media']:.2f}")
        print(f"Situação: {aluno['situacao']}")



def estatisticas_turma():
    print("=" * 30, "ESTATÍSTICAS DA TURMA", "=" * 30)

    if len(alunos) == 0 : return
        print("Cadastre pelo menos 2 alunos.")
        return

    medias = [aluno["media"] for aluno in alunos]

    media_turma = statistics.mean(medias)
    desvio_padrao = statistics.stdev(medias)

    aprovados = sum(
        1 for aluno in alunos
        if aluno["situacao"] == "Aprovado"
    )

    reprovados = len(alunos) - aprovados

    percentual_aprovados = (aprovados / len(alunos)) * 100
    percentual_reprovados = (reprovados / len(alunos)) * 100

    print(f"Quantidade de alunos: {len(alunos)}")
    print(f"Média da turma: {media_turma:.2f}")
    print(f"Desvio padrão: {desvio_padrao:.2f}")
    print(f"Aprovados: {aprovados} ({percentual_aprovados:.1f}%)")
    print(f"Reprovados: {reprovados} ({percentual_reprovados:.1f}%)")


def teste_hipotese():
    print("=" * 30, "TESTE DE HIPÓTESE", "=" * 30)

    if len(alunos) < 2:
        print("Cadastre pelo menos 2 alunos para realizar o teste.")
        return

    medias = [aluno["media"] for aluno in alunos]

    n = len(medias)
    media_amostral = statistics.mean(medias)
    desvio_padrao = statistics.stdev(medias)


    t = (media_amostral - MEDIA_MINIMA) / (
        desvio_padrao / math.sqrt(n)
    )

    print("\nHipóteses:")
    print("H0: μ = 6,0")
    print("H1: μ ≠ 6,0")

    print(f"\nMédia da amostra: {media_amostral:.2f}")
    print(f"Desvio padrão: {desvio_padrao:.2f}")
    print(f"Número de alunos: {n}")
    print(f"Estatística t: {t:.4f}")

    print("\nNível de significância: 5%")

    # Para o teste bilateral com amostras maiores,
    # utilizamos aproximadamente o valor crítico ±1,96.
    valor_critico = 1.96

    if abs(t) > valor_critico:
        print("\nResultado: Rejeitamos H0.")
        print(
            "Há evidências estatísticas de que "
            "a média da turma é diferente de 6,0."
        )
    else:
        print("\nResultado: Não rejeitamos H0.")
        print(
            "Não há evidências estatísticas suficientes "
            "para afirmar que a média da turma é diferente de 6,0."
        )


# ==========================================
# MENU PRINCIPAL
# ==========================================

def menu():
    while True:
        print("\n")
        print("==========================================")
        print("       SISTEMA DE DESEMPENHO ESCOLAR")
        print("==========================================")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Ver estatísticas da turma")
        print("4 - Realizar teste de hipótese")
        print("0 - Sair")
        print("==========================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()

        elif opcao == "2":
            listar_alunos()

        elif opcao == "3":
            estatisticas_turma()

        elif opcao == "4":
            teste_hipotese()

        elif opcao == "0":
            print("\nSistema encerrado.")
            break

        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
