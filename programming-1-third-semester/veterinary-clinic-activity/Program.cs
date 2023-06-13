using System;

class Program
{
    static void ExibirCabecalho(string texto)
    {
        Console.WriteLine("====================================");
        Console.WriteLine(texto);
        Console.WriteLine("====================================");
    }

    static void CadastrarMedicos()
    {
        ExibirCabecalho("Cadastro de Médicos");
    }

    static void CadastrarAnimais()
    {
        ExibirCabecalho("Cadastro de Animais");
    }

    static void CadastrarAtendimentos()
    {
        ExibirCabecalho("Cadastro de Atendimentos");
    }

    static void ExibirRelatorioAnimais()
    {
        ExibirCabecalho("Relatório de Animais");
    }

    static void ExibirRelatorioAtendimentos()
    {
        ExibirCabecalho("Relatório de Atendimentos");
    }

    static void ExibirMenu()
    {
        while (true)
        {
            ExibirCabecalho("MENU PRINCIPAL");
            Console.WriteLine("1 - Cadastros");
            Console.WriteLine("    1.1 - Médicos");
            Console.WriteLine("    1.2 - Animais");
            Console.WriteLine("    1.3 - Atendimentos");
            Console.WriteLine("    1.4 - SAIR");
            Console.WriteLine("2 - Relatórios");
            Console.WriteLine("     2.1 - Animais");
            Console.WriteLine("     2.2 - Atendimentos");
            Console.WriteLine("     2.3 - SAIR");
            Console.WriteLine("0 - SAIR");

            Console.Write("Digite a opção desejada: ");
            string opcao = Console.ReadLine();

            if (opcao == "1")
            {
                while (true)
                {
                    ExibirCabecalho("MENU CADASTROS");
                    Console.WriteLine("1.1 - Médicos");
                    Console.WriteLine("1.2 - Animais");
                    Console.WriteLine("1.3 - Atendimentos");
                    Console.WriteLine("1.4 - SAIR");

                    Console.Write("Digite a opção desejada (1.1, 1.2, 1.3 ou 1.4): ");
                    string opcaoCadastros = Console.ReadLine();

                    if (opcaoCadastros == "1.1")
                    {
                        CadastrarMedicos();
                    }
                    else if (opcaoCadastros == "1.2")
                    {
                        CadastrarAnimais();
                    }
                    else if (opcaoCadastros == "1.3")
                    {
                        CadastrarAtendimentos();
                    }
                    else if (opcaoCadastros == "1.4")
                    {
                        break;
                    }
                    else
                    {
                        Console.WriteLine("Opção inválida. Digite novamente.");
                    }
                }
            }
            else if (opcao == "2")
            {
                while (true)
                {
                    ExibirCabecalho("MENU RELATÓRIOS");
                    Console.WriteLine("2.1 - Animais");
                    Console.WriteLine("2.2 - Atendimentos");
                    Console.WriteLine("2.3 - SAIR");

                    Console.Write("Digite a opção desejada (2.1, 2.2 ou 2.3): ");
                    string opcaoRelatorios = Console.ReadLine();

                    if (opcaoRelatorios == "2.1")
                    {
                        ExibirRelatorioAnimais();
                    }
                    else if (opcaoRelatorios == "2.2")
                    {
                        ExibirRelatorioAtendimentos();
                    }
                    else if (opcaoRelatorios == "2.3")
                    {
                        break;
                    }
                    else
                    {
                        Console.WriteLine("Opção inválida. Digite novamente.");
                    }
                }
            }
            else if (opcao == "0")
            {
                break;
            }
            else
            {
                Console.WriteLine("Opção inválida. Digite novamente.");
            }
        }
    }

    static void Main()
    {
        ExibirMenu();
    }
}
