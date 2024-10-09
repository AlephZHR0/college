import java.util.Scanner;
public class exercise_22 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o valor em reais");
        double dinheiro_inicial = scanner.nextDouble();
        double conversao_dolar = 1.80;
        double marco_alemao = 2.00;
        double libra_esterlina = 3.57;
        
        System.out.printf("O valor em dólar é: %.2f\n", converte_moeda(dinheiro_inicial, conversao_dolar));
        System.out.printf("O valor em marco alemão é: %.2f\n", converte_moeda(dinheiro_inicial, marco_alemao));
        System.out.printf("O valor em libra esterlina é: %.2f\n", converte_moeda(dinheiro_inicial, libra_esterlina));
        
        scanner.close();
    }
    public static double converte_moeda(double dinheiro_inicial, double conversao) {
        return dinheiro_inicial * conversao;
    }
}