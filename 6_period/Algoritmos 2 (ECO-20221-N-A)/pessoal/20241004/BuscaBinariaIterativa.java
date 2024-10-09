import java.util.Random;

public class BuscaBinariaIterativa {
    public static int buscaBinaria(int[] v, int valorProcurado) {
        int inicio = 0;
        int fim = v.length - 1;

        while (inicio <= fim) {
            int centro = (inicio + fim) / 2;

            if (v[centro] == valorProcurado) {
                return centro;
            }

            if (valorProcurado < v[centro]) {
                fim = centro - 1;
            } else {
                inicio = centro + 1;
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

        int valorProcurado = 7;

        int resultado = buscaBinaria(vetor, valorProcurado);

        if (resultado != -1) {
            System.out.println("Valor encontrado no índice: " + resultado);
        } else {
            System.out.println("Valor não encontrado.");
        }
    }
}
