class Solution:
    def countPoints(self, rings: str) -> int:
        rods_d = {}
        count = len(rings) - 1
        while count >= 0:
            nr = rings[count]
            color = rings[count - 1]

            if rods_d.get(nr) is None:
                rods_d[nr] = [color]
            else:
                rods_d[nr].append(color)
            count = count - 2

        rod_count = 0
        rgb_list = ["R", "G", "B"]
        rgb_list.sort()
        for rings in rods_d.values():
            value = list(set(rings))
            value.sort()
            print("value:", value, "rgb_list", rgb_list)
            if value == rgb_list:
                rod_count += 1
        return rod_count


class Solution:
    def countPoints(self, rings: str) -> int:
        rods_d = {}
        count = len(rings) - 1
        while count >= 0:
            nr = rings[count]
            color = rings[count - 1]

            if rods_d.get(nr) is None:
                rods_d[nr] = [color]
            else:
                rods_d[nr].append(color)
            count = count - 2

        rod_count = 0
        rgb_set = {"R", "G", "B"}

        for rings in rods_d.values():
            value = set(rings)

            if value == rgb_set:
                rod_count += 1
        return rod_count


alist = ["B0B6G0R6R0R6G9", "B0R0G0R9R0B0G0", "G4"]

for x in alist:
    print(Solution().countPoints(x))
