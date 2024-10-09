import java.util.Scanner;
public class exercise_3 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o primeiro numero");
        float num1 = scanner.nextFloat();
        System.out.println("Digite o segundo numero");
        float num2 = scanner.nextFloat();

        float result = calc(num1, num2);

        System.out.printf("%f / %f = %.2f", num1, num2, result);

        scanner.close();
    }
    public static float calc(float num1, float num2) {
        return num1 / num2;
    }
    
}