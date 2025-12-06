import unittest
import contact_manager
import io
import sys

class TestContactManager(unittest.TestCase):

    def setUp(self):
        # Clear the contacts list before each test
        contact_manager.contacts = []

    def test_add_contact(self):
        contact_manager.add_contact("Alice", "12345")
        self.assertEqual(len(contact_manager.contacts), 1)
        self.assertEqual(contact_manager.contacts[0]["name"], "Alice")
        self.assertEqual(contact_manager.contacts[0]["phone"], "12345")

    def test_delete_contact(self):
        contact_manager.add_contact("Bob", "67890")
        contact_manager.delete_contact("Bob")
        self.assertEqual(len(contact_manager.contacts), 0)

    def test_delete_non_existent_contact(self):
        contact_manager.add_contact("Charlie", "11111")
        contact_manager.delete_contact("David") # Should not delete anything
        self.assertEqual(len(contact_manager.contacts), 1)

    def test_search_contact_found(self):
        contact_manager.add_contact("Eve", "22222")
        # Capture stdout to verify print output
        captured_output = io.StringIO()
        sys.stdout = captured_output
        contact_manager.search_contact("Eve")
        sys.stdout = sys.__stdout__
        self.assertIn("Found: Name: Eve, Phone: 22222", captured_output.getvalue())

    def test_search_contact_not_found(self):
        # Capture stdout to verify print output
        captured_output = io.StringIO()
        sys.stdout = captured_output
        contact_manager.search_contact("Frank")
        sys.stdout = sys.__stdout__
        self.assertIn("Contact 'Frank' not found.", captured_output.getvalue())

    def test_sorting(self):
        contact_manager.add_contact("Zack", "999")
        contact_manager.add_contact("Adam", "111")
        
        self.assertEqual(len(contact_manager.contacts), 2)
        
        # To truly test the view_contacts sorting logic which prints, we'd capture stdout again.
        captured_output = io.StringIO()
        sys.stdout = captured_output
        contact_manager.view_contacts()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        # Adam should appear before Zack in the output
        adam_index = output.find("Name: Adam")
        zack_index = output.find("Name: Zack")
        self.assertNotEqual(adam_index, -1)
        self.assertNotEqual(zack_index, -1)
        self.assertLess(adam_index, zack_index)

if __name__ == '__main__':
    unittest.main()
