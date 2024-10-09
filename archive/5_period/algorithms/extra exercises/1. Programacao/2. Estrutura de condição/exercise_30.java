import java.util.Scanner;
public class exercise_30 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite valor");
        double valor = scanner.nextDouble();
        if (valor < 500) {
            System.out.printf("Novo salário: %f", valor * 1.3);
        } else {
            System.out.println("Você não recebeu o aumento.");
        }
        scanner.close();
    }
}