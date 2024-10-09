import java.util.Scanner;

public class copilot_exercises_2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.printf("Digite a primeira nota: ");
        double nota1 = scanner.nextDouble();
        System.out.printf("Digite a segunda nota: ");
        double nota2 = scanner.nextDouble();
        double media = (nota1 + nota2) / 2;
        if (media >= 7) {
            System.out.printf("A média é %.2f. O aluno foi aprovado", media);
        } else if (media < 5) {
            System.out.printf("A média é %.2f. O aluno foi reprovado", media);
        } else {
            System.out.printf("A média é %.2f. O aluno está de recuperação", media);
        }
        scanner.close();
    }
}