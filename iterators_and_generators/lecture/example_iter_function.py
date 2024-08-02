# my_list = [4, 7, 0, 3]
# # get an iterator using iter()
#
# my_iter = iter(my_list)
# print(next(my_iter))
# print(next(my_iter))
# print(my_iter.__next__())
# print(my_iter.__next__())
# next(my_iter)


#2
# my_list = [4, 7, 0, 3]

# iter_my_list = iter(my_list)
#
# # while True:
# #     try:
# #         print(next(iter_my_list))
# #     except StopIteration:
# #         break

# for el in my_list:
#     print(el)


#3
my_list = [4, 7, 0, 3, 5, 8]
filter_my_list = filter(lambda x: x % 2 == 1, my_list)
print(filter_my_list)

for el in filter_my_list:
    print(el)


#4
# my_list = [4, 7, 0, 3, 5, 8]
# filter_my_list = list(filter(lambda x: x % 2 == 1, my_list))
# print(filter_my_list)
#
# for el in filter_my_list:
#     print(el)