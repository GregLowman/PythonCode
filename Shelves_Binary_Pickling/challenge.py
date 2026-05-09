"""Append multiplication tables (2–12) to sample.txt, right-justified."""
with open("sample.txt", 'a') as new_sample:
    for i in range(2,13):
        for j in range(1, 13):
            print("{1:>2} times {0} is {2}".format(i, j, i * j), file=new_sample)
        print("-" * 20, file=new_sample)
