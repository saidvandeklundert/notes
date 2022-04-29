class Solution:
    def defangIPaddr(self, address: str) -> str:
        return_value = address.replace(".", "[.]")
        return return_value


if __name__ == "__main__":
    alist = ["1.1.1.1", "255.100.50.0"]
    for ip in alist:
        print(Solution().defangIPaddr(ip))
