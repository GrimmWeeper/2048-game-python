import numpy as np

def main():
    
    array = []                    #Create 4x4 board with digit '2' on 2 randomly assigned tiles
    for i in range(16):
        array.append(0)
    array_tworand= np.random.choice(16,2,replace=False)
    for i in range(2):
        array[array_tworand[i]] = 2
    board(array) 
    
    while True:                   #Loop through the game after each moves
        array_initial = list(array)
        print("""
'0' = left ; '1' = up ; '2' = right ; '3' = down""")
        while True:
            try:
                arrow = int(input("Key in a digit (0-3):"))   #Command user to input digit (0-3) for directions
                print("")
            except ValueError as error:
                continue
            if arrow == 0 or arrow == 1 or arrow == 2 or arrow == 3:  #Only accept 0-3 as input
                break        
        shift(array,arrow)         #Move the tiles
       
        if np.array_equal(array_initial,array) == True and np.count_nonzero(array) != 16:   #Catch invalid move and allow user to retry
            print("Invalid move. Please key in another digit.")
            continue
       
        elif np.count_nonzero(array) == 16:   #Prevent game from ending when there are still possible moves available with completely filled board
            for i in range(4):
                arrow = i
                array_test = list(array)
                shift(array_test,arrow)
                if np.array_equal(array_initial,array_test) == False:
                    print("Invalid move. Please key in another digit.")
                    break
           
            if i == 3 and np.array_equal(array_initial,array_test) == True:  #End the game when there are no available moves
                board(array)
                print("""
==================== GAME OVER ====================""")
                break
            
            else:
                continue
                
        else:
            array_zero = []      #Insert '2' into a random unfilled tile after each moves
            for i in range(16):
                if array[i] == 0:
                    array_zero.append(i)
            array_onerand= np.random.choice(len(array_zero),1)
            array[array_zero[array_onerand[0]]] = 2
            board(array)

     
        
def board(a):     #Function to print out the 4x4 board
    print("Output:")    
    print("{} {} {} {}".format(a[0],a[1],a[2],a[3]))
    print("{} {} {} {}".format(a[4],a[5],a[6],a[7]))    
    print("{} {} {} {}".format(a[8],a[9],a[10],a[11]))
    print("{} {} {} {}".format(a[12],a[13],a[14],a[15]))    

def shift(x,y):     #Function to move the tile in the requested direction. 
                    # "x" = array, "y" = direction
    def flush(j,k,l,m):   #Function to move each row/column with the correct set of rules
        sets = [j,k,l,m]
        count_dup = 0
        while True:
            count = 0
            
            for b in range(3):
                if sets[b] != 0 and sets[b+1] ==0 :
                    (sets[b+1],sets[b]) = (sets[b],sets[b+1])
                    count += 1
                elif sets[b] == sets[b+1] and sets[b] != 0:
                    sets[b+1] = sets[b] + sets[b+1]
                    sets[b]=0
                    count += 1
                    if b == 0 and sets[1] == sets[2] and sets[2] != sets[3] and sets[3] != 0:
                        sets[1] += 1
                        count_dup = 1
                    elif b == 0 and sets[1] == sets[2] and sets[2] != sets[3] and sets[3] == 0:
                        sets[1] += 1
                        count_dup = 9
                    elif b == 0 and sets[1] == sets[2] and sets[2] == sets[3]:
                        sets[1] = 0
                        sets[3] *= 2
                        count_dup = 8 
                    elif b == 0 and sets[1] == sets[3] and sets[2] == 0:
                        sets[1] += 1
                        count_dup = 5
                    elif b == 1 and sets[2] == sets[3]:
                        sets[2] += 1
                        count_dup = 2
                    elif b == 1 and sets[2] == sets[0] and sets[1] == 0 and sets[3] != 0:
                        sets[2] += 1
                        count_dup = 6    
                    elif b == 1 and sets[2] == sets[0] and sets[1] == 0 and sets[3] == 0:
                        sets[2] += 1
                        count_dup = 7    
                    elif b == 2 and (sets[3] == sets[1] or sets[3] == sets[0]):
                        sets[3] += 1
                        count_dup = 3
                    elif b == 0 and sets[0] == sets[1] == sets[2] == sets[3]:
                        sets[0] = 0
                        sets[1] = 1
                        sets[2] *= 2
                        sets[3] *= 2
                        count_dup = 4
           
            if count == 0 and count_dup == 0 :
                break
            elif count == 0 and count_dup == 1:
                sets[1] -= 1
                break
            elif count == 0 and count_dup == 2:
                sets[2] -= 1
                break
            elif count == 0 and count_dup == 3:
                sets[3] -= 1
                break
            elif count_dup == 4:
                break
            elif count == 0 and count_dup == 5:
                sets[2] -= 1
                break
            elif count == 0 and count_dup == 6:
                sets[2] -= 1
                break
            elif count == 0 and count_dup == 7:
                sets[3] -= 1
                break
            elif count_dup == 8:
                break
            elif count_dup == 9 and count == 0:
                sets[2] -= 1
                break
        return sets

    if y == 0 :
        x[3],x[2],x[1],x[0] = flush(x[3],x[2],x[1],x[0])
        x[7],x[6],x[5],x[4] = flush(x[7],x[6],x[5],x[4])
        x[11],x[10],x[9],x[8] = flush(x[11],x[10],x[9],x[8])
        x[15],x[14],x[13],x[12] = flush(x[15],x[14],x[13],x[12])
    
    elif y == 1 :
        x[12],x[8],x[4],x[0] = flush(x[12],x[8],x[4],x[0])
        x[13],x[9],x[5],x[1] = flush(x[13],x[9],x[5],x[1])
        x[14],x[10],x[6],x[2] = flush(x[14],x[10],x[6],x[2])
        x[15],x[11],x[7],x[3] = flush(x[15],x[11],x[7],x[3])
    
    elif y == 2 :
        x[0],x[1],x[2],x[3] = flush(x[0],x[1],x[2],x[3])
        x[4],x[5],x[6],x[7] = flush(x[4],x[5],x[6],x[7])
        x[8],x[9],x[10],x[11] = flush(x[8],x[9],x[10],x[11])
        x[12],x[13],x[14],x[15] = flush(x[12],x[13],x[14],x[15])
    
    elif y == 3 :
        x[0],x[4],x[8],x[12] = flush(x[0],x[4],x[8],x[12])
        x[1],x[5],x[9],x[13] = flush(x[1],x[5],x[9],x[13])
        x[2],x[6],x[10],x[14] = flush(x[2],x[6],x[10],x[14])
        x[3],x[7],x[11],x[15] = flush(x[3],x[7],x[11],x[15])
    



if __name__ == "__main__":
    main()