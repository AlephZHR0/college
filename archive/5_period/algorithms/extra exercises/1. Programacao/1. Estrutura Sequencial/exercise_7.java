import java.util.Scanner;
public class exercise_7 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite seu peso");
        double peso = scanner.nextDouble();
        System.out.printf("Se você engordar 15%%, seu novo peso será: %.3f\n", peso * 1.15);
        System.out.printf("Se você engordar 20%%, seu novo peso será: %.3f", peso * 1.20);
        scanner.close();
    }
}