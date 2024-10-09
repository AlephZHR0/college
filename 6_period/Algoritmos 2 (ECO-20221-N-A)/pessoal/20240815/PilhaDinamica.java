public class PilhaDinamica {
    private No topo;

    public PilhaDinamica() {
        topo = null;
    }

    public void push(int dado){
        No novoNo = new No(dado);
        novoNo.setProximoNo(topo);
        topo = novoNo;
    }

    public int pop(){
        if (isEmpty()) {
            return -1;
        } else {
            No temp = topo;
            topo = topo.getProximoNo();
            return temp.getDado();
        }
    }

    public int peek(){
        if (isEmpty()) {
            return -1;
        } else {
            return topo.getDado();
        }
    }

    public int size(){
        No aux = topo;
        int cont = 0;
        while (aux != null) {
            aux = aux.getProximoNo();
            cont++;
        }
        return cont;
    }

    public boolean isEmpty(){
        return topo == null;
    }

    public String Display(){
        String retorno = "";
        if (isEmpty()) {
            retorno = "Pilha vazia";
        } else {
            No aux = topo;
            while (aux != null) {
                retorno += aux.getDado() + " ";
                aux = aux.getProximoNo();
            }
        }
        return retorno;
    }
}
