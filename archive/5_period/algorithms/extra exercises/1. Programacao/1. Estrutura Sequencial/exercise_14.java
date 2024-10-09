import java.util.Scanner;
public class exercise_14 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o seu salário");
        double salario = scanner.nextDouble();
        System.out.println("Digite o valor da primeira conta");
        double conta1 = scanner.nextDouble();
        System.out.println("Digite o valor da segunda conta");
        double conta2 = scanner.nextDouble();
        double salario_restante = salario - (conta1 + conta2) * 1.02;
        System.out.printf("Do salário de %f vai sobrar %f", salario, salario_restante);
        scanner.close();
    }
}