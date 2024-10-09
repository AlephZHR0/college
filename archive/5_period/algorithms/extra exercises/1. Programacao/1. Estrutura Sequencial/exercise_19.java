import java.util.Scanner;
public class exercise_19 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o valor do salário mínimo");
        double salario_minimo = scanner.nextDouble();
        System.out.println("Digite o número de horas trabalhadas");
        double horas_trabalhadas = scanner.nextDouble();
        System.out.println("Digite o número de horas extras");
        double horas_extras = scanner.nextDouble();

        double valor_a_receber = salary_calc(horas_trabalhadas, salario_minimo, horas_extras);
        System.out.println("O valor a receber é: " + valor_a_receber);

        scanner.close();
    }
    public static double salary_calc(double horas_trabalhadas, double salario_minimo, double horas_extras) {
        double valor_hora_trabalhada = horas_trabalhadas * salario_minimo * 1/8;
        double valor_hora_extras = horas_extras * salario_minimo * 1/4;
        double receber_horas_trabalhadas = horas_trabalhadas * valor_hora_trabalhada;
        double receber_horas_extras = horas_extras * valor_hora_extras;
        return receber_horas_trabalhadas + receber_horas_extras;
    }
}