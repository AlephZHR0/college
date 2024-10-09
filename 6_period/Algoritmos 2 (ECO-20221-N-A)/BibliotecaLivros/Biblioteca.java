import java.io.FileReader;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.List;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import java.lang.reflect.Type;
import java.text.Normalizer;

/**
 * Gerencia a biblioteca de livros utilizando uma lista duplamente encadeada.
 */
public class Biblioteca {
    private DoublyLinkedList<Livro> livros;
    private static final String FILE_NAME = "Livrospequeno.json";
    private Gson gson;

    /**
     * Construtor da classe Biblioteca.
     */
    public Biblioteca() {
        livros = new DoublyLinkedList<>();
        gson = new Gson();
        carregarDados();
    }

    /**
     * Adiciona um livro à biblioteca.
     *
     * @param livro Livro a ser adicionado.
     */
    public void adicionarLivro(Livro livro) {
        livros.insertAtBack(livro);
        salvarDados();
    }

    /**
     * Remove um livro da biblioteca pelo UUID.
     *
     * @param uuid UUID do livro a ser removido.
     * @return true se o livro foi removido, false caso contrário.
     */
    public boolean removerLivro(String uuid) {
        boolean removed = livros.remove(l -> l.getUuid().equals(uuid));
        if (removed) {
            salvarDados();
        }
        return removed;
    }

    /**
     * Lista todos os livros da biblioteca.
     */
    public void listarLivros() {
        livros.display();
    }

