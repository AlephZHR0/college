import java.util.Scanner;
public class exercise_12 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o valor do salário mínimo");
        double valor_salario_minimo = scanner.nextDouble();
        System.out.println("Digite o valor do salário do funcionário");
        double valor_salario_funcionario = scanner.nextDouble();
        System.out.printf("Esse funcionário recebe %f salários mínimos", valor_salario_funcionario / valor_salario_minimo);
        scanner.close();
    }
}