import sys
import os

print("Creating file..")

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

newpath = r"{}\ ".format(c_argv)
if not os.path.exists(newpath):
    os.makedirs(newpath)

cpp = open('{}/{}.cpp'.format(c_argv, c_argv), 'w')

cpp.write('#include "{}.h"\n'.format(c_argv))
cpp.write('#include <iostream>\n\n')

# big5
cpp.write('{}::{}(): '.format(c_argv, c_argv))
for counter in range(1, param_count):
    if counter < param_count - 1:
        cpp.write('{}(),'.format(param_list[counter]))
    else:
        cpp.write('{}() {}{}\n'.format(param_list[counter], "{", "}"))

cpp.write('{}::{}('.format(c_argv, c_argv))
for counter in range(0, param_count - 1):
    if counter < param_count - 2:
        cpp.write('{} {},'.format(type_list[counter], param_list[counter + 1]))
    else:
        cpp.write('{} {}) \n{}\n\n{}\n'.format(type_list[counter], param_list[counter + 1], "{", "}"))

cpp.write("{}::{}(const {} &rhs) \n{}\n\n{}\n".format(c_argv, c_argv, c_argv, "{", "}"))
cpp.write("{}::~{}() \n{}\n\n{}\n".format(c_argv, c_argv, "{", "}"))
cpp.write("{}&{}::operator=(const {} &rhs)\n{}\n\n{}\n".format(c_argv, c_argv, c_argv, "{", "}"))

# set
for counter in range(0, param_count - 1):
    cpp.write("void {}::set{}({} A)\n{}\n\n{}\n".format(c_argv, param_list[counter + 1].upper(), type_list[counter], "{", "}"))

# get
for counter in range(0, param_count - 1):
    cpp.write("{} {}::get{}() const\n{}\n\n{}\n".format(type_list[counter], c_argv, param_list[counter + 1].upper(), "{", "}"))

cpp.close()

print("File created.")
