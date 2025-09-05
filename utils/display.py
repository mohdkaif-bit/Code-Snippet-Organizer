from pygments import highlight
from pygments.lexers import get_lexer_by_name, TextLexer
from pygments.formatters import TerminalFormatter

def display_snippet(snippet):
    print(f"Title: {snippet['title']}")
    print(f"Description: {snippet['description']}")
    print(f"Language: {snippet['language']}")
    print(f"Category: {snippet['category']}")
    print(f"Tags: {', '.join(snippet['tags']) if snippet['tags'] else 'None'}")
    try:
        lexer = get_lexer_by_name(snippet['language'].lower())
    except:
        from pygments.lexers import TextLexer
        lexer = TextLexer()
    colored_code = highlight(snippet['code'], lexer, TerminalFormatter())
    print(colored_code)
    print("-" * 50)
