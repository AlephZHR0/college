public class FilaDinamica {
    private No primeiroNo;
    private No ultimoNo;

    public FilaDinamica() {
        this.primeiroNo = null;
        this.ultimoNo = null;
    }
    public boolean isEmpty() {
        if (this.primeiroNo == null) {
            return true;
        } else {
            return false;
        }
    }
    public void enqueue(int data) {
        if (this.primeiroNo == null) {
            this.primeiroNo = new No(data);
            this.ultimoNo = this.primeiroNo;        
        } else {
            this.ultimoNo.setProximoNo(new No(data));
            this.ultimoNo = this.ultimoNo.getProximoNo();
        }
    }
    public void dequeue() {
        if (this.primeiroNo != null){
            this.primeiroNo = this.primeiroNo.getProximoNo();
        }
    }
    public void show() {
        if (!isEmpty()) {
            No noAux = this.primeiroNo;
            while (noAux != null) {
                System.out.println(noAux.getDado());
                noAux = noAux.getProximoNo();
            }
        } else {
            System.out.println("Fila vazia");
        }
    }
    public void peek() {
        if (this.primeiroNo != null) {
            System.out.println(this.primeiroNo.getDado());
        } else {
            System.out.println("Fila vazia");
        }
    }
    public void size() {
        int contador = 0;
        if (!isEmpty()) {
            No noAux = this.primeiroNo;
            while (noAux != null) {
                noAux = noAux.getProximoNo();
                contador++;
            }
        }
        System.out.printf("Tamanho da fila: %d", contador);
    }
}
