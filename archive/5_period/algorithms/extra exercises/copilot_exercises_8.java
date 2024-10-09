public class copilot_exercises_8 {
    public static void main(String[] args) {
        ContaBancaria conta = new ContaBancaria(123, 1000.0, "João");
        conta.sacar(500.0);
        conta.depositar(250.0);
        conta.sacar(750.0);
    }
}