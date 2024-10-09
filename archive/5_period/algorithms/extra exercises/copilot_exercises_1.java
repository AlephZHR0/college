import java.util.Scanner;

public class copilot_exercises_1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.printf("Digite um número: ");
        int choice = scanner.nextInt();
        if (choice % 2 == 0) {
            System.out.printf("O número %d é um número par", choice);
        } else {
            System.out.printf("O número %d é um número ímpar", choice);
        }
        scanner.close();
    }
}