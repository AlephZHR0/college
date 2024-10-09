/**
 * Representa um livro na biblioteca.
 */
public class Livro implements Comparable<Livro> {
    private String title;
    private String author;
    private String description;
    private String kind;
    private int edition;
    private String coverImageUrl;
    private String publisher;
    private String publishDate;
    private String uuid;

    /**
     * Construtor vazio necessário para a desserialização JSON.
     */
    public Livro() {
    }

    /**
     * Construtor da classe Livro.
     *
     * @param title         Título do livro.
     * @param author        Autor do livro.
     * @param description   Descrição do livro.
     * @param kind          Tipo do livro.
     * @param edition       Edição do livro.
     * @param coverImageUrl URL da imagem de capa.
     * @param publisher     Editora do livro.
     * @param publishDate   Data de publicação.
     * @param uuid          Identificador único do livro.
     */
    public Livro(String title, String author, String description, String kind, int edition, String coverImageUrl,
            String publisher, String publishDate, String uuid) {
        this.title = title;
        this.author = author;
        this.description = description;
        this.kind = kind;
        this.edition = edition;
        this.coverImageUrl = coverImageUrl;
        this.publisher = publisher;
        this.publishDate = publishDate;
        this.uuid = uuid;
    }

    // Getters e setters para todos os atributos

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    // Repita os getters e setters para os demais atributos...

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    
    public String getDescription() {
        return description;
    }
    
    public void setDescription(String description) {
        this.description = description;
    }

    public String getKind() {
        return kind;
    }
    
    public void setKind(String kind) {
        this.kind = kind;
    }
    
    public int getEdition() {
        return edition;
    }
    
    public void setEdition(int edition) {
        this.edition = edition;
    }
    
    public String getCoverImageUrl() {
        return coverImageUrl;
    }
    
    public void setCoverImageUrl(String coverImageUrl) {
        this.coverImageUrl = coverImageUrl;
    }
    
    public String getPublisher() {
        return publisher;
    }
    
    public void setPublisher(String publisher) {
        this.publisher = publisher;
    }
    
    public String getPublishDate() {
        return publishDate;
    }
    
    public void setPublishDate(String publishDate) {
        this.publishDate = publishDate;
    }
    
    public String getUuid() {
        return uuid;
    }
    
    public void setUuid(String uuid) {
        this.uuid = uuid;
    }

    @Override
    public String toString() {
        return "Título: " + title + "\n" + 
               "Autor: " + author + "\n" + 
               "Descrição: " + description + "\n" +
               "Tipo: " + kind + "\n" + 
               "Edição: " + edition + "\n" + 
               "URL da Capa: " + coverImageUrl + "\n" +
               "Editora: " + publisher + "\n" + 
               "Data de Publicação: " + publishDate + "\n" + 
               "UUID: " + uuid + "\n";
    }

    /**
     * Implementação do método compareTo para comparação entre livros.
     *
     * @param other Livro a ser comparado.
     * @return Resultado da comparação.
     */
    @Override
    public int compareTo(Livro other) {
        return this.title.compareToIgnoreCase(other.title);
    }
}
