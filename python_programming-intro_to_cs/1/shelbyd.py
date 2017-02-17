def main():
    for _ in range(5):
      celsius = eval(input("What is the Celsius temperature? "))
      farenheit = 9/5 * celsius + 32
      print("The temperature is ", farenheit, "degrees Farenheit.")

main()
