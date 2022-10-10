#There will be 9 entries in the tic tac toe game initially they are blank
# We have used dictionary datatype to store the values 
d = {1:' ', 2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}

def display_row(d,row_number):
    

display_row(d,1)

#function for printing the horizontal sepration between two rows
def display_horizonal_line(n):
    
display_horizonal_line(17)

def display_board(d):
    
display_board(d)

def player_name():   
      #stores the name of first user
    
    

def row_check(d,char,i):
    
def column_check(d,char,i):
    if d[i+1] == char and d[i+4] == char and d[i+7] == char:
        return True
    else:
        return False

#checks whether all positions in a particular diagonal are same
#if they are same it returns true else it return false
def diag1_check(d,char):
    if d[1] == char and d[5] == char and d[9] == char:
        return True
    else:
        return False

def diag2_check(d,char):
    if d[3] == char and d[5] == char and d[7] == char:
        return True
    else:
        return False

def won(d,char):
    

def complete(d):                                     
    f

#How number are connected to grid
ref = {1:'1', 2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}
print("Following are number relation to grid cells")
display_board(ref)


player = 1
# reinitializing the whole grid
d = {1:' ', 2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
display_board(d)
while(True):
    if player == 1:   # Condition for which player to move
        
        player = 2  

    else:
        print(user_2 , "Please select a cell from 1,2...9 where you want to put " , user_2_char)
        place = input()
        ls = ['1','2','3','4','5','6','7','8','9']
        flag1 = 1 
        flag2 = 1
        while(flag1 == 1 or flag2 == 1):
            flag1 = 1 
            flag2 = 1
            if place not in ls:
                print("You have choose not choose form 1 to 9 . Please choosen from 1 - 9")
                place = input("Try again")
                continue
            else:
                flag1 = 0
            place = int(place)
            if d[place] != ' ':
                print("This place is already occupied")
                place = input("Try again")
                continue
            else:
                flag2 = 0;     
        d[place] = user_2_char
        display_board(d)
        if won(d,user_2_char) == True:
            print("Congrats!",user_2,"you won")
            break
        player = 1
    if complete(d) == True:
        print("Match Draw!!!!")
        break
