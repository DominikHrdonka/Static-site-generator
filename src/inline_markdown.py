from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image
)
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(pattern, text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(pattern, text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_image(old_nodes):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    ### withouth capturing
    pattern_split = r"!\[.*?\]\(.*?\)"
    new_nodes = []
    for old_node in old_nodes:
        if extract_markdown_images(pattern, old_node.text) is False:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        
        image_tuples = extract_markdown_images(pattern, old_node.text)
        text_sections = re.split(pattern_split, old_node.text)
        
        for text_section in text_sections:
            if text_section == "":
                continue
            split_nodes.append(TextNode(text_section, text_type_text))
            
        for tuple in image_tuples:
            split_nodes.append(TextNode(tuple[0], text_type_image, tuple[1]))

        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_links(old_nodes):
    pass