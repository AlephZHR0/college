### Principais Classes e Componentes

1. **Classe `Livro`**
    - **Atributos:**
        - `String title`
        - `String author`
        - `String description`
        - `int edition`
        - `String coverImageUrl`
        - `String publisher`
        - `String publishDate`
        - `boolean isFavorite`
    - **Métodos:**
        - Getters e Setters para todos os atributos.
        - `toString(): String` – Para representação textual do livro.

2. **Classe `Biblioteca`**
    - **Atributos:**
        - `ListaDuplamenteEncadeada<Livro> livros` – Utilizando a estrutura de dados fornecida (`ListaDuplamenteEncadeada`).
    - **Métodos:**
        - `adicionarLivro(Livro livro): void`
        - `removerLivro(String titulo): boolean`
        - `listarLivros(): List<Livro>`
        - `buscarLivroLinear(String criterio, String valor): List<Livro>`
        - `buscarLivroBinario(String criterio, String valor): Livro`
        - `ordenarLivros(String criterio): void` – Utiliza algoritmos de ordenação como BubbleSort, MergeSort, etc.
        - `salvarDados(): void` – Persistência em arquivos.
        - `carregarDados(): void`

3. **Classe `ListaLeitura`**
    - **Atributos:**
        - `CircularList<Livro> livrosParaLer` – Utilizando uma lista circular personalizada.
        - `String nomeLista`
    - **Métodos:**
        - `adicionarLivro(Livro livro): void`
        - `removerLivro(String titulo): boolean`
        - `navegarProximo(): Livro`
        - `navegarAnterior(): Livro`
        - `marcarProgresso(String titulo, boolean lido): void`
        <!-- - trazer livros com ordenação -->

4. **Classe `Usuario`**
    - **Atributos:**
        - `String username`
        - `String senha`
        - `List<Livro> favoritos`
        - `List<ListaLeitura> listasDeLeitura`
        - `List<Livro> historicoLeitura`
    - **Métodos:**
        - `autenticar(String username, String senha): boolean`
        - `adicionarFavorito(Livro livro): void`
        - `removerFavorito(String titulo): boolean`
        - `criarListaLeitura(String nome): ListaLeitura`
        - `adicionarLivroNaLista(String nomeLista, Livro livro): void`
        - `removerLivroDaLista(String nomeLista, String titulo): boolean`

5. **Classe `TabelaHashUsuarios`**
    - **Atributos:**
        - `HashMap<String, Usuario> usuarios`
    - **Métodos:**
        - `criarUsuario(String username, String senha): boolean`
        - `obterUsuario(String username): Usuario`
        - `removerUsuario(String username): boolean`

6. **Classe `Recomendador`**
    - **Atributos:**
        - `TabelaHashUsuarios tabelaUsuarios`
    - **Métodos:**
        - `gerarRecomendacoes(Usuario usuario): List<Livro>`
        - `analisarPreferencias(Usuario usuario): Map<String, Integer>`

7. **Classe `InterfaceUsuario`**
    - **Atributos:**
        - `Biblioteca biblioteca`
        - `TabelaHashUsuarios tabelaUsuarios`
        - `Recomendador recomendador`
        - `Usuario usuarioAtual`
    - **Métodos:**
        - `mostrarMenuPrincipal(): void`
        - `registrarUsuario(String username, String senha): void`
        - `login(String username, String senha): void`
        - `logout(): void`
        - `interagirComBiblioteca(): void`
        - `gerenciarListasDeLeitura(): void`
        - `visualizarRecomendacoes(): void`
        - `marcarFavorito(String titulo): void`

### Relacionamentos entre Classes

- **`Biblioteca`** utiliza uma **`ListaDuplamenteEncadeada`** para armazenar instâncias de **`Livro`**.
- **`Usuario`** possui listas de **`ListaLeitura`**, uma lista de livros favoritos e um histórico de leitura.
- **`TabelaHashUsuarios`** gerencia instâncias de **`Usuario`** através de um **`HashMap`**.
- **`Recomendador`** interage com **`TabelaHashUsuarios`** para gerar recomendações personalizadas.
- **`InterfaceUsuario`** atua como a camada de apresentação, interagindo com **`Biblioteca`**, **`TabelaHashUsuarios`** e **`Recomendador`**.
- **`ListaLeitura`** utiliza uma **`CircularList`** para gerenciar listas de leitura personalizadas.
