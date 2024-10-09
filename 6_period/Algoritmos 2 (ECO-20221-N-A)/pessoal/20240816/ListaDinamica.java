public class ListaDinamica {
    private No inicio;
    private No fim;
    
    public ListaDinamica(){
       inicio = fim = null;
    }
    
    boolean isEmpty(){
       return (inicio == null);
    }

   void inserirAtFront(int dado){
      if (isEmpty()){
         inicio = new No(dado);
         fim = inicio;
      }else {
         No novoNo = new No(dado);
         novoNo.setProximoNo(inicio);
         inicio = novoNo;
      }
   }

   void inserirAtBack(int dado){
      if (isEmpty()){
         inicio = new No(dado);
         fim = inicio;
      }else {
         No novoNo = new No(dado);
         fim.setProximoNo(novoNo);
         fim = novoNo;
      }
   }
   
   int removeFromFront() {
       if (isEmpty()) {
           return -1; 
       }
       int value = inicio.getDado();
       if (inicio == fim) { 
           inicio = fim = null;
       } else {
           inicio = inicio.getProximoNo();
       }
       return value;
   }
   
   int removeFromBack() {
       if (isEmpty()) {
           return -1; 
       }
       int valorRemovido = fim.getDado();
       if (inicio == fim) { 
           inicio = fim = null;
       } else {
           No atual = inicio;
           while (atual.getProximoNo() != fim) {
               atual = atual.getProximoNo();
           }
           fim = atual;
           atual.setProximoNo(null);
       }
       return valorRemovido;
   }
   
   No find(int dado){
      if (isEmpty()){
         return null; 
      }else{
         No atual = inicio;
         while (atual != null){
            if (atual.getDado() == dado){
               return atual;
            }
            atual = atual.getProximoNo(); 
         }
         return null;
      }
   }
   
   boolean remove(int item) {
       if (isEmpty()) {
           return false; 
       }

       No anterior = null;
       No atual = inicio;

       while (atual != null && atual.getDado() != item) {
           anterior = atual;
           atual = atual.getProximoNo();
       }
       if (atual == null) {
           return false; 
       }
       if (atual == inicio) { 
           removeFromFront();
      }   else if (atual == fim) { 
           removeFromBack();
      }   else { 
           anterior.setProximoNo(atual.getProximoNo());
       }
       return true;
    }
    
    void exibirLista() {
        if (isEmpty()) {
            System.out.println("Lista Vazia");
            return;
        }

        System.out.println("Dados na Lista:");
        No atual = inicio; 

        while (atual != null) {
            System.out.print(atual.getDado() + " ");
            atual = atual.getProximoNo(); 
        }
        System.out.println(); 
    }
}