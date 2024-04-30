# Marwan Elgoghel
# CS 175L
# Expense Pie Chart

import matplotlib.pyplot as plt

def PieChart(expenseA, expenseN):
    plt.pie(expenseA, labels=expenseN)
    plt.title("Monthly Expenses")
    plt.show()



def main():
    expenseN = []
    expenseA = []
    with open("expenses.txt", "r") as file:
        count = 0
        for line in file:
            everything = line.strip().split("\t")
            name = everything[0]
            if len(everything) == 2:
                try:
                    expenseN.append(name)
                    amount = float(everything[1])
                    expenseA.append(amount)
                except ValueError:
                    print(f"INVALID AMOUNT FOR {name.upper()}")
                    expenseN.pop(count)
            count += 1
    PieChart(expenseA, expenseN)





if __name__ == "__main__":
    main()