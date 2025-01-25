def main():

    
    # initailize states list
    stateList = []
    file = open(r"\Users\Thoan\Desktop\REIA\statesList.txt")
    fileContents = file.read()
    while fileContents:
        stateList.append(stateList)
        fileContents = print(fileContents)
    file.close()


    choice = 0
    while choice !=4:
        print("*** State  View ***" )
        print("1) Show all States")
        print("2) Search for a State")
        print("3) Search for your State")
        print("4) Quit")
        choice = int(input())

        if choice == 1:
             print("Displaying all States...")
             nState = input("Enter the name of the State >>>")
             stateList.append([nState])

        elif choice == 2:
             print("Search for a State...")
             keyword = input("Enter Search Term: ")
             for state in stateList:
                  if keyword in state:
                       print(state)

        elif choice == 3:
             print("Search for your State...")
             for i in range(len(stateList)):
                  print(stateList[i])

        elif choice ==4:
             print("Quitting Program")
    print("Program Terminated!")



if __name__ == "__main__":
        main()