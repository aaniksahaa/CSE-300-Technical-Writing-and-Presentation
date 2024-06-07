leafnode_width = 1
leafnode_height_1 = 0.5
leafnode_height_2 = 1

def generate_leafnode():
    tikz_code = f"""
\\begin{{tikzpicture}}
    \\filldraw[color=red!80, fill=red!5, very thick, font=\\large] (0,0) rectangle ({leafnode_width},{leafnode_height_1}) node[midway] {{#1}};
    \\filldraw[color=blue!80, fill=blue!5, very thick, font=\\Huge] (0,0) rectangle ({leafnode_width},-{leafnode_height_2}) node[midway, text=black] {{#2}};
\\end{{tikzpicture}}
"""
    return tikz_code


# Example usage:
latex_output = generate_leafnode()
print(latex_output)
