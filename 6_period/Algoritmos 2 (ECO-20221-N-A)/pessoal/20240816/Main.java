public class Main {
    public static void main(String[] args) {
        ListaDinamica lista = new ListaDinamica();

        lista.exibirLista();
        lista.inserirAtFront(10);
        lista.inserirAtFront(5);
        lista.inserirAtBack(15);

        lista.exibirLista();

        No encontrado = lista.find(10);
        System.out.println("Encontrado: " + (encontrado != null ? encontrado.getDado() : "Não encontrado"));

        int removido = lista.removeFromFront();
        System.out.println("Removido do início: " + removido);

        removido = lista.removeFromBack();
        System.out.println("Removido do final: " + removido);

        boolean removidoComSucesso = lista.remove(12);
        System.out.println("Removido 12: " + removidoComSucesso);

        lista.exibirLista();
    }
}
