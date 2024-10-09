import java.util.Scanner;

public class exercise_2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite os números separados por espaço: ");
        String[] numbers = scanner.nextLine().split(" ");
        scanner.close();
        int even = 0;
        int odd = 0;
        for (int i = 0; i < numbers.length; i++) {
            if (Integer.parseInt(numbers[i]) % 2 == 0) {
                even++;
            } else {
                odd++;
            }
        }
        // format_string
        System.out.printf("Número de pares: %d, Número de ímpares: %d", even, odd);
    }
}
