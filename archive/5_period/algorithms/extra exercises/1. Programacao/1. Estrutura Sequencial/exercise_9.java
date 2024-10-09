import java.util.Scanner;
public class exercise_9 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o valor da Altura do Trapézio: ");
        double a = scanner.nextDouble();
        System.out.println("Digite o valor da Base Maior do Trapézio: ");
        double B = scanner.nextDouble();
        System.out.println("Digite o valor da Base Menor do Trapézio: ");
        double b = scanner.nextDouble();
        System.out.println("Área = (Base Maior + Base Menor) * Altura");
        System.out.printf("Área = (%f + %f) * %f = %.3f", B, b, a, ((B + b) * a)/2);
        scanner.close();
    }
}