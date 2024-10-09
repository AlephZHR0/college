import java.util.Scanner;
public class exercise_15 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o valor do cateto 1");
        double cateto1 = scanner.nextDouble();
        System.out.println("Digite o valor do cateto 2");
        double cateto2 = scanner.nextDouble();
        double hip = Math.sqrt(Math.pow(cateto1, 2) + Math.pow(cateto2, 2));
        System.out.printf("Hipotenusa = %f", hip);
        scanner.close();
    }
}