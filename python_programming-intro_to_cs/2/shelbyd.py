def main():
    for celsius in range(0, 110, 10):
      farenheit = 9/5 * celsius + 32

      print(celsius, "C ->", farenheit, "F")

main()
