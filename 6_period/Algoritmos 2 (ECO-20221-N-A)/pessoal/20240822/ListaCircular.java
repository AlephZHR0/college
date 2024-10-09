public class ListaCircular {
    private No inicio = null;

    public void InserirNoInicio(int dado) {
        No novoNo = new No(dado);
        if (inicio == null) {
            inicio = novoNo;
            inicio.setProximoNo(inicio);
        } else {
            No temp = inicio;
            while (temp.getProximoNo() != inicio) {
                temp = temp.getProximoNo();
            }
            novoNo.setProximoNo(inicio);
            temp.setProximoNo(novoNo);
            inicio = novoNo;
        }
    }

    public void inserirNoFim(int dado) {
        No novoNo = new No(dado);
        if (inicio == null) {
            inicio = novoNo;
            inicio.setProximoNo(inicio);
        } else {
            No temp = inicio;
            while (temp.getProximoNo() != inicio) {
                temp = temp.getProximoNo();
            }
            temp.setProximoNo(novoNo);
            novoNo.setProximoNo(inicio);
        }
    }

    public int deletarNo(int chave) {
        if (inicio == null) {
            return -1;
        }
        if (inicio.getDado() == chave && inicio.getProximoNo() == inicio) {
            int temp = inicio.getDado();
            inicio = null;
            return temp;
        }
        No auxiliar = inicio;
        if (inicio.getDado() == chave) {
            while (auxiliar.getProximoNo() != inicio) {
                auxiliar = auxiliar.getProximoNo();
            }
            auxiliar.setProximoNo(inicio.getProximoNo());
            inicio = inicio.getProximoNo();
            return auxiliar.getDado();
        } else {
            No d = inicio;
            while (auxiliar.getProximoNo() != inicio && auxiliar.getProximoNo().getDado() != chave) {
                auxiliar = auxiliar.getProximoNo();
            }
            if (auxiliar.getProximoNo().getDado() == chave) {
                d = auxiliar.getProximoNo();
                auxiliar.setProximoNo(d.getProximoNo());
                return d.getDado();
            }
        }
        return -1;
    }

    public void mostrar() {
        if (inicio == null) {
            return;
        }
        No temp = inicio;
        do {
            System.out.println(temp.getDado());
            temp = temp.getProximoNo();
        } while (temp != inicio);
        System.out.println();
    }
}