# Basis of a Test

# Tests would normally be in a different file and separate from the actual application.

# Example function

def correct_name(name):
    return name.title().strip()

# Test Setup
known_input = '     ryan      '
expected_out = 'Ryan'

# Test Execution
print("Testing function correct_name() with '     ryan     ' --> 'Ryan'")
# Print True if input matches output (test passed)
print(correct_name(known_input) == expected_out)
