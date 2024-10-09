import java.util.Scanner;
public class copilot_exercises_3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.printf("Digite quantos digitos da sequencia de Fibonacci você quer: ");
        int n = scanner.nextInt();
        System.out.printf("%d ", fibonacci(n));
        scanner.close();
    }
    public static int fibonacci(int n) {
        if (n == 0) {
            return 0;
        } else if (n == 1) {
            return 1;
        } else {
            return fibonacci(n-1) + fibonacci(n-2);
        }
    }
}