from json import load

class NodeTester:

    def __init__(self, hostname, path):
        self.hostname = hostname
        self.path = path
        
    
    @classmethod
    def example(cls):
        # TODO: implement method to collect tests from a location
        return 'yolo'
    
    def _load_test(self, test_name):
        """Load the pre- and post-change data for a test"""
        with open(f"{self.path}\\{self.hostname}_pre_{test_name}_data.json", "r") as f:
            test_pre_d = load(f)
        with open(f"{self.path}\\{self.hostname}_post_{test_name}_data.json", "r") as f:
            test_post_d = load(f)
        return test_pre_d, test_post_d
    
    def _dict_diff(test_pre_d, test_post_d):
        """Diff a dict toplevel"""
        all_keys = test_pre_d.items() | test_post_d.()
        return all_keys

    def bgp_v4_test(self,):
        """Execute the bgp_v4_test check"""
        test_pre_d, test_post_d = self._load_test(test_name='bgp_v4')
        print(test_pre_d.keys())
        print(test_post_d.keys())
        return test_pre_d, test_post_d



    
if __name__ == "__main__":
    # debug purposes
    x = NodeTester(hostname = 'router1', path ='C:\\dev-container\\python\\change')
    x.bgp_v4_test()
    d1, d2 = x.bgp_v4_test()
