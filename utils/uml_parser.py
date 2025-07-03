import re

def parse_cpp_file(filepath):
    """
    Parses a C++ file to find:
    - Class names
    - Inheritance relationships (supports multiple base classes)

    Handles:
    - Single-line or simple multi-line class declarations.
    - Multiple inheritance: class C : public A, protected B

    Limitations:
    - Doesn't handle advanced macros, templates, or preprocessor conditions.
    """

    classes = []
    relations = []

    with open(filepath, "r") as file:
        content = file.read()

        # Remove newlines inside class declaration line
        content = re.sub(r'\s*\n\s*', ' ', content)

        # Regex: class ClassName [: access Base1, access Base2 ] {
        pattern = r'class\s+(\w+)\s*(?:\:\s*([^{]+))?\s*\{'
        matches = re.findall(pattern, content)

        for cls_name, bases in matches:
            classes.append(cls_name.strip())

            if bases:
                # bases = 'public A, protected B'
                base_classes = re.findall(r'(?:public|protected|private)?\s*(\w+)', bases)
                for base in base_classes:
                    relations.append((base.strip(), cls_name.strip()))

    return {
        "classes": list(set(classes)),
        "relations": relations
    }
