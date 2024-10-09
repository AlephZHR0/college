import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Gerencia as diferentes listas de livros do usuário.
 */
public class GrupoDeLivros {
    private String usuarioId;
    private Map<String, List<Livro>> listas;

    /**
     * Construtor da classe GrupoDeLivros.
     *
     * @param usuarioId ID do usuário.
     */
    public GrupoDeLivros(String usuarioId) {
        this.usuarioId = usuarioId;
        listas = new HashMap<>();
        listas.put("FAVORITOS", new ArrayList<>());
        // Podemos adicionar outras listas como "LISTA_DE_LEITURA", "HISTORICO_DE_LEITURA", etc.
    }

    /**
     * Adiciona um livro a uma lista.
     *
     * @param nomeLista Nome da lista.
     * @param livro     Livro a ser adicionado.
     */
    public void adicionarLivro(String nomeLista, Livro livro) {
        List<Livro> lista = listas.get(nomeLista);
        if (lista != null) {
            lista.add(livro);
        }
    }

    /**
     * Remove um livro de uma lista.
     *
     * @param nomeLista Nome da lista.
     * @param uuid      UUID do livro a ser removido.
     * @return true se o livro foi removido, false caso contrário.
     */
    public boolean removerLivro(String nomeLista, String uuid) {
        List<Livro> lista = listas.get(nomeLista);
        if (lista != null) {
            return lista.removeIf(l -> l.getUuid().equals(uuid));
        }
        return false;
    }

    /**
     * Exibe os livros de uma lista.
     *
     * @param nomeLista Nome da lista.
     */
    public void exibirLivros(String nomeLista) {
        List<Livro> lista = listas.get(nomeLista);
        if (lista != null) {
            if (lista.isEmpty()) {
                System.out.println("A lista está vazia.");
            } else {
                for (Livro livro : lista) {
                    System.out.println(livro.toString());
                }
            }
        }
    }

    /**
     * Retorna a lista de livros de uma lista específica.
     *
     * @param nomeLista Nome da lista.
     * @return Lista de livros.
     */
    public List<Livro> getLivros(String nomeLista) {
        return listas.get(nomeLista);
    }
}
