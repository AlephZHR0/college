import java.util.Scanner;
public class exercise_20 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o número de lados do polígono");
        int numero_de_lados = scanner.nextInt();
        int numero_de_diagonais = (numero_de_lados * (numero_de_lados - 3)) / 2;
        System.out.printf("O número de diagonais do polígono é: %d", numero_de_diagonais);
        scanner.close();
    }
}