import java.util.Scanner;

public class exercise_28 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o primeiro número");
        double numero1 = scanner.nextDouble();
        System.out.println("Digite o segundo número");
        double numero2 = scanner.nextDouble();
        System.out.println("Escolha uma das seguintes opções:");
        System.out.println("1. Média entre os números digitados");
        System.out.println("2. Diferença do maior pelo menor");
        System.out.println("3. Produto entre os números digitados");
        System.out.println("4. Divisão do primeiro pelo segundo");
        int option = scanner.nextInt();
        scanner.close();
        switch (option) {
            case 1:
                System.out.printf("A média entre %f e %f = %f", numero1, numero2, (numero1 + numero2) / 2);
                break;
            case 2:
                if (numero1 > numero2) {
                    System.out.printf("A diferença entre %f e %f = %f", numero1, numero2, numero1 - numero2);
                } else {
                    System.out.printf("A diferença entre %f e %f = %f", numero2, numero1, numero2 - numero1);
                }
                break;
            case 3:
                System.out.printf("O produto entre %f e %f = %f", numero1, numero2, numero1 * numero2);
                break;
            case 4:
                System.out.printf("A divisão entre %f e %f = %f", numero1, numero2, numero1 / numero2);
        }
    }
}