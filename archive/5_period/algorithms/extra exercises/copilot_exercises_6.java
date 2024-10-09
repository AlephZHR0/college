import java.util.Scanner;
public class copilot_exercises_6 {
    public static void main(String[] args) {
        // Crie um método que recebe uma string e retorna a mesma string, mas com todas as letras em maiúsculas.
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite uma palavra para transformar em maiúscula: ");
        String palavra = scanner.nextLine();
        System.out.println(palavra.toUpperCase());
        scanner.close();
    }
}