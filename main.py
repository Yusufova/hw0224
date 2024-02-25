# lst = [1, 2, 3, 4, 5, 6]
# x = map(lambda x : x - 2, lst)
# print(list(x))
# def map(func, lst):
#     lst2 = []
#     for item in lst:
#         lst2.append(func(item))
#
#     return lst2

# lst = [1, 2, 3, 4, 5, 6]
# y = filter(lambda x : x % 2 == 0, lst)
# print(list(y))

def percentage(nums):
    for percent in nums:
        return percent / 100
nums = [1, 2, 3]
decimal = percentage(nums)
print(decimal)

