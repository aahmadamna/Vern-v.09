def execute_expression(expr):
    try:
        return eval(expr)
    except Exception as e:
        return f"Error: {str(e)}"