    /**
     * Salva os dados dos livros no arquivo JSON.
     */
    public void salvarDados() {
        List<Livro> listaLivros = livros.toList();
        try (FileWriter writer = new FileWriter(FILE_NAME)) {
            gson.toJson(listaLivros, writer);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    /**
     * Carrega os dados dos livros do arquivo JSON.
     */
    public void carregarDados() {
        try (FileReader reader = new FileReader(FILE_NAME)) {
            Type listType = new TypeToken<List<Livro>>() {}.getType();
            List<Livro> listaLivros = gson.fromJson(reader, listType);
            if (listaLivros != null) {
                for (Livro livro : listaLivros) {
                    livros.insertAtBack(livro);
                }
            }
        } catch (Exception e) {
            // Arquivo não existe ou está vazio
        }
    }

    /**
     * Busca livros usando busca linear.
     *
     * @param criterio Critério de busca ("titulo", "autor", "editora").
     * @param valor    Valor a ser buscado.
     * @return Lista de livros encontrados.
     */
    public List<Livro> buscaLinear(String criterio, String valor) {
        List<Livro> resultados = new ArrayList<>();
        Node<Livro> current = livros.getHead();

        // Normaliza o valor buscado
        String valorNormalizado = normalizeString(valor);

        while (current != null) {
            Livro livro = current.getData();
            String campoComparacao = "";

            if (criterio.equalsIgnoreCase("titulo")) {
                campoComparacao = normalizeString(livro.getTitle());
            } else if (criterio.equalsIgnoreCase("autor")) {
                campoComparacao = normalizeString(livro.getAuthor());
            } else if (criterio.equalsIgnoreCase("editora")) {
                campoComparacao = normalizeString(livro.getPublisher());
            }

            if (campoComparacao.equals(valorNormalizado)) {
                resultados.add(livro);
            }

            current = current.getNext();
        }

        return resultados;
    }

    /**
     * Ordena a lista de livros usando Quick Sort.
     *
     * @param criterio Critério de ordenação ("titulo", "autor", "editora").
     */
    public void quickSort(String criterio) {
        List<Livro> listaLivros = livros.toList();
        quickSortHelper(listaLivros, 0, listaLivros.size() - 1, criterio);
        livros = new DoublyLinkedList<>();
        for (Livro livro : listaLivros) {
            livros.insertAtBack(livro);
        }
        salvarDados();
    }

    private void quickSortHelper(List<Livro> lista, int low, int high, String criterio) {
        if (low < high) {
            int pi = partition(lista, low, high, criterio);
            quickSortHelper(lista, low, pi - 1, criterio);
            quickSortHelper(lista, pi + 1, high, criterio);
        }
    }

    private int partition(List<Livro> lista, int low, int high, String criterio) {
        Livro pivot = lista.get(high);
        int i = low - 1;

        for (int j = low; j < high; j++) {
            if (compareLivros(lista.get(j), pivot, criterio) <= 0) {
                i++;
                Livro temp = lista.get(i);
                lista.set(i, lista.get(j));
                lista.set(j, temp);
            }
        }

        Livro temp = lista.get(i + 1);
        lista.set(i + 1, lista.get(high));
        lista.set(high, temp);

        return i + 1;
    }

    private int compareLivros(Livro l1, Livro l2, String criterio) {
        String campoL1 = "";
        String campoL2 = "";

        if (criterio.equalsIgnoreCase("titulo")) {
            campoL1 = normalizeString(l1.getTitle());
            campoL2 = normalizeString(l2.getTitle());
        } else if (criterio.equalsIgnoreCase("autor")) {
            campoL1 = normalizeString(l1.getAuthor());
            campoL2 = normalizeString(l2.getAuthor());
        } else if (criterio.equalsIgnoreCase("editora")) {
            campoL1 = normalizeString(l1.getPublisher());
            campoL2 = normalizeString(l2.getPublisher());
        }

        return campoL1.compareTo(campoL2);
    }

    /**
     * Busca um livro usando busca binária.
     *
     * @param criterio Critério de busca ("titulo").
     * @param valor    Valor a ser buscado.
     * @return Livro encontrado ou null.
     */
    public Livro buscaBinaria(String criterio, String valor) {
        List<Livro> listaLivros = livros.toList();
        // Ordena a lista antes de realizar a busca binária
        listaLivros.sort((l1, l2) -> compareLivros(l1, l2, criterio));
        return buscaBinariaHelper(listaLivros, 0, listaLivros.size() - 1, criterio, valor);
    }

    private Livro buscaBinariaHelper(List<Livro> lista, int low, int high, String criterio, String valor) {
        if (low <= high) {
            int mid = (low + high) / 2;
            Livro midLivro = lista.get(mid);

            // Normaliza o valor buscado e o campo de comparação
            String valorNormalizado = normalizeString(valor);
            String campoComparacao = "";

            if (criterio.equalsIgnoreCase("titulo")) {
                campoComparacao = normalizeString(midLivro.getTitle());
            } else if (criterio.equalsIgnoreCase("autor")) {
                campoComparacao = normalizeString(midLivro.getAuthor());
            } else if (criterio.equalsIgnoreCase("editora")) {
                campoComparacao = normalizeString(midLivro.getPublisher());
            } else {
                // Outros critérios podem ser adicionados aqui
                return null;
            }

            int cmp = campoComparacao.compareTo(valorNormalizado);

            if (cmp == 0) {
                return midLivro;
            } else if (cmp > 0) {
                return buscaBinariaHelper(lista, low, mid - 1, criterio, valor);
            } else {
                return buscaBinariaHelper(lista, mid + 1, high, criterio, valor);
            }
        }
        return null;
    }

    /**
     * Busca um livro pelo UUID.
     *
     * @param uuid UUID do livro.
     * @return Livro encontrado ou null.
     */
    public Livro buscarLivroPorUuid(String uuid) {
        Node<Livro> current = livros.getHead();
        while (current != null) {
            Livro livro = current.getData();
            if (livro.getUuid().equals(uuid)) {
                return livro;
            }
            current = current.getNext();
        }
        return null;
    }

    // Método auxiliar para normalizar strings
    public static String normalizeString(String str) {
        if (str == null) {
            return "";
        }
        String normalized = Normalizer.normalize(str, Normalizer.Form.NFD);
        normalized = normalized.replaceAll("\\p{M}", "");
        return normalized.toLowerCase().trim();
    }
}
