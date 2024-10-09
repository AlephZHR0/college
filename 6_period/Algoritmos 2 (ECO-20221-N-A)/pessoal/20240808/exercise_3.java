import java.util.Scanner;
import java.util.List;
import java.util.Arrays;
public class exercise_3 {
    public static void main(String[] args) {
        int count_vogais = 0;
        int count_consoantes = 0;
        List<Character> vogais = Arrays.asList('a', 'e', 'i', 'o', 'u');
        List<Character> numbers = Arrays.asList('0', '1', '2', '3', '4', '5', '6', '7', '8', '9');
        String espaco = " ";
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite uma string: ");
        String word = scanner.nextLine();
        scanner.close();
        word = word.toLowerCase();
        for (int i = 0; i < word.length(); i++) {
            if (vogais.contains(word.charAt(i))) {
                count_vogais++;
            } else if (numbers.contains(word.charAt(i))) {
                continue;
            } else if (word.charAt(i) == espaco.charAt(0)) {
                continue;}
             else {
                count_consoantes++;
            }
        }
        System.out.printf("Número de vogais: %d, Número de consoantes: %d", count_vogais, count_consoantes);
    }
}
