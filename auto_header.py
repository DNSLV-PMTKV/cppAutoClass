import sys

c_argv = sys.argv[1]

param_count = 0
for num, arg in enumerate(sys.argv):
    if num % 2 == 0:
        param_count += 1

param_list = []
type_list = []
for num, arg in enumerate(sys.argv[1:]):
    if num % 2 != 0:
        type_list.append(arg)
    else:
        param_list.append(arg)

header = open('{}.h'.format(c_argv), 'w')
# first part
header.write("#ifndef _{}_H\n".format(c_argv.upper()))
header.write("#define _{}_H\n".format(c_argv.upper()))
header.write("\nclass {} \n{}\n".format(c_argv, "{"))


# public
header.write("public:\n")

# big5
header.write("\t{}();\n".format(c_argv))  # defualt constructor
header.write("\t{}(".format(c_argv))                        # constructor
for a in range(0, param_count - 1):                         #
    if a < param_count - 2:                                 # with
        header.write("{}, ".format(type_list[a]))           #
    else:                                                   # parameters
        header.write("{});\n".format(type_list[a]))         #
header.write("\t{}(const {} &);\n".format(c_argv, c_argv))  # copy
header.write("\t~{}();\n".format(c_argv))  # desctructor
header.write("\t{}&operator=(const {} &);\n\n". format(c_argv, c_argv))  # = overload

# set
for counter in range(0, param_count - 1):
    header.write("\tvoid set{}({});\n".format(param_list[counter + 1].upper(), type_list[counter]))

# get
for counter in range(0, param_count - 1):
    header.write("\n\t{} get{} const;".format(type_list[counter], param_list[counter + 1].upper()))


# private
header.write("\nprivate:")
for counter in range(0, param_count - 1):
    header.write("\n\t{} {};".format(type_list[counter], param_list[counter + 1]))

# last part
header.write("\n{};\n".format("}"))
header.write("#endif\n")

header.close()
