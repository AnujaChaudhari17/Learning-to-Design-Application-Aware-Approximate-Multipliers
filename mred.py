from compute import *

def MRED(x):
    
    print("MRED: ", x)
    gencode = generate_code(x)
    
    #write the code in a python file
    with open("temp.py", "w") as file:
        file.write(gencode)
    print("Code written to temp.py")
    import importlib
    import temp
    importlib.reload(temp)
    from temp import multiply2

    # from temp import multiply2
    
    bit_width = 8

    # Generate all samples for the given bit width
    samples = [(a, b) for a in range(2**bit_width) for b in range(2**bit_width)]

    # Recalculate MRED using sampled inputs
    total_error = 0
    count = 0

    for a, b in samples:
        approx_result = multiply2(a, b)
        exact_result = a * b
        
        if exact_result != 0:  # Avoid division by zero
            total_error += abs(approx_result - exact_result) / exact_result
        count += 1

    MRED_sampled = total_error / count if count > 0 else 0
    print("MRED_sampled: ", MRED_sampled)

    return MRED_sampled