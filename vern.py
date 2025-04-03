print("Starting vern.py...")

from ai_engine import get_math_expression
from run_expression import execute_expression

def main():
    print("\n Vern v.09 - Natural Language Math CLI")
    print ("Type 'exit' to quit.\n")

    while True:
        instruction = input("Vern> ")
        if instruction.lower() in ["exit", "quit"]:
            break

        expression = get_math_expression(instruction)
        print(f"Expression: {expression}")
        result = execute_expression(expression)
        print(f"Result: {result}\n")

if __name__ == "__main__":
    main()
