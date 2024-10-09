import java.util.Scanner;
public class exercise_4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite a primeira nota");
        float nota1 = scanner.nextFloat();
        System.out.println("Digite a segunda nota");
        float nota2 = scanner.nextFloat();

        float media = mediaNotas(nota1, nota2);

        System.out.printf("A média ponderada entre as notas %f e %f é: %.2f", nota1, nota2, media);


        scanner.close();
    }
    public static float mediaNotas(float nota1, float nota2) {
        return ((nota1 * 2) + (nota2 * 3)) / 5;
    }
}