def mask(value, size):
    masks = {"byte": 0xFF, "word": 0xFFFF, "dword": 0xFFFFFFFF, "qword": 0xFFFFFFFFFFFFFFFF}
    return value & masks[size]

def format_result(value, size):
    masked = mask(value, size)
    return {
        "decimal": str(masked),
        "binary": format(masked, '0{}b'.format(size_bits(size)))
    }

def size_bits(size):
    return {"byte": 8, "word": 16, "dword": 32, "qword": 64}[size]

def perform_operation(num1, num2, op, size):
    if op == "AND":
        res = num1 & num2
    elif op == "OR":
        res = num1 | num2
    elif op == "XOR":
        res = num1 ^ num2
    elif op == "NOT":
        res = ~num1
    elif op == "SHL":
        res = num1 << 1
    elif op == "SHR":
        res = num1 >> 1
    else:
        raise ValueError("Operación no válida")

    return format_result(res, size)
