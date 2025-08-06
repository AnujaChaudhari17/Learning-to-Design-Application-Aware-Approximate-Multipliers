import yaml

def compute_latencies(params, x):
    """
    Compute latencies for columns 5 to 13 based on compressor indices in x.

    The mapping of compressors per column is as follows:
      - Column 5: 2 compressors
      - Column 6: 2 compressors
      - Columns 7-10: 3 compressors each (with special handling:
                   take max(latency_1, latency_2) + latency_3)
      - Column 11: 2 compressors
      - Columns 12-13: 1 compressor each

    Parameters:
        params (dict): Dictionary that must include a key 'compressors', which is
                       a list of compressor dictionaries. Each compressor dictionary
                       must have a 'latency' key.
        x (list): List of indices used to select compressors from params['compressors'].
                  The list should contain exactly 20 indices (2 + 2 + 4*3 + 2 + 2*1 = 20).

    Returns:
        dict: A dictionary mapping column numbers (5 through 13) to the computed latency.
    """
    # Define the number of compressors for each column (columns 5 to 13)
    # Columns:    5, 6, 7, 8, 9, 10, 11, 12, 13
    comp_counts = [2, 2, 3, 3, 3, 3, 2, 1, 1]

    # Dictionary to store computed latencies.
    latencies = {}

    # Pointer to the current position in list x.
    x_index = 0

    # Iterate over the columns and their respective compressor counts.
    for col, count in zip(range(5, 14), comp_counts):
        if count == 3:
            # For three compressors: latency = max(first, second) + third.
            lat1 = params['compressors'][x[x_index]]['latency']
            x_index += 1
            lat2 = params['compressors'][x[x_index]]['latency']
            x_index += 1
            lat3 = params['compressors'][x[x_index]]['latency']
            x_index += 1
            latency = max(lat1, lat2) + lat3
        else:
            # For columns with count != 3, sum all compressor latencies.
            latency = 0
            for _ in range(count):
                latency += params['compressors'][x[x_index]]['latency']
                x_index += 1

        latencies[col] = latency

    return latencies

def optimizationParam(x):
    """
    This function calculates the Latency, Area, and Power using the params values in parameter.yaml
    for the compressors corresponding to the indices in x.
    
    :param x: List of indices corresponding to the compressors
    :return: Dictionary with total latency, power, and area
    """
    # Load parameters from parameters.yaml
    with open("parameters.yaml", "r") as file:
        params = yaml.safe_load(file)
    
    # Initialize totals
    total_latency = compute_latencies(params, x)
    total_power = 0
    
    
    # Iterate through the indices in x
    for index in x:
        if 0 <= index < len(params['compressors']):
            compressor = params['compressors'][index]
            total_power += compressor['power']
        else:
            raise ValueError(f"Index {index} is out of range for compressor_variants.")
    
    # Return the calculated totals
    return max(total_latency.values()),total_power