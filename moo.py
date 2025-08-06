import numpy as np
# from mred import MRED
# from optimizationParams import optimizationParam

def multi_objective_function(x):
    """
    This function calculates four objectives: MRED, Latency, Area, and Power.
    The calculation is arbitrary for demonstration purposes. Replace these with your actual equations.
    """
    print(x, type(x))
    # Replace these with actual formulas for MRED, Latency, Area, and Power
    from mred import MRED
    from accuracy import train_and_evaluate
    from optimizationParams import optimizationParam
    error = MRED(x)  # Example: Sum of squares
    
    final_acc =  train_and_evaluate()/100  
    # Calculate Latency, Area, and Power using the optimizationPram function
    Latency, Power = optimizationParam(x)
    print(error, Latency, Power, final_acc)
    return error, Latency, Power, final_acc

# multi_objective_function([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
# 0.5748287746549505

# test_inputs = [
#     [12, 10, 9, 1, 4, 4, 1, 4, 10, 3, 13, 2, 19, 20, 19, 6, 21, 5, 5, 19],
#     [0, 5, 10, 15, 20, 1, 3, 6, 9, 12, 4, 8, 14, 7, 11, 13, 18, 2, 19, 21],
#     [21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2],
# ]

# for config in test_inputs:
#     error, latency, power, accuracy = multi_objective_function(config)
#     print(f"Config: {config}")
#     print(f"MRED: {error}, Latency: {latency}, Power: {power}, Accuracy: {accuracy}")
#     print("-" * 40)

# from mred import MRED
# from optimizationParams import optimizationParam
# from accuracy import train_and_evaluate
# test_inputs = [
#     [12, 10, 9, 1, 4, 4, 1, 4, 10, 3, 13, 2, 19, 20, 19, 6, 21, 5, 5, 19],
#     [0, 5, 10, 15, 20, 1, 3, 6, 9, 12, 4, 8, 14, 7, 11, 13, 18, 2, 19, 21],
#     [21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2],
# ]

# for config in test_inputs:
#     print(f"Testing config: {config}")
#     print(f"MRED: {MRED(config)}")
#     print(f"Accuracy: {train_and_evaluate()}")
#     print(f"Latency, Power: {optimizationParam(config)}")
#     print("-" * 40)