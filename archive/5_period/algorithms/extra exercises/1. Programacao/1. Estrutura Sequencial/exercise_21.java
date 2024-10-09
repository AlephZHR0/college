import java.util.Scanner;
public class exercise_21 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o primeiro ângulo");
        double angulo1 = scanner.nextDouble();
        System.out.println("Digite o segundo ângulo");
        double angulo2 = scanner.nextDouble();
        double angulo3 = 180 - (angulo1 + angulo2);
        System.out.printf("O terceiro ângulo é: %.2f", angulo3);
        scanner.close();
    }
}