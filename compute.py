from helper import base_code 
import string

# Define the compressor functions
compressor_variants = [
    "ahmad", "akbari", "meo", "venka", "yang", "momeni",
    "AC6G1", "AC6G2", "AC6G3", "AC6G4", "AC6G5", "AC6G6",
    "AC6G7", "AC6G8", "AC6G9", "AC6G10", "AC6G11", "AC6G12",
    "ACFGI1", "ACFGII1", "ACFGII10", "app_compressor"
]

index_to_letter = string.ascii_lowercase

def generate_code(vector):
    """
    Replaces the compressor calls in column 8 based on the input vector.

    Args:
        vector (list): A list of size 3 indicating which compressor to use for each position.
    Returns:
        str: Modified Python code.
    """
    if len(vector) != 20:
        raise ValueError("Input vector must be of size 3.")
    
    modified_code = base_code
    
    # Replace each COMPRESSOR placeholder with a variant from the combination
    for idx, compressor_idx in enumerate(vector):
        compressor_name = compressor_variants[compressor_idx]
        placeholder = f"COMPRESSOR{index_to_letter[idx]}"
        # print(f"Replacing {placeholder} with {compressor_name}")
        modified_code = modified_code.replace(placeholder, compressor_name)
    
    
    return modified_code


# vector = [0, 12, 2, 3, 4, 5, 6, 7, 8, 9, 20, 11, 12, 13, 14, 15, 16, 17, 18, 21]
# code = generate_code(vector)
# print(code)

