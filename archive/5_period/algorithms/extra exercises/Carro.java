public class Carro {
    String marca;
    String modelo;
    int ano;

    public void setMarca(String marca) {
        this.marca = marca;
    }
    public void setModelo(String modelo) {
        this.modelo = modelo;
    }
    public void setAno(int ano) {
        this.ano = ano;
    }
    public String getMarca() {
        return this.marca;
    }
    public String getModelo() {
        return this.modelo;
    }
    public int getAno() {
        return this.ano;
    }

    public Carro() {
        this.marca = "Fiat";
        this.modelo = "Uno";
        this.ano = 2020;
    }
    public Carro(String marca, String modelo, int ano) {
        this.marca = marca;
        this.modelo = modelo;
        this.ano = ano;
    }

    public void acelerar() {
        System.out.printf("%s %s está acelerando...\n", this.marca, this.modelo);
    }
}