# Modify the following code so that it prints the celsius temperature and the
# farenheit equivalent every 10 degrees from 0C to 100C.

def main():
    celsius = eval(input("What is the Celsius temperature? "))
    farenheit = 9/5 * celsius + 32
    print("The temperature is ", farenheit, "degrees Farenheit.")

main()
