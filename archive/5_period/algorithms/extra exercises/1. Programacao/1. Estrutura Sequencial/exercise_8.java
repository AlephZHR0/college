import java.util.Scanner;
public class exercise_8 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite seu peso (Kg)");
        double peso_em_kg = scanner.nextDouble();
        double peso_em_g = peso_em_kg * 1000;
        System.out.printf("%f kg = %f g", peso_em_kg, peso_em_g);
        scanner.close();
    }
}