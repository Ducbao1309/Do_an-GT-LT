from collections import OrderedDict

class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        number_of_people = len(names)
        height_to_name_map = OrderedDict()

        for height, name in zip(heights, names):
            height_to_name_map[height] = name

        height_to_name_map = OrderedDict(
            sorted(height_to_name_map.items(), reverse=True)
        )
        sorted_names = list(height_to_name_map.values())

        return sorted_names
