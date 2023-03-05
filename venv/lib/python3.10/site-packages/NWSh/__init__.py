import sys

if not sys.stdin.isatty():
    print("Error: The console is not a TTY.", file=sys.stderr)
    sys.stderr.flush()
    sys.exit(1)
