import java.util.ArrayList;
import java.util.List;
import java.util.function.Predicate;

/**
 * Implementa uma lista circular genérica.
 *
 * @param <T> Tipo de dados armazenado na lista.
 */
public class CircularLinkedList<T> {
    private Node<T> last;

    /**
     * Verifica se a lista está vazia.
     *
     * @return true se a lista estiver vazia, false caso contrário.
     */
    public boolean isEmpty() {
        return last == null;
    }

    /**
     * Insere um elemento na lista.
     *
     * @param data Dado a ser inserido.
     */
    public void insert(T data) {
        Node<T> newNode = new Node<>(data);
        if (isEmpty()) {
            last = newNode;
            last.setNext(last);
        } else {
            newNode.setNext(last.getNext());
            last.setNext(newNode);
            last = newNode;
        }
    }

    /**
     * Remove um elemento que satisfaz uma condição.
     *
     * @param condition Condição para remoção.
     * @return true se um elemento foi removido, false caso contrário.
     */
    public boolean remove(Predicate<T> condition) {
        if (isEmpty()) {
            return false;
        }

        Node<T> current = last.getNext();
        Node<T> prev = last;
        boolean found = false;

        do {
            if (condition.test(current.getData())) {
                if (current == last) {
                    if (current.getNext() == last) {
                        last = null;
                    } else {
                        prev.setNext(current.getNext());
                        last = prev;
                    }
                } else {
                    prev.setNext(current.getNext());
                    if (current == last.getNext()) {
                        last.setNext(current.getNext());
                    }
                }
                found = true;
                break;
            }
            prev = current;
            current = current.getNext();
        } while (current != last.getNext());

        return found;
    }

    /**
     * Exibe os elementos da lista.
     */
    public void display() {
        if (isEmpty()) {
            System.out.println("A lista está vazia.");
            return;
        }

        Node<T> first = last.getNext();
        Node<T> current = first;

        do {
            System.out.println(current.getData().toString());
            current = current.getNext();
        } while (current != first);
    }

    /**
     * Converte a lista circular em uma lista padrão.
     *
     * @return Lista de elementos.
     */
    public List<T> toList() {
        List<T> list = new ArrayList<>();
        if (isEmpty()) {
            return list;
        }

        Node<T> first = last.getNext();
        Node<T> current = first;

        do {
            list.add(current.getData());
            current = current.getNext();
        } while (current != first);

        return list;
    }
}
