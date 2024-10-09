import java.io.FileReader;
import java.io.FileWriter;
import java.lang.reflect.Type;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

/**
 * Classe principal que executa o programa.
 */
public class Main {
    private static Map<String, Usuario> usuarios = new HashMap<>();
    private static Usuario usuarioAtual = null;
    private static final String USUARIOS_FILE = "usuarios.json";
    private static Gson gson = new Gson();

    /**
     * Método principal que inicia a execução do programa.
     *
     * @param args Argumentos de linha de comando.
     */
    public static void main(String[] args) {
        Biblioteca biblioteca = new Biblioteca();
        carregarUsuarios();
        Scanner scanner = new Scanner(System.in);
        boolean executando = true;

        while (executando) {
            if (usuarioAtual == null) {
                System.out.println("===== Biblioteca de Livros =====");
                System.out.println("1. Registrar Usuário");
                System.out.println("2. Login");
                System.out.println("3. Listar Livros");
                System.out.println("4. Sair");
                System.out.print("Escolha uma opção: ");
                int opcao = Integer.parseInt(scanner.nextLine());
                System.out.println("");
                switch (opcao) {
                    case 1:
                        registrarUsuario(scanner);
                        break;
                    case 2:
                        login(scanner);
                        break;
                    case 3:
                        biblioteca.listarLivros();
                        break;
                    case 4:
                        System.out.println("Saindo do programa...");
                        salvarUsuarios();
                        executando = false;
                        break;
                    default:
                        System.out.println("Opção inválida. Tente novamente.");
                }
            } else {
                System.out.println("===== Bem-vindo, " + usuarioAtual.getUsername() + " =====");
                System.out.println("1. Listar Livros");
                System.out.println("2. Adicionar Livro");
                System.out.println("3. Remover Livro");
                System.out.println("4. Buscar Livro (Linear)");
                System.out.println("5. Buscar Livro (Binária)");
                System.out.println("6. Ordenar Livros (Quick Sort)");
                System.out.println("7. Adicionar Livro aos Favoritos");
                System.out.println("8. Remover Livro dos Favoritos");
                System.out.println("9. Listar Livros Favoritos");
                System.out.println("10. Logout");
                System.out.print("Escolha uma opção: ");
                int opcao = Integer.parseInt(scanner.nextLine());
                System.out.println("");
                switch (opcao) {
                    case 1:
                        biblioteca.listarLivros();
                        break;
                    case 2:
                        Livro novoLivro = criarLivro(scanner);
                        biblioteca.adicionarLivro(novoLivro);
                        System.out.println("Livro adicionado com sucesso!");
                        break;
                    case 3:
                        System.out.print("Digite o UUID do livro a ser removido: ");
                        String uuidRemover = scanner.nextLine();
                        boolean removidoLivro = biblioteca.removerLivro(uuidRemover);
                        if (removidoLivro) {
                            System.out.println("Livro removido com sucesso!");
                        } else {
                            System.out.println("Livro não encontrado.");
                        }
                        break;
                    case 4:
                        System.out.print("Digite o critério de busca (titulo, autor, editora): ");
                        String criterioBusca = scanner.nextLine();
                        System.out.print("Digite o valor a ser buscado: ");
                        String valorBusca = scanner.nextLine();
                        List<Livro> resultados = biblioteca.buscaLinear(criterioBusca, valorBusca);
                        if (resultados.isEmpty()) {
                            System.out.println("Nenhum livro encontrado.");
                        } else {
                            for (Livro livro : resultados) {
                                System.out.println(livro.toString());
                            }
                        }
                        break;
                    case 5:
                        System.out.print("Digite o critério de busca (titulo, autor, editora): ");
                        String criterioBinario = scanner.nextLine();
                        System.out.print("Digite o valor a ser buscado: ");
                        String valorBinario = scanner.nextLine();
                        Livro livroEncontrado = biblioteca.buscaBinaria(criterioBinario, valorBinario);
                        if (livroEncontrado != null) {
                            System.out.println("Livro encontrado:");
                            System.out.println(livroEncontrado.toString());
                        } else {
                            System.out.println("Livro não encontrado.");
                        }
                        break;
                    case 6:
                        System.out.print("Digite o critério de ordenação (titulo, autor, editora): ");
                        String criterioOrdenacao = scanner.nextLine();
                        biblioteca.quickSort(criterioOrdenacao);
                        System.out.println("Livros ordenados com sucesso!");
                        break;
                    case 7:
                        System.out.print("Digite o UUID do livro a ser adicionado aos favoritos: ");
                        String uuidAdd = scanner.nextLine();
                        Livro livroAdd = biblioteca.buscarLivroPorUuid(uuidAdd);
                        if (livroAdd != null) {
                            usuarioAtual.adicionarFavorito(livroAdd);
                            System.out.println("Livro adicionado aos favoritos com sucesso!");
                            salvarUsuarios();
                        } else {
                            System.out.println("Livro não encontrado.");
                        }
                        break;
                    case 8:
                        System.out.print("Digite o UUID do livro a ser removido dos favoritos: ");
                        String uuidRemove = scanner.nextLine();
                        boolean removido = usuarioAtual.removerFavorito(uuidRemove);
                        if (removido) {
                            System.out.println("Livro removido dos favoritos com sucesso!");
                            salvarUsuarios();
                        } else {
                            System.out.println("Livro não encontrado nos favoritos.");
                        }
                        break;
                    case 9:
                        usuarioAtual.exibirFavoritos();
                        break;
                    case 10:
                        usuarioAtual = null;
                        System.out.println("Logout realizado com sucesso.");
                        break;
                    default:
                        System.out.println("Opção inválida. Tente novamente.");
                }
            }
        }

        scanner.close();
    }

