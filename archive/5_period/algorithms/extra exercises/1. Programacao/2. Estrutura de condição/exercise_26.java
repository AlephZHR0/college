import java.util.Scanner;
public class exercise_26 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o primeiro número");
        double numero1 = scanner.nextDouble();
        System.out.println("Digite o segundo número");
        double numero2 = scanner.nextDouble();
        if (numero1 > numero2) {
            System.out.println(numero1);
        } else {
            System.out.println(numero2);
        }
        scanner.close();
    }
}