print("\N{ESC}[31mtest\u001b[0ming")

print("\N{ESC}[1mbold\u001b[0m not bold")


class Colors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    NORMALIZE = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


print(f"{Colors.OKGREEN}in {Colors.BOLD}green{Colors.NORMALIZE}, normal")

print(f"{Colors.OKCYAN}OKCYAN {Colors.NORMALIZE}")

print(f"{Colors.OKBLUE}OKCYAN {Colors.NORMALIZE}")

print(f"{Colors.HEADER}HEADER {Colors.NORMALIZE}")
