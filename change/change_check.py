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
    
    def _dict_diff(self, test_pre_d, test_post_d):
        """Diff a dict"""
        diff_d = {}
        all_keys_set = test_pre_d.keys() | test_post_d.keys()
        
        # record change in keys: 
        for key in all_keys_set:
            if test_pre_d.get(key) != test_post_d.get(key):
                diff_d[key] = [ test_pre_d.get(key), test_post_d.get(key)]
        

        return diff_d

    def ez_test(self,):
        """Execute the ex check"""
        test_pre_d, test_post_d = self._load_test(test_name='bgp')
        diff = self._dict_diff(test_pre_d, test_post_d)
        bgp_result = {}

        if len(diff.keys()) == 0:
            print('BGP PASSED')
            bgp_result['result'] = 'PASSED'
        else:
            print('BGP FAILED')
            bgp_result['result'] = 'FAILED'
            for peer, state in diff.items():
                print(f"{peer} changed from {state[0]} to {state[1]}")
                bgp_result[peer] = f"{peer} changed from {state[0]} to {state[1]}"
                

        return bgp_result



    
if __name__ == "__main__":
    # debug purposes
    x = NodeTester(hostname = 'router1', path ='C:\\dev-container\\python\\change')
    x.ez_test()
    d1, d2 = x.ez_test()
    x._dict_diff(d1, d2)
