public class No {
    private int dado;
    private No proximoNo;
    public No(int dd) {
        this.dado = dd;
        this.proximoNo = null;
    }
    public void setDado(int dado) {
        this.dado = dado;
    }
    public int getDado() {
        return this.dado;
    }
    public void setProximoNo(No proximoNo) {
        this.proximoNo = proximoNo;
    }
    public No getProximoNo() {
        return this.proximoNo;
    }
}