    /**
     * Registra um novo usuário.
     *
     * @param scanner Scanner para leitura de entradas.
     */
    private static void registrarUsuario(Scanner scanner) {
        System.out.print("Nome de usuário: ");
        String username = scanner.nextLine();
        if (usuarios.containsKey(username)) {
            System.out.println("Usuário já existe.\n");
            return;
        }
        System.out.print("Senha: ");
        String senha = scanner.nextLine();
        Usuario novoUsuario = new Usuario(username, senha);
        usuarios.put(username, novoUsuario);
        salvarUsuarios();
        System.out.println("Usuário registrado com sucesso!\n");
    }

    /**
     * Realiza o login de um usuário existente.
     *
     * @param scanner Scanner para leitura de entradas.
     */
    private static void login(Scanner scanner) {
        System.out.print("Nome de usuário: ");
        String username = scanner.nextLine();
        System.out.print("Senha: ");
        String senha = scanner.nextLine();
        Usuario usuario = usuarios.get(username);
        if (usuario != null && usuario.autenticar(senha)) {
            usuarioAtual = usuario;
            System.out.println("Login realizado com sucesso!\n");
        } else {
            System.out.println("Usuário ou senha inválidos.\n");
        }
    }

    /**
     * Salva os usuários em um arquivo JSON.
     */
    private static void salvarUsuarios() {
        try (FileWriter writer = new FileWriter(USUARIOS_FILE)) {
            gson.toJson(usuarios, writer);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    /**
     * Carrega os usuários de um arquivo JSON.
     */
    private static void carregarUsuarios() {
        try (FileReader reader = new FileReader(USUARIOS_FILE)) {
            Type type = new TypeToken<Map<String, Usuario>>() {}.getType();
            usuarios = gson.fromJson(reader, type);
            if (usuarios == null) {
                usuarios = new HashMap<>();
            }
        } catch (Exception e) {
            usuarios = new HashMap<>();
        }
    }

    /**
     * Cria um novo livro com base nas entradas do usuário.
     *
     * @param scanner Scanner para leitura de entradas.
     * @return Novo objeto Livro.
     */
    private static Livro criarLivro(Scanner scanner) {
        System.out.print("Título: ");
        String title = scanner.nextLine();

        System.out.print("Autor: ");
        String author = scanner.nextLine();

        System.out.print("Descrição: ");
        String description = scanner.nextLine();

        System.out.print("Tipo: ");
        String kind = scanner.nextLine();

        System.out.print("Edição: ");
        int edition = Integer.parseInt(scanner.nextLine());

        System.out.print("URL da Capa: ");
        String coverImageUrl = scanner.nextLine();

        System.out.print("Editora: ");
        String publisher = scanner.nextLine();

        System.out.print("Data de Publicação: ");
        String publishDate = scanner.nextLine();

        String uuid = java.util.UUID.randomUUID().toString();

        return new Livro(title, author, description, kind, edition, coverImageUrl, publisher, publishDate, uuid);
    }
}
