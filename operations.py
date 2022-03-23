"""Basic math operations."""

def add(a, b):
    """Add a and b."""

    return a + b


def sub(a, b):
    """Subtract b from a."""

    return a - b


def mult(a, b):
    """Multiply a and b."""

    return a * b


def div(a, b):
    """Divide a by b."""

    return a / b

OPERATIONS = {
    "add" : add,
    "subtract" : sub,
    "multiply" :mult,
    "divide": div
}
