class Array(object):
    """ Array class """

    def __init__(self, size, array_string):
        self.nums = list(map(int, array_string.split()))
        if size != len(self.nums):
            raise Exception('array size is not matched.')
        self.psum = [sum(self.nums[:i+1]) for i in range(size)]

    def naiveSum(self):
        """ Return the sum of the array. """
        return sum(self.nums)

    def partSum(self, left, right):
        """ Return part sum of the range [left, right]. """
        if left == 0:
            return self.psum[right]
        return self.psum[right] - self.psum[left-1]

