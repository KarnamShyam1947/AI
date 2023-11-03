def isGoalState(currentState, goalState):
    if(currentState[0] == goalState[0]) or currentState[1] == goalState[0]:
        return True
    
    return False

def valid_rules(x, y):
    result = dict()
    
    # filling
    x1 = x
    y1 = y
    if x1 < jug1:
        x1 = jug1

        if (x, y) != (x1, y1):
            result[1] = (x1, y1)

    x1 = x
    y1 = y 
    if y1 < jug2:
        y1 = jug2

        if (x, y) != (x1, y1):
            result[2] = (x1, y1)
    
    #empty
    x1 = x
    y1 = y
    if x1 > 0:
        x1 = 0

        if (x, y) != (x1, y1):
            result[3] = (x1, y1)
    
    x1 = x
    y1 = y
    if y1 > 0:
        y1 = 0

        if (x, y) != (x1, y1):
            result[4] = (x1, y1)
    
    # pour 
    x1 = x
    y1 = y
    if x1 + y1 >= jug1:
        y1 = y1 - (jug1-x1)
        x1 = jug1

        if (x, y) != (x1, y1):
            result[5] = (x1, y1)

    x1 = x
    y1 = y
    if x1 + y1 >= jug2:
        x1 = x1 - (jug2-y1)
        y1 = jug2

        if (x, y) != (x1, y1):
            result[6] = (x1, y1)
    
    # swap
    x1 = x
    y1 = y
    if x1 + y1 < jug1:
        x1 = x1 + y1
        y1 = 0

        if (x, y) != (x1, y1):
            result[7] = (x1, y1)
    
    x1 = x
    y1 = y
    if x1 + y1 < jug2:
        y1 = x1 + y1
        x1 = 0

        if (x, y) != (x1, y1):
            result[8] = (x1, y1)
        
    return result

def apply_rule(x, y, rno):
    
    if rno == 1: # filling
        if x < jug1:
            x = jug1

        else:
            return False
        
    elif rno == 2: 
        if y < jug2:
            y = jug2

        else:
            return False
        
    elif rno == 3: #empty
        if x > 0:
            x = 0

        else:
            return False
        
    elif rno == 4:
        if y > 0:
            y = 0

        else:
            return False
        
    elif rno == 5: # pour 
        if x + y >= jug1:
            y = y - (jug1-x)
            x = jug1

        else:
            return False
        
    elif rno == 6:
        if x + y >= jug2:
            x = x - (jug2-y)
            y = jug2

        else:
            return False
        
    elif rno == 7: # swap
        if x + y < jug1:
            x = x + y
            y = 0

        else:
            return False
        
    elif rno == 8:
        if x + y < jug2:
            y = x + y
            x = 0

        else:
            return False
        
    return (x, y)

if __name__ == '__main__':
    print('NAME : KARNAM SHYAM\t\t\tREG. NO. : 21MIC7182\n')
    jug1 = int(input("Enter max capacity of jug1 : "))
    jug2 = int(input("Enter max capacity of jug2 : "))

    target = int(input("Enter amount to measure : "))
    x = 0
    y = 0
    
    steps = 0
    goalState = (target, )
    currentState = (x, y)
    print(f"Goal state : {goalState}")
    print('1.Fill the jug1 completely')
    print('2.Fill the jug2 completely')
    print('3.Empty the jug1')
    print('4.Empty the jug2')
    print('5.Pour some water from the jug2 to fill the jug1')
    print('6.Pour some water from the jug1 to fill the jug2')
    print('7.Pour all water from jug2 to the jug1')
    print('8.Pour all water from jug1 to the jug2')
    while True:
        print("\n--------------------------------------------------------------------------------")
        print(f"current state : {currentState}\t\tGoal state : {goalState}\t\tNo. of moves : {steps}")
        
        rules = valid_rules(x, y)
        print("Valid rules:")
        for rno, state in rules.items():
            print(f'{rno} -> {state}')
        rno = int(input(f"Enter rule number : "))
        
        if rno not in rules:
            print("Invalid rule.... :(")
            continue
        
        check = apply_rule(x, y, rno)
        
        if check is False:
            print("Invalid rule.... :(")
            
        else:
            currentState = check
            x, y = check
            
        if isGoalState(currentState, goalState):
            print(f'Goal State Reached in {steps} moves..... :) ')
            # print(f"Goal state : {currentState}")
            break

        steps += 1