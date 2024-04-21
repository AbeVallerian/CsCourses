package textgen;

import java.util.AbstractList;


/** A class that implements a doubly linked list
 * 
 * @author UC San Diego Intermediate Programming MOOC team
 *
 * @param <E> The type of the elements stored in the list
 */
public class MyLinkedList<E> extends AbstractList<E> {
	LLNode<E> head;
	LLNode<E> tail;
	int size;

	/** Create a new empty LinkedList */
	public MyLinkedList() {
		head = null;
		tail = null;
		size = 0;
	}

	/**
	 * Appends an element to the end of the list
	 * @param element The element to add
	 */
	public boolean add(E element) 
	{
		if (element == null) {
			throw new NullPointerException("element cannot be null");
		}
		
		LLNode<E> newNode = new LLNode<E>(element);
		if (size == 0) {
			head = newNode;
			tail = newNode;
		} else {
			newNode.prev = tail;
			newNode.next = null;
			tail.next = newNode;
			tail = newNode;
		}
		size += 1;
		return false;
	}

	/** Get the element at position index 
	 * @throws IndexOutOfBoundsException if the index is out of bounds. */
	public E get(int index) 
	{
		if (index >= size) {
			throw new IndexOutOfBoundsException("index is larger or equal than list size");
		}
		if (index < 0) {
			throw new IndexOutOfBoundsException("index cannot be negative");
		}
		LLNode<E> currNode = head;
		for(int i=index; i > 0; i--) {
			currNode = currNode.next;
		}
		return currNode.data;
	}
	
	/**
	 * Add an element to the list at the specified index
	 * @param The index where the element should be added
	 * @param element The element to add
	 */
	public void add(int index, E element) 
	{
		if (element == null) {
			throw new NullPointerException("element cannot be null");
		}
		
		if (index > size) {
			throw new IndexOutOfBoundsException("index is larger than list size");
		}
		if (index < 0) {
			throw new IndexOutOfBoundsException("index cannot be negative");
		}
		
		if(index == size) {
			add(element);
		} else {
			LLNode<E> currNode = head;
			for(int i=index; i > 0; i--) {
				currNode = currNode.next;
			}
			
			LLNode<E> newNode = new LLNode<E>(element);
			newNode.prev = currNode.prev;
			newNode.next = currNode;
			if (newNode.prev != null) {
				newNode.prev.next = newNode;
			} else {
				head = newNode;
			}
			newNode.next.prev = newNode;
			
			size += 1;
		}
	}


	/** Return the size of the list */
	public int size() 
	{
		return size;
	}

	/** Remove a node at the specified index and return its data element.
	 * @param index The index of the element to remove
	 * @return The data element removed
	 * @throws IndexOutOfBoundsException If index is outside the bounds of the list
	 * 
	 */
	public E remove(int index) 
	{		
		if (index >= size) {
			throw new IndexOutOfBoundsException("index is larger than list size");
		}
		if (index < 0) {
			throw new IndexOutOfBoundsException("index cannot be negative");
		}
		
		LLNode<E> currNode = head;
		for(int i=index; i > 0; i--) {
			currNode = currNode.next;
		}
		
		E currData = currNode.data;
		
		if (currNode.prev == null) {
			head = currNode.next;
		} else {
			currNode.prev.next = currNode.next;
		}
		if (currNode.next == null) {
			tail = currNode.prev;
		} else {
			currNode.next.prev = currNode.prev;
		}
		
		currNode.prev = null;
		currNode.next = null;
		
		size -= 1;
		
		return currData;
	}

	/**
	 * Set an index position in the list to a new element
	 * @param index The index of the element to change
	 * @param element The new element
	 * @return The element that was replaced
	 * @throws IndexOutOfBoundsException if the index is out of bounds.
	 */
	public E set(int index, E element) 
	{
		if (element == null) {
			throw new NullPointerException("element cannot be null");
		}
		
		if (index >= size) {
			throw new IndexOutOfBoundsException("index is larger or equal than list size");
		}
		if (index < 0) {
			throw new IndexOutOfBoundsException("index cannot be negative");
		}
		
		LLNode<E> currNode = head;
		for(int i=index; i > 0; i--) {
			currNode = currNode.next;
		}
		
		E oldData = currNode.data;
		currNode.data = element;
		
		return oldData;
	}   
}

class LLNode<E> 
{
	LLNode<E> prev;
	LLNode<E> next;
	E data;

	public LLNode(E e) 
	{
		this.data = e;
		this.prev = null;
		this.next = null;
	}

}
