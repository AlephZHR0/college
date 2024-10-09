public class Main {
    public static void main(String[] args) {
        FilaDinamica fila = new FilaDinamica();
        fila.enqueue(1);
        fila.enqueue(2);
        fila.enqueue(3);
        fila.enqueue(4);
        fila.enqueue(5);
        fila.dequeue();
        fila.peek();
        fila.show();
        fila.size();
    }
}
