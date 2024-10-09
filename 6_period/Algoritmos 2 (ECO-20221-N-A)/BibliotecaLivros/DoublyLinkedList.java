import java.util.ArrayList;
import java.util.List;
import java.util.function.Predicate;

/**
 * Implementa uma lista duplamente encadeada genérica.
 *
 * @param <T> Tipo de dados armazenado na lista.
 */
public class DoublyLinkedList<T> {
    private Node<T> head;
    private Node<T> tail;

    /**
     * Verifica se a lista está vazia.
     *
     * @return true se a lista estiver vazia, false caso contrário.
     */
    public boolean isEmpty() {
        return head == null;
    }

    /**
     * Retorna o nó cabeça (head) da lista.
     *
     * @return O nó cabeça da lista.
     */
    public Node<T> getHead() {
        return head;
    }

    /**
     * Insere um elemento no início da lista.
     *
     * @param data Dado a ser inserido.
     */
    public void insertAtFront(T data) {
        Node<T> newNode = new Node<>(data);
        if (isEmpty()) {
            tail = newNode;
        } else {
            head.setPrev(newNode);
        }
        newNode.setNext(head);
        head = newNode;
    }

    /**
     * Insere um elemento no final da lista.
     *
     * @param data Dado a ser inserido.
     */
    public void insertAtBack(T data) {
        Node<T> newNode = new Node<>(data);
        if (isEmpty()) {
            head = newNode;
        } else {
            tail.setNext(newNode);
            newNode.setPrev(tail);
        }
        tail = newNode;
    }

    /**
     * Remove o primeiro elemento da lista.
     *
     * @return O dado removido.
     */
    public T removeFromFront() {
        if (isEmpty()) {
            return null;
        }
        T removedData = head.getData();
        if (head == tail) {
            head = tail = null;
        } else {
            head = head.getNext();
            head.setPrev(null);
        }
        return removedData;
    }

    /**
     * Remove o último elemento da lista.
     *
     * @return O dado removido.
     */
    public T removeFromBack() {
        if (isEmpty()) {
            return null;
        }
        T removedData = tail.getData();
        if (head == tail) {
            head = tail = null;
        } else {
            tail = tail.getPrev();
            tail.setNext(null);
        }
        return removedData;
    }

    /**
     * Remove um elemento que satisfaz uma condição.
     *
     * @param condition Condição para remoção.
     * @return true se um elemento foi removido, false caso contrário.
     */
    public boolean remove(Predicate<T> condition) {
        Node<T> current = head;
        while (current != null) {
            if (condition.test(current.getData())) {
                if (current == head) {
                    removeFromFront();
                } else if (current == tail) {
                    removeFromBack();
                } else {
                    current.getPrev().setNext(current.getNext());
                    current.getNext().setPrev(current.getPrev());
                }
                return true;
            }
            current = current.getNext();
        }
        return false;
    }

    /**
     * Converte a lista em uma lista do Java.
     *
     * @return Lista de elementos.
     */
    public List<T> toList() {
        List<T> list = new ArrayList<>();
        Node<T> current = head;
        while (current != null) {
            list.add(current.getData());
            current = current.getNext();
        }
        return list;
    }

    /**
     * Exibe os elementos da lista.
     */
    public void display() {
        Node<T> current = head;
        while (current != null) {
            System.out.println(current.getData().toString());
            current = current.getNext();
        }
    }
}
