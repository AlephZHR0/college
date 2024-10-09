public class BombaCombustivel {
    private String tipoCombustivel;
    private double valorLitro;
    private double quantidadeCombustivel;
    
    public void alterarValor(double valor) {
        this.valorLitro = valor;
    }

    public void alterarCombustivel(String combustivel) {
        this.tipoCombustivel = combustivel;
    }

    public void alterarQuantidadeCombustivel(double quantidade) {
        this.quantidadeCombustivel = quantidade;
    }

    public void AbastecerPorValor(double Valor){
        double litros = Valor / this.valorLitro;
        System.out.printf("A quantidade de gasolina é %.2f", litros);
        alterarQuantidadeCombustivel(this.quantidadeCombustivel - litros);
        System.out.printf("A nova quantidade de gasolina na bomba é %.2f", this.quantidadeCombustivel);
    }

    public void abastecerPorLitro(double litros) {
        double valor = litros * this.valorLitro;
        System.out.printf("O valor a ser pago é %.2f", valor);
        alterarQuantidadeCombustivel(this.quantidadeCombustivel - litros);
        System.out.printf("A nova quantidade de gasolina na bomba é %.2f", this.quantidadeCombustivel);
    }
}