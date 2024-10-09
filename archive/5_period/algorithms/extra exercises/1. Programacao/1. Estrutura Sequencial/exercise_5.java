import java.util.Scanner;
public class exercise_5 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o preço original");
        double original_price = scanner.nextDouble();
        double reajust = 0.9;
        double new_price = original_price * reajust;
        System.out.printf("O preço %f com um aumento de %f = %f",original_price, reajust, new_price);
        scanner.close();
    }
}