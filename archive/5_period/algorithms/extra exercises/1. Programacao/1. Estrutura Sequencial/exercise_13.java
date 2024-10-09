import java.util.Scanner;
public class exercise_13 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o ano de nascimento");
        int ano_nascimento = scanner.nextInt();
        System.out.println("Digite o ano atual");
        int ano_atual = scanner.nextInt();
        int idade = ano_atual - ano_nascimento;
        System.out.printf("Sua idade é %f anos", idade);
        System.out.printf("Sua idade é %f meses", idade * 12);
        System.out.printf("Sua idade é %f dias", idade * 365);
        System.out.printf("Sua idade é %f semanas", idade * 365 / 7);
        scanner.close();
    }
}