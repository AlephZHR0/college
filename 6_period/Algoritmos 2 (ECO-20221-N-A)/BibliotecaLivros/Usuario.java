import java.util.List;

/**
 * Representa um usuário do sistema.
 */
public class Usuario {
    private String username;
    private String senha;
    private GrupoDeLivros grupoDeLivros;

    /**
     * Construtor da classe Usuario.
     *
     * @param username Nome de usuário.
     * @param senha    Senha do usuário.
     */
    public Usuario(String username, String senha) {
        this.username = username;
        this.senha = senha;
        this.grupoDeLivros = new GrupoDeLivros(username);
    }

    /**
     * Autentica o usuário.
     *
     * @param senha Senha fornecida.
     * @return true se a senha estiver correta, false caso contrário.
     */
    public boolean autenticar(String senha) {
        return this.senha.equals(senha);
    }

    /**
     * Adiciona um livro aos favoritos.
     *
     * @param livro Livro a ser adicionado.
     */
    public void adicionarFavorito(Livro livro) {
        grupoDeLivros.adicionarLivro("FAVORITOS", livro);
    }

    /**
     * Remove um livro dos favoritos.
     *
     * @param uuid UUID do livro a ser removido.
     * @return true se o livro foi removido, false caso contrário.
     */
    public boolean removerFavorito(String uuid) {
        return grupoDeLivros.removerLivro("FAVORITOS", uuid);
    }

    /**
     * Exibe os livros favoritos.
     */
    public void exibirFavoritos() {
        grupoDeLivros.exibirLivros("FAVORITOS");
    }

    /**
     * Retorna a lista de livros favoritos.
     *
     * @return Lista de livros favoritos.
     */
    public List<Livro> getFavoritos() {
        return grupoDeLivros.getLivros("FAVORITOS");
    }

    // Getters e setters

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public GrupoDeLivros getGrupoDeLivros() {
        return grupoDeLivros;
    }

    public void setGrupoDeLivros(GrupoDeLivros grupoDeLivros) {
        this.grupoDeLivros = grupoDeLivros;
    }
}
