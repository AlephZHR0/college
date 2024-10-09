import java.util.Scanner;
public class exercise_16 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o raio da esfera");
        double raio = scanner.nextDouble();
        double comprimento_esfera = 2 * Math.PI * raio;
        double area_esfera = Math.PI * Math.pow(raio, 2);
        double volume_esfera = 3/4 * Math.PI * Math.pow(raio, 3);
        System.out.printf("Comprimento da esfera = %f", comprimento_esfera);
        System.out.printf("Área da esfera = %f", area_esfera);
        System.out.printf("Volume da esfera = %f", volume_esfera);
        scanner.close();
    }
}