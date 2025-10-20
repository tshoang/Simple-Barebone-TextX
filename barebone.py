from textx import metamodel_from_file
import argparse

barebone_meta = metamodel_from_file('barebone.tx')


def parse_arguments():
    parser = argparse.ArgumentParser(description ='Barebone interpreter')
    parser.add_argument('filename', 
                    help ='Name of the Barebone file')

    args = parser.parse_args()
    return args.filename

def clear(name, heap):
    heap[name] = 0
    return heap

def incr(name, heap):
    value = heap.get(name, 0)
    heap[name] = value + 1
    return heap

def decr(name, heap):
    value = heap.get(name, 0)
    heap[name] = value - 1
    return heap

def loop(name, statements, heap):
    while heap[name] != 0:
        for statement in statements:
            heap = execute(heap, statement)
            print(heap)
    return heap

def execute(heap, statement):
    statement_type = type(statement).__name__
    if statement_type == "Clear":
        return clear(statement.name, heap)
    if statement_type == "Increment":
        return incr(statement.name, heap)
    if statement_type == "Decrement":
        return decr(statement.name, heap)
    if statement_type == "While":
        return loop(statement.name, statement.statements, heap)

    
if __name__ == "__main__":
    barebone_file = parse_arguments()

    barebone_model = barebone_meta.model_from_file(barebone_file)

    heap = {}
    for statement in barebone_model.statements:
        heap = execute(heap, statement)
        print(heap)
    
