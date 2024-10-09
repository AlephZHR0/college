public class ContaBancaria {
    int numeroDaConta;
    double saldo;
    String titular;

    public void setNumeroDaConta(int numeroDaConta) {
        this.numeroDaConta = numeroDaConta;
    }
    public void setSaldo(int saldo) {
        this.saldo = saldo;
    }
    public void setTitular(String titular) {
        this.titular = titular;
    }
    
    public int getNumeroDaConta() {
        return this.numeroDaConta;
    }
    public double getSaldo() {
        return this.saldo;
    }
    public String getTitular() {
        return this.titular;
    }

    public ContaBancaria(int numeroDaConta, double saldo, String titular) {
        this.numeroDaConta = numeroDaConta;
        this.saldo = saldo;
        this.titular = titular;
    }

    public void sacar(double quantidade) {
        this.saldo -= quantidade;
        System.out.printf("Foi sacado %f.\n", quantidade);
        System.out.printf("Seu saldo final é de %f\n", this.saldo);
    }

    public void depositar(double quantidade) {
        this.saldo += quantidade;
        System.out.printf("Foi depositado %f.\n", quantidade);
        System.out.printf("Seu saldo final é de %f.\n", this.saldo);
    }
}
