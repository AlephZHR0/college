import java.util.Scanner;
public class copilot_exercises_4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite um número para obter sua tabuada: ");
        int num = scanner.nextInt();
        for (int i=0; i<= 10; i++) {
            System.out.printf("%d x %d = %d\n", num, i, num * i);
        }
        scanner.close();
    }
}