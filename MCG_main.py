#testing python diagram generation
import matplotlib.pyplot as plt
from random import randint
import math

################################################################################
#                                                                              #
#   This python program generates 6 plots or diagrams using matplotlib from    #
#   a txt file, generating random data using the randint function or           #
#   generating data following a mathematical equation.                         #
#                                                                              #
#   The code uses the matplotlib library to create a scatter, plot, histogram  #
#   fill between, and two pie charts.                                          #
#                                                                              #
#   For using the txt mode, file must have the following format:               #
#   option 1:                                                                  #
#   Auto                                                                       #
#   x_quantity (max 9999)                                                      #
#   first x                                                                    #
#                                                                              #
#   yyyyyyy                                                                    #
#   ...                                                                        #
#   option 2:                                                                  #
#   x y                                                                        #
#   x_quantity (max 9999)                                                      #
#   xxxxxxx yyyyyyy                                                            #
#   ...                                                                        #
#                                                                              #
#   Recommendaion: check what data is being used to generate the diagrams      #
#   you are going to use.                                                      #
################################################################################

#generate random values
def random_n(n):
    lst = list()
    for i in range(n):
        a = randint(0, 1000)
        lst.append(a)
    return lst

#pick values from '.txt' file
def picking_values_txt(file_path):
    lst_x = list()
    lst_y = list()
    with open(file_path, 'r') as file:
        line_1 = file.readline()
        if line_1[0] == 'x':
            line_2 = file.readline()
            for i in range(int(line_2)):
                line = file.readline()
                n1=''
                n2=''
                for i in range(7):
                    n1 += line[i]
                    n2 += line[i+8]
                lst_x.append(int(n1))
                lst_y.append(int(n2))
                
        elif line_1[0] == 'A':
            line_2 = file.readline()
            line_3 = file.readline()
            for i in range(int(line_3), (int(line_3)+int(line_2))):
                lst_x.append(i)
            emp_line = file.readline()
            for i in range(int(line_2)):
                line = file.readline()
                lst_y.append(int(line))

    file.close()
    return lst_x, lst_y

#generating data following a mathematical equation
def math(n, fst_n):
    lst = list()
    for i in range(fst_n, fst_n+n):
        y = pow(i, 3)        #you might need to change this function, being i = x
        lst.append(y)
    return lst

#main program
data_source = input("Data source [random(0), txt(1), math(2)]: ")

x = list()
y = list()
if data_source == '0' or data_source == 'random':
    n = int(input("Quantity of x values: "))
    for i in range(n):
        x.append(i)
    y = random_n(n)
elif data_source == '1' or data_source == 'txt' or data_source == 'txt file':
    file_name = input("File name or path: ")
    file_path = ''
    if file_name[0]=='/' and  file_name[1]=='U' and file_name[2]=='s' and file_name[3]=='e' and file_name[4]=='r' and file_name[5]=='s':
        file_path = file_name
    else:
        file_path = '/Users/j.alcaide/Documents/MCG/' + file_name + '.txt'
    print("Final path to file:", file_path)
    x, y = picking_values_txt(file_path)
    print("x =",x)
    print("y =",y)
elif data_source == '2' or data_source == "math":
    n = int(input("Quantity of x values: "))
    fst_n = int(input("First x value: "))
    for i in range(fst_n, fst_n+n):
        x.append(i)
    y = math(n, fst_n)
else:
    print('Input problem')

fig_1, axs = plt.subplots(3, 2, figsize=(12,8))
axs[0,0].scatter(x,y)
axs[0,1].hist(y)
axs[1,0].plot(x,y)
axs[1,1].fill_between(x,y)
axs[2,0].pie(x)
axs[2,1].pie(y)

plt.savefig("/Users/j.alcaide/Documents/MCG/pyplots.png")
plt.show()
