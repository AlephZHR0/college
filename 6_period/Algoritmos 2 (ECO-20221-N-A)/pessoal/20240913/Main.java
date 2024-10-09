public class Main {
    /**
     * Ordena parcialmente os primeiros k elementos de um array utilizando o algoritmo de seleção.
     *
     * @param array O array de inteiros a ser ordenado parcialmente.
     * @param k     O número de elementos a serem ordenados.
     * @throws IllegalArgumentException se k for menor que 1 ou maior que o tamanho do array.
     */
    public static void partialSelectionSort(int[] array, int k) {
        if (k < 1 || k > array.length) {
            throw new IllegalArgumentException("O valor de k deve estar entre 1 e o tamanho do array.");
        }

        int tamanho = array.length;

        for (int i = 0; i < k; i++) {
            int indiceMinimo = i;

            // Encontra o índice do menor elemento no subarray não ordenado
            for (int j = i + 1; j < tamanho; j++) {
                if (array[j] < array[indiceMinimo]) {
                    indiceMinimo = j;
                }
            }

            // Troca o menor elemento encontrado com o elemento na posição i
            int temp = array[i];
            array[i] = array[indiceMinimo];
            array[indiceMinimo] = temp;
        }
    }

    /**
     * Ordena parcialmente os primeiros k elementos de um array utilizando o algoritmo QuickSort.
     *
     * @param array O array de inteiros a ser ordenado parcialmente.
     * @param low   O índice inicial do subarray a ser considerado.
     * @param high  O índice final do subarray a ser considerado.
     * @param k     O número de primeiros elementos a serem ordenados.
     * @throws IllegalArgumentException se k for menor que 1 ou maior que o tamanho do array.
     */
    public static void partialQuickSort(int[] array, int low, int high, int k) {
        if (k < 1 || k > array.length) {
            throw new IllegalArgumentException("O valor de k deve estar entre 1 e o tamanho do array.");
        }

        if (low < high) {
            int partitionIndex = partition(array, low, high);

            if (partitionIndex >= k) {
                partialQuickSort(array, low, partitionIndex - 1, k);
            } else {
                partialQuickSort(array, low, partitionIndex - 1, k);
                if (partitionIndex + 1 < k) {
                    partialQuickSort(array, partitionIndex + 1, high, k);
                }
            }
        }
    }

    /**
     * Particiona o array em torno de um pivô, colocando os elementos menores que o pivô à esquerda
     * e os maiores à direita.
     *
     * @param array O array de inteiros a ser particionado.
     * @param low   O índice inicial do subarray a ser particionado.
     * @param high  O índice final do subarray a ser particionado.
     * @return O índice de partição após a colocação do pivô.
     */
    private static int partition(int[] array, int low, int high) {
        int pivot = array[high];
        int indiceMenor = low - 1;

        for (int j = low; j < high; j++) {
            if (array[j] <= pivot) {
                indiceMenor++;
                trocar(array, indiceMenor, j);
            }
        }

        trocar(array, indiceMenor + 1, high);
        return indiceMenor + 1;
    }

    /**
     * Troca os elementos nas posições i e j do array.
     *
     * @param array O array de inteiros.
     * @param i     O índice do primeiro elemento a ser trocado.
     * @param j     O índice do segundo elemento a ser trocado.
     */
    private static void trocar(int[] array, int i, int j) {
        int temporario = array[i];
        array[i] = array[j];
        array[j] = temporario;
    }

    /**
     * Método auxiliar para imprimir os elementos do array.
     *
     * @param array O array de inteiros a ser impresso.
     */
    public static void imprimirArray(int[] array) {
        for (int elemento : array) {
            System.out.print(elemento + " ");
        }
        System.out.println();
    }

    /**
     * Método principal para demonstrar a ordenação parcial.
     *
     * @param args Argumentos de linha de comando (não utilizados).
     */
    public static void main(String[] args) {
        int[] dados1 = {64, 25, 12, 22, 11};
        int[] dados2 = {64, 25, 12, 22, 11};
        int k = 3;

        System.out.println("Array antes da ordenacao parcial:");
        imprimirArray(dados1);

        partialSelectionSort(dados1, k);

        System.out.println("Array apos a ordenacao parcial dos primeiros " + k + " elementos com selection sort parcial:");
        imprimirArray(dados1);

        System.out.println("Array antes da ordenacao parcial:");
        imprimirArray(dados2);

        partialQuickSort(dados2, 0, dados2.length - 1, k);

        System.out.println("Array apos a ordenacao parcial dos primeiros " + k + " elementos com quicksort parcial:");
        imprimirArray(dados2);
    }
}
