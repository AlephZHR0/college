import java.util.Scanner;
public class exercise_11 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o tamanho da diagonal maior");
        double diagonal_maior = scanner.nextDouble();
        System.out.println("Digite o tamanho da diagonal menor");
        double diagonal_menor = scanner.nextDouble();
        System.out.println("Área = (diagonal_maior * diagonal_menor)/2");
        System.out.printf("Área = %f * %f = %.3f", diagonal_maior, diagonal_menor, (diagonal_maior * diagonal_menor)/2);
        scanner.close();
    }
}