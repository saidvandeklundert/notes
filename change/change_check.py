from json import load

class NodeTester:

    def __init__(self, hostname,):
        self.hostname = hostname
        
    
    @classmethod
    def example(cls):
        # TODO: implement method to collect tests from a location
        return 'yolo'
    
    def load_test(self,):
        with open(f"{self.hostname}_pre_bgp_v4_data.json", "r") as f:
            bgp_v4_pre_d = load(f)
        with open(f"{self.hostname}_post_bgp_v4_data.json", "r") as f:
            bgp_v4_post_d = load(f)
        return bgp_v4_pre_d, bgp_v4_post_d
        

    
if __name__ == "__main__":
    # debug purposes
    x = NodeTester('router1')