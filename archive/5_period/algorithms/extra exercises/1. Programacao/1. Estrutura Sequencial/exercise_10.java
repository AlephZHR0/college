import java.util.Scanner;
public class exercise_10 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o tamanho do primeiro lado");
        double lado1 = scanner.nextDouble();
        System.out.println("Digite o tamanho do segundolado");
        double lado2 = scanner.nextDouble();
        System.out.println("Área = lado * lado");
        System.out.printf("Área = %f * %f = %.3f", lado1, lado2, lado1 * lado2);
        scanner.close();
    }
}