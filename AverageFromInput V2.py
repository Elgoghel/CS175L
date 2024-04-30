#Marwan Elgoghel
#CS 175
#AverageFromInput

def IoError_Handling():
    print("SystemExit: File not found: numbers.txt - exiting")
    exit()

def valueError_handling():
    print(f"Bad Data: {badData} - skipping")

def main():
    Total = 0
    counter = 0

    file = open("numbers.txt", 'r')
    for line in (file):
        number = float(line.strip())
        Total += number
        counter += 1
        print(f'I read in {counter} number(s). Current number is:    {number:.2f}  Total is:    {Total}')
    try:
        file = open("numbers.txt", 'r')
    except IOError:
        IoError_Handling()

    for line in file:
        try:
            number = float(line.strip())
            Total += number
            counter += 1
            print(f'I read in {counter} number(s). Current number is:    {number:.2f}  Total is:    {Total}')
        except ValueError:
            number = str(line.strip())
            global badData
            badData = number
            valueError_handling()

    average = Total / counter
    print(f"Average: {average:.1f}")

    file.close()

if __name__ == '__main__':
    main()