#Marwan Elgoghel
#CS 175
#AverageFromInput

def main():
    Total = 0
    counter = 0

    file = open("numbers.txt", 'r')
    for line in (file):
        number = float(line.strip())
        Total += number
        counter += 1
        print(f'I read in {counter} number(s). Current number is:    {number:.2f}  Total is:    {Total}')
    average = Total / counter
    print(f"Average: {average:.1f}")

if __name__ == '__main__':
    main()