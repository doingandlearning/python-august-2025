import traceback

try:
    1/0
except ZeroDivisionError as e:
    print("This is a ZeroDivisionError")
    print(f"Error message: {e}")
    # traceback.print_exc()
    trace = traceback.format_exc()  # capture the trace!
    print(trace)