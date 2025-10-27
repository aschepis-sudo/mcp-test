import subprocess
import sys
import io
import contextlib

from mcp_test import __main__

def test_hello_world_output():
    # Capture the output of the main function
    with contextlib.redirect_stdout(io.StringIO()) as f:
        __main__.main()
    output = f.getvalue().strip()
    
    assert output == "Hello, World!", f"Expected 'Hello, World!', but got '{output}'"