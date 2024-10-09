import java.util.Scanner;
public class exercise_1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o primeiro número");
        int num1 = scanner.nextInt();
        System.out.println("Digite o primeiro número");
        int num2 = scanner.nextInt();
        int soma = somaDeDoisNumeros(num1, num2);
        System.out.println("O resultado da soma de " + num1 + " + " + num2 + " = " + soma);
        scanner.close();
    }
    public static int somaDeDoisNumeros(int num1, int num2) {
        return num1 + num2;
    }
}