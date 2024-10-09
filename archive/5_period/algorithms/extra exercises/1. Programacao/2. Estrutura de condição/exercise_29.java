import java.util.Scanner;
public class exercise_29 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o primeiro número");
        double numero1 = scanner.nextDouble();
        System.out.println("Digite o segundo número");
        double numero2 = scanner.nextDouble();
        scanner.close();
        System.out.println("Escolha uma das seguintes opções:");
        System.out.println("1. O primeiro número elevado ao segundo número");
        System.out.println("2. Raiz quadrada de cada um dos números");
        System.out.println("3. Raiz cúbica de cada um dos números");
        int option = scanner.nextInt();
        switch (option){
            case 1:
                System.out.println(Math.pow(numero1, numero2));
                break;
            case 2:
                System.out.printf("%f, %f", Math.sqrt(numero1), Math.sqrt(numero2));
                break;
            case 3:
                System.out.printf("%f, %f", Math.cbrt(numero1), Math.cbrt(numero2));
                break;
        }
    }
}