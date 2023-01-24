import tkinter as tk
import math
from tkinter import messagebox

def ip_calculator():
    
    ipaddress_calculate = ipaddress_input.get()
    subnet_calculate = int(subnet_input.get())

    #This is for calculating the class of IP address
    if int(ipaddress_calculate.split(".")[0]) < 128:
        IPclass = "A"

    elif int(ipaddress_calculate.split(".")[0]) < 192:
        IPclass = "B"

    elif int(ipaddress_calculate.split(".")[0]) < 224:
        IPclass = "C"

    elif int(ipaddress_calculate.split(".")[0]) < 240:
        IPclass = "D"

    else:
        IPclass = "E"
    
    #This is for calculating the default subnet mask for the class
    if IPclass == "A":
        default_subnet_output = "255.0.0.0"

    elif IPclass == "B":
        default_subnet_output = "255.255.0.0"

    elif IPclass == "C":
        default_subnet_output = "255.255.255.0"

    #This is for calculating the number of bits needed for the subnet
    bits = int(math.ceil(math.log(subnet_calculate, 2)))

    #This is for calculating the custom subnet mask
    custom_subnet_output = ""
    for i in range(4):
        if i < 3:
            custom_subnet_output += ipaddress_calculate.split(".")[i] + "."

        else:
            custom_subnet_output = "255.255.255." + str(256-(2**(8-bits)))

    #This is for calculating the number of networks
    number_networks_output = (2**(bits) - 2)

    #This is for calculating the number of hosts
    number_hosts_output = (2**(8-bits)) - 2

    #This is for displaying the results in IP calculator
    ip_class_label.config(text="IP Class: " + IPclass)
    default_subnet_label.config(text="Default Subnet Mask: " + default_subnet_output)
    bits_label.config(text="Number of Bits: " + str(bits))
    custom_subnet_label.config(text="Custom Subnet Mask: " + custom_subnet_output)
    networks_label.config(text="Number of Networks: " + str(number_networks_output))
    hosts_label.config(text="Number of Hosts: " + str(number_hosts_output))


main = tk.Tk()
heads = tk.Label(main, text='IP Calculator', font=('Comic Sans MS', 15, 'bold'), bg="skyblue")
heads.grid(row=0, column=0, columnspan=2, padx=0, pady=20)


#label for the IP address input field
ip_label = tk.Label(main, font=('Times', 11, 'bold'), text="IP Address:", bg="skyblue")
ip_label.grid(row=1, column=0, padx=20, pady=0, sticky='E')

#input field for the IP address
ipaddress_input = tk.Entry(main, font=('Times', 12, 'bold'), width=25, bg="silver")
ipaddress_input.grid(row=1, column=1, padx=0, pady=5)

#label for the subnet number input field
subnetnumber_label = tk.Label(main, font=('Times', 11, 'bold'), text="Number of Subnets:", bg="skyblue")
subnetnumber_label.grid(row=2, column=0, padx=20, pady=0, sticky = 'E')

#input field for the subnet number
subnet_input = tk.Entry(main, font=('Times', 12, 'bold'), width=25, bg="silver")
subnet_input.grid(row=2, column=1, padx=0, pady=5)

#calculate button
calculate_button = tk.Button(main, width=15, bg="indianred", cursor='circle', font=('Times', 10, 'bold'), text="Calculate", command=ip_calculator)
calculate_button.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

#labels for displaying the results
ip_class_label = tk.Label(main, font=('Times', 11, 'bold'), bg="skyblue")
ip_class_label.grid(row=4, column=0, columnspan=2, padx=40, pady=5, sticky='W')
default_subnet_label = tk.Label(main, font=('Times', 11, 'bold'), bg="skyblue")
default_subnet_label.grid(row=5, column=0, columnspan=2, padx=40, pady=5, sticky='W')
bits_label = tk.Label(main, font=('Times', 11, 'bold'), bg="skyblue")
bits_label.grid(row=6, column=0, columnspan=2, padx=40, pady=5, sticky='W')
custom_subnet_label = tk.Label(main, font=('Times', 11, 'bold'), bg="skyblue")
custom_subnet_label.grid(row=7, column=0, columnspan=2, padx=40, pady=5, sticky='W')
networks_label = tk.Label(main, font=('Times', 11, 'bold'), bg="skyblue")
networks_label.grid(row=8, column=0, columnspan=2, padx=40, pady=5, sticky='W')
hosts_label = tk.Label(main, font=('Times', 11, 'bold'), bg="skyblue")
hosts_label.grid(row=9, column=0, columnspan=2, padx=40, pady=5, sticky='W')

#IP Calculator User Interface

main.geometry("400x450")
main.configure(width=1500,height=600,bg='skyblue')
main.title("IP Calculator - BET COET 4B")
main.mainloop()
