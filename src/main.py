from textnode import TextNode, TextType

def main():
    text_node = TextNode("text", TextType.TEXT, "boot.dev")
    print(text_node)

if __name__ == "__main__":
    main()