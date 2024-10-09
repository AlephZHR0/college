import java.util.Scanner;
public class exercise_23 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite as horas");
        int horas = scanner.nextInt();
        System.out.println("Digite os minutos");
        int minutos = scanner.nextInt();
        int horas_to_Minutos = horas * 60;
        int minutos_to_Segundos = minutos * 60;
        System.out.printf("a hora digitada convertida em minutos é: %d\n", horas_to_Minutos);
        System.out.printf("o total de minutos é: %d\n", horas_to_Minutos + minutos);
        System.out.printf("o total dos minutos convertidos em segundos é: %d\n", minutos_to_Segundos);
        scanner.close();
    }
}