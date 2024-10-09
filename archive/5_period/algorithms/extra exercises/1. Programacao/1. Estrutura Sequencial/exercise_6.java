import java.util.Scanner;
public class exercise_6 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o salário");
        double salario = scanner.nextDouble();
        System.out.println("Digite valor das vendas");
        double valor_das_vendas = scanner.nextDouble();
        scanner.close();
        double salario_final = calc_salario_final(salario, valor_das_vendas);
        System.out.printf("O salário final vai ser de %.2f", salario_final);
    }
    public static double calc_salario_final(double salario, double valor_das_vendas) {
        return salario + valor_das_vendas * 0.04;
    }
}