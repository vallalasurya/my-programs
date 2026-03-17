def string_test(s):
    d={"upper_case":0, "lower_case":0}
    for i in s:
        if i.isupper():
            d["upper_case"]+=1
        elif i.islower():
            d["lower_case"]+=1
        else:
            pass
    print("uppper case letters:", d["upper_case"])
    print("lower case letters:", d["lower_case"])
string_test("The term Internet of Things(IoT) has emerged over the past few years as one of the popular “technology buzz” terms. In today's technological world, IoT figures prominently in technology discussions due to its rapid growth. There are multiple ways to define IoT.") 



