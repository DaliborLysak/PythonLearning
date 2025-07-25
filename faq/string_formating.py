# insert variable i into the string
i = 9.999
j = 999.999

# f string formatting examples
print(f"The value of i is: {i:.1f} value of j is {j:.3f}")
print(f"The value of i + j is: {i + j:.3f}")

# format() method examples
print("The value of i is: {:.1f} value of j is {:.3f}".format(i, j))
print("The value of j is: {1:.3f} value of i is {0:.1f}".format(i, j))
print("The value of i + j is: {0:.3f}".format(i + j))

# old-style formatting examples
print("The value of i is: %.1f value of j is %.3f" % (i, j))
print("The value of i + j is: %.3f" % (i + j))


