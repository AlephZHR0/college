import java.util.Scanner;
public class exercise_2 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o primeiro numero");
        int num1 = scanner.nextInt();
        System.out.println("Digite o segundo numero");
        int num2 = scanner.nextInt();
        System.out.println("Digite o terceiro numero");
        int num3 = scanner.nextInt();

        int multiplicacao = multiplica_3_numeros(num1, num2, num3);
        System.out.printf("A multiplicação dos numeros %d * %d * %d = %d", num1, num2, num3, multiplicacao);
        scanner.close();
    }
    public static int multiplica_3_numeros(int num1, int num2, int num3) {
        return num1 * num2 * num3;
    }
}