/**
 * 
 */
package textgen;

import static org.junit.Assert.*;

import java.util.LinkedList;

import org.junit.Before;
import org.junit.Test;

/**
 * @author UC San Diego MOOC team
 *
 */
public class MyLinkedListTester {

	private static final int LONG_LIST_LENGTH = 10; 

	MyLinkedList<String> shortList;
	MyLinkedList<Integer> emptyList;
	MyLinkedList<Integer> longerList;
	MyLinkedList<Integer> list1;
	
	/**
	 * @throws java.lang.Exception
	 */
	@Before
	public void setUp() throws Exception {
		// Feel free to use these lists, or add your own
	    shortList = new MyLinkedList<String>();
		shortList.add("A");
		shortList.add("B");
		emptyList = new MyLinkedList<Integer>();
		longerList = new MyLinkedList<Integer>();
		for (int i = 0; i < LONG_LIST_LENGTH; i++)
		{
			longerList.add(i);
		}
		list1 = new MyLinkedList<Integer>();
		list1.add(65);
		list1.add(21);
		list1.add(42);
	}

	
	/** Test if the get method is working correctly.
	 */
	/*You should not need to add much to this method.
	 * We provide it as an example of a thorough test. */
	@Test
	public void testGet()
	{
		//test empty list, get should throw an exception
		try {
			emptyList.get(0);
			fail("Check out of bounds");
		}
		catch (IndexOutOfBoundsException e) {
			
		}
		
		// test short list, first contents, then out of bounds
		assertEquals("Check first", "A", shortList.get(0));
		assertEquals("Check second", "B", shortList.get(1));
		
		try {
			shortList.get(-1);
			fail("Check out of bounds");
		}
		catch (IndexOutOfBoundsException e) {
		
		}
		try {
			shortList.get(2);
			fail("Check out of bounds");
		}
		catch (IndexOutOfBoundsException e) {
		
		}
		// test longer list contents
		for(int i = 0; i<LONG_LIST_LENGTH; i++ ) {
			assertEquals("Check "+i+ " element", (Integer)i, longerList.get(i));
		}
		
		// test off the end of the longer array
		try {
			longerList.get(-1);
			fail("Check out of bounds");
		}
		catch (IndexOutOfBoundsException e) {
		
		}
		try {
			longerList.get(LONG_LIST_LENGTH);
			fail("Check out of bounds");
		}
		catch (IndexOutOfBoundsException e) {
		}
		
	}
	
	
	/** Test removing an element from the list.
	 * We've included the example from the concept challenge.
	 * You will want to add more tests.  */
	@Test
	public void testRemove()
	{	
		try {
			shortList.remove(-1);
			fail("Set element at negative index");
		} catch (IndexOutOfBoundsException e) {
		}
		try {
			shortList.remove(2);
			fail("Set element outbound");
		} catch (IndexOutOfBoundsException e) {
		}
		
		String letter1 = shortList.remove(0);
		assertEquals("Remove: check 'A' is correct ", "A", letter1);
		assertEquals("Remove: check element 0 is correct ", "B", shortList.get(0));
		assertEquals("Remove: check size is correct ", 1, shortList.size());
		
		String letter2 = shortList.remove(0);
		assertEquals("Remove: check 'B' is correct ", "B", letter2);
		assertEquals("Remove: check size is correct ", 0, shortList.size());
		
		int a = list1.remove(0);
		assertEquals("Remove: check a is correct ", 65, a);
		assertEquals("Remove: check element 0 is correct ", (Integer)21, list1.get(0));
		assertEquals("Remove: check size is correct ", 2, list1.size());
		
	}
	
	/** Test adding an element into the end of the list, specifically
	 *  public boolean add(E element)
	 * */
	@Test
	public void testAddEnd()
	{
		try {
			list1.add(0, null);
			fail("Add null element");
		} catch (NullPointerException e) {
		}
		
		emptyList.add(0);
		assertEquals("Add: check new added int 0", (Integer)0, emptyList.get(0));
		
		longerList.add(999);
		assertEquals("Add: check new added int 999", (Integer)999, longerList.get(10));
	}

	
	/** Test the size of the list */
	@Test
	public void testSize()
	{
		assertEquals("Size: shortList is correct", 2, shortList.size);
		assertEquals("Size: emptyList is correct", 0, emptyList.size);
		assertEquals("Size: longerList is correct", LONG_LIST_LENGTH, longerList.size);
		assertEquals("Size: list1 is correct", 3, list1.size);
	}

	
	
	/** Test adding an element into the list at a specified index,
	 * specifically:
	 * public void add(int index, E element)
	 * */
	@Test
	public void testAddAtIndex()
	{
		try {
			emptyList.add(0, null);
			fail("Add null element");
		} catch (NullPointerException e) {
		}
		
		try {
			emptyList.add(1, 0);
			fail("Add element outbound");
		} catch (IndexOutOfBoundsException e) {
		}
		
		emptyList.add(0, 0);
		assertEquals("Add: check new added int 0", (Integer)0, emptyList.get(0));
		assertEquals("Add: check size", 1, emptyList.size());
		
		emptyList.add(0, 1);
		assertEquals("Add: check new added int 1", (Integer)1, emptyList.get(0));
		assertEquals("Add: check size", 2, emptyList.size());
		
		longerList.add(10, 999);
		assertEquals("Add: check new added int 999", (Integer)999, longerList.get(10));
		assertEquals("Add: check size", 11, longerList.size());
		
		longerList.add(0, -1);
		assertEquals("Add: check new added int -1", (Integer)(-1), longerList.get(0));
		assertEquals("Add: check size", 12, longerList.size());
	}
	
	/** Test setting an element in the list */
	@Test
	public void testSet()
	{
		try {
			shortList.set(0, null);
			fail("Set null element");
		} catch (NullPointerException e) {
		}
		
		try {
			shortList.set(-1, "Z");
			fail("Set element at negative index");
		} catch (IndexOutOfBoundsException e) {
		}
		try {
			shortList.set(2, "Z");
			fail("Set element outbound");
		} catch (IndexOutOfBoundsException e) {
		}
		
		assertEquals("Set: check element A is correct", "A", shortList.set(0, "C"));
		assertEquals("Set: check element C is correct", "C", shortList.get(0));
	}
	
}
