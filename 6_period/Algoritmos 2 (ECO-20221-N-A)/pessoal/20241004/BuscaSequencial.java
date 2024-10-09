import java.util.Random;

public class BuscaSequencial {

    public static int buscaSequencial(int[] array, int valorProcurado) {
        for (int i = 0; i < array.length; i++) {
            if (array[i] == valorProcurado) {
                return i;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int tamanho = 10;
        int[] vetor = new int[tamanho];
        Random rand = new Random();

        for(int i = 0; i < tamanho; i++) {
            vetor[i] = rand.nextInt(10);
        }

        int valorProcurado = 5;

        int resultado = buscaSequencial(vetor, valorProcurado);

        if (resultado != -1) {
            System.out.println("Valor encontrado no índice: " + resultado);
        } else {
            System.out.println("Valor não encontrado.");
        }
    }
}
