import java.util.Scanner;
public class exercise_18 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double dimensao1 = scanner.nextDouble();
        double dimensao2 = scanner.nextDouble();
        double area = dimensao1 * dimensao2;
        double potencia_total_necessaria = 18 * area;
        System.out.printf("A área é %f m²", area);
        System.out.printf("A potência total necessária é %f", potencia_total_necessaria);
        scanner.close();
    }
}