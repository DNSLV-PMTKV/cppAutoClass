import sys
import os

c_argv = sys.argv[1]

param_count = 0
for num, arg in enumerate(sys.argv):
    if num % 2 == 0:
        param_count += 1

param_list = []
type_list = []
for num, arg in enumerate(sys.argv[2:]):
    if num % 2 != 0:
        param_list.append(arg)
    else:
        type_list.append(arg)

newpath = os.path.join('.', c_argv)
if not os.path.exists(newpath):
    os.mkdir(newpath)

print(param_list)
print(type_list)


def auto_header():
    header = open('{}/{}.h'.format(newpath, c_argv), 'w')

    # first part
    header.write("#ifndef _{}_H\n".format(c_argv.upper()))
    header.write("#define _{}_H\n".format(c_argv.upper()))
    header.write("\nclass {} \n{}\n".format(c_argv, "{"))

    # public
    header.write("public:\n")

    # big5
    header.write("\t{}();\n".format(c_argv))                    # defualt constructor
    header.write("\t{}(".format(c_argv))                        # constructor
    for a in range(0, param_count - 1):                         #
        if a < param_count - 2:                                 # with
            header.write("{}, ".format(type_list[a]))           #
        else:                                                   # parameters
            header.write("{});\n".format(type_list[a]))         #
    header.write("\t{}(const {} &);\n".format(c_argv, c_argv))  # copy
    header.write("\t~{}();\n".format(c_argv))                   # desctructor
    header.write("\t{}&operator=(const {} &);\n\n". format(c_argv, c_argv))  # = overload

    # set
    for counter in range(0, param_count - 1):
        header.write("\tvoid set{}({});\n".format(param_list[counter].upper(), type_list[counter]))

    # get
    for counter in range(0, param_count - 1):
        header.write("\n\t{} get{}() const;".format(type_list[counter], param_list[counter].upper()))

    # private
    header.write("\nprivate:")
    for counter in range(0, param_count - 1):
        header.write("\n\t{} {};".format(type_list[counter], param_list[counter]))

    # last part
    header.write("\n{};\n".format("}"))
    header.write("#endif\n")

    header.close()


def auto_cpp():
    cpp = open('{}/{}.cpp'.format(newpath, c_argv), 'w')

    cpp.write('#include "{}.h"\n'.format(c_argv))
    cpp.write('#include <iostream>\n\n')

    # big5
    cpp.write('{}::{}(): '.format(c_argv, c_argv))
    for counter in range(1, param_count - 1):
        if counter < param_count - 2:
            cpp.write('{}(),'.format(param_list[counter]))
        else:
            cpp.write('{}() {}{}\n'.format(param_list[counter], "{", "}"))

    cpp.write('{}::{}('.format(c_argv, c_argv))
    for counter in range(0, param_count - 1):
        if counter < param_count - 2:
            cpp.write('{} {},'.format(type_list[counter], param_list[counter]))
        else:
            cpp.write('{} {}) \n{}\n\n{}\n'.format(type_list[counter], param_list[counter], "{", "}"))

    cpp.write("{}::{}(const {} &rhs) \n{}\n\n{}\n".format(c_argv, c_argv, c_argv, "{", "}"))
    cpp.write("{}::~{}() \n{}\n\n{}\n".format(c_argv, c_argv, "{", "}"))
    cpp.write("{}&{}::operator=(const {} &rhs)\n{}\n\n{}\n".format(c_argv, c_argv, c_argv, "{", "}"))

    # set
    for counter in range(0, param_count - 1):
        cpp.write("void {}::set{}({} A)\n{}\n\n{}\n".format(c_argv, param_list[counter].upper(), type_list[counter], "{", "}"))

    # get
    for counter in range(0, param_count - 1):
        cpp.write("{} {}::get{}() const\n{}\n\n{}\n".format(type_list[counter], c_argv, param_list[counter].upper(), "{", "}"))

    cpp.close()


if __name__ == '__main__':
    print("Creating files..")
    auto_header()
    auto_cpp()
    print("Done.")
