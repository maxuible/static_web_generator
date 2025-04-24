from textnode import TextNode
from textnode import TextType

import shutil

def main():
    node = TextNode("this is some anchor text", TextType.NORMAL, "https://boot.dev")

    print(node)
    shutil.rmtree()


main()