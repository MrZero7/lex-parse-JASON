import graphviz
# import parse_final

# input_code = '''
# begin
# declare int x;
# while (x=1) do read y; endwhile
# write y;
# end
# '''

# for token in parse_final.new_lex:
#     print(parse_final.input_code)

def draw_parse_tree():
    dot = graphviz.Digraph()
    
    # Add nodes
    dot.node('S', 'S')
    dot.node('NP', 'NP')
    dot.node('VP', 'VP')
    dot.node('Noun', 'Noun')
    dot.node('Verb', 'Verb')
    dot.node('Article', 'Article')

    # Add edges
    dot.edge('S', 'NP')
    dot.edge('S', 'VP')
    dot.edge('NP', 'Article')
    dot.edge('NP', 'Noun')
    dot.edge('VP', 'Verb')

    # Render and save the parse tree
    dot.format = 'png'
    dot.render('parse_tree', view=True)

# Call the function to draw the parse tree
draw_parse_tree()


#TODO: must do stuff here





# # Importing the libraries
# import nltk
# from nltk.tree import Tree
# from nltk.draw.util import CanvasFrame
# from nltk.draw import TreeWidget

# # Defining the grammar
# grammar = nltk.CFG.fromstring("""
# S -> NP VP
# NP -> DT NN | DT NN PP | PRP
# VP -> VBD NP | VBD NP PP
# PP -> IN NP
# DT -> 'the' | 'a'
# NN -> 'cat' | 'dog' | 'park' | 'ball'
# VBD -> 'chased' | 'saw'
# IN -> 'in' | 'with'
# PRP -> 'he' | 'she'
# """)

# # Parsing the sentence
# sentence = "the cat chased the dog in the park"
# tokens = sentence.split()
# parser = nltk.ChartParser(grammar)
# trees = list(parser.parse(tokens))

# # Drawing the first parse tree
# tree = trees[0]
# cf = CanvasFrame()
# tc = TreeWidget(cf.canvas(), tree)
# tc['node_font'] = ('arial', 10, 'bold')
# tc['leaf_font'] = ('arial', 10, 'italic')
# tc['node_color'] = '#005990'
# tc['leaf_color'] = '#3F8F57'
# tc['line_color'] = '#175252'
# cf.add_widget(tc, 10, 10)
# cf.print_to_file('parse_tree.png')
# cf.destroy()
