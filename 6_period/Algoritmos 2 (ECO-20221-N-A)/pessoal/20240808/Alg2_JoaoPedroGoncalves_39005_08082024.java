// João Pedro Gonçalves (39005)

import java.util.Scanner;

public class Alg2_JoaoPedroGoncalves_39005_08082024 {
    public static void isPalindrome(String word) {
        String wordReverse = "";
        for (int i = word.length() - 1; i >= 0; i--) {
            wordReverse += word.charAt(i);
            System.out.println(wordReverse);
        }
        // wordReverse = new StringBuilder(word).reverse().toString();
        if (wordReverse.equals(word)) {
            System.out.println("A palavra é um palíndromo.");
        } else {
            System.out.println("A palavra não é um palíndromo.");
        }
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite uma palavra: ");
        String word = scanner.nextLine();
        scanner.close();
        String lowerCaseWord = word.toLowerCase();
        isPalindrome(lowerCaseWord);

    }
}
