import java.util.Random;

public class Main {
    public static void main(String[] args) {
        // Tamanhos dos vetores
        int[] tamanhos = {10, 100, 1000, 10000, 100000, 1000000};

        // Criando vetores e preenchendo com números aleatórios
        for (int tamanho : tamanhos) {
            int[] vetor = gerarVetorAleatorio(tamanho);
            System.out.println("Vetor de tamanho " + tamanho + " gerado.");

            // Bubble Sort
            int[] vetorBubble = vetor.clone();
            long inicioBubble = System.currentTimeMillis();
            BubbleSort.bubbleSort(vetorBubble);
            long fimBubble = System.currentTimeMillis();
            System.out.println("BubbleSort - Tamanho: " + tamanho + "Começou: " + inicioBubble + " Terminou: " + fimBubble + "ms");

            // Selection Sort
            int[] vetorSelection = vetor.clone();
            long inicioSelection = System.currentTimeMillis();
            SelectionSort.selectionSort(vetorSelection);
            long fimSelection = System.currentTimeMillis();
            System.out.println("SelectionSort - Tamanho: " + tamanho + "Começou: " + inicioSelection + " Terminou: " + fimSelection + "ms");

            // Insertion Sort
            int[] vetorInsertion = vetor.clone();
            long inicioInsertion = System.currentTimeMillis();
            InsertionSort.insertionSort(vetorInsertion);
            long fimInsertion = System.currentTimeMillis();
            System.out.println("InsertionSort - Tamanho: " + tamanho + "Começou: " + inicioInsertion + " Terminou: " + fimInsertion + "ms");

            // Merge Sort
            int[] vetorMerge = vetor.clone();
            long inicioMerge = System.currentTimeMillis();
            MergeSort.mergeSort(vetorMerge, 0, vetorMerge.length - 1);
            long fimMerge = System.currentTimeMillis();
            System.out.println("MergeSort - Tamanho: " + tamanho + "Começou: " + inicioMerge + " Terminou: " + fimMerge + "ms");

            // Quick Sort
            int[] vetorQuick = vetor.clone();
            long inicioQuick = System.currentTimeMillis();
            QuickSort.quickSort(vetorQuick, 0, vetorQuick.length - 1);
            long fimQuick = System.currentTimeMillis();
            System.out.println("QuickSort - Tamanho: " + tamanho + "Começou: " + inicioQuick + " Terminou: " + fimQuick + "ms");
        }
    }

    /**
     * Gera um vetor de números aleatórios de um determinado tamanho.
     * 
     * @param tamanho Tamanho do vetor a ser gerado
     * @return Vetor preenchido com números aleatórios
     */
    public static int[] gerarVetorAleatorio(int tamanho) {
        int[] vetor = new int[tamanho];
        Random random = new Random();

        for (int i = 0; i < tamanho; i++) {
            vetor[i] = random.nextInt(); // Preenche com números aleatórios
        }

        return vetor;
    }
}
