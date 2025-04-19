import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_repr_01(self):
        dict = {
                    "href": "https://www.google.com",
                    "target": "_blank",
                }
        node = HTMLNode(props=dict)
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"')

    def test_init_01(self):
        node1 = HTMLNode()
        self.assertIsNone(node1.tag)
        self.assertIsNone(node1.value)
        self.assertIsNone(node1.children)
        self.assertIsNone(node1.props)

    def test_init_02(self):
        node1 = HTMLNode("tag1", "value2", "children3", "props4")
        self.assertEqual(node1.tag, "tag1")
        self.assertEqual(node1.value, "value2")
        self.assertEqual(node1.children, "children3")
        self.assertEqual(node1.props, "props4")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")


    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_grandchildren_01(self):
        grandchild_node = LeafNode("b", "grandchild", {"href": "https://www.google.com"})
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b href=\"https://www.google.com\">grandchild</b></span></div>",
        )

    def test_to_html_with_grandchildren_01(self):
        grandchild_node = LeafNode("b", "grandchild", {"href": "https://www.google.com"})
        child_node = ParentNode("span", [grandchild_node], {"property1" : "value"})
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span property1=\"value\"><b href=\"https://www.google.com\">grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()