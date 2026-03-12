class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        list_people = [0] * num_people
        index = 1

        while candies > 0: 
            if candies > index:
                list_people[(index - 1) % num_people] += index
            else:
                list_people[(index - 1) % num_people] += candies

            candies -= index
            index += 1

        return(list_people)