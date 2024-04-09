from textnode import TextNode

def main():
    textnode = TextNode("This is a textnode", "italic", "https://facebook.com")
    print(textnode.__repr__())
main()