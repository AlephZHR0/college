import java.util.Scanner;
public class exercise_17 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double temp_celcius = scanner.nextDouble();
        double temp_fahrenheit = 180 * (temp_celcius + 32) / 100;
        System.out.printf("A temperatura em Fahrenheit é %f", temp_fahrenheit);
        scanner.close();
    }
}