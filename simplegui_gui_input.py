'''
Author Name: Abhilasha Dave
Date : 02/22/2018
Description:
Queation 1 and 2 for characters
PART A
1) Characters
     Automatically generates an array of random characters
     Prompts for user to specify length and range of array
2) User input
    Take length and range of array from the user
    Prompts the user for an array of single characters
3) Output
    Generate random characters array in given constraints
PART B
    All user input must be validate to prevent program instability
'''
# Import all libraries
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random
import string

# Class that takes inputs for the array and return the random array in given constraints.

class random_integers():
    
    #Define the initial method for the class
    def __init__(self,length_array,start_range_array,end_range_array):
        self.length_array = length_array
        self.start_range_array = start_range_array
        self.end_range_array = end_range_array

    #create the array using given length and range
    def random_array(self):
        return (random.sample(range (self.start_range_array,self.end_range_array), self.length_array))




# Class that takes inputs for the array and return the random array in given constraints.

class random_charactor():

    random = 0
    #Define the initial method for the class
    def __init__(self,values,length_array):
        self.length_array = length_array
        self.values = values

    #create the array using given length and range
    def random_array(self):
            # random.choice returns a random character array.
            letter = ''.join([random.choice(self.values) for i in range (self.length_array)]) 
            return (letter)
 

'''
Description:
Question-3,4,5
Remove all duplicate elements within the array
Sort the array in ascending order
Find consecutive runs within the array, ignoring runs of length less than 2
Sum the contents of each consecutive run
Find the median character of each consecutive run, rounded down
Provide a menu choice that will close the program.
After the results are displayed, return to main menu and prompt the user for another menuchoice.
'''


# Class that takes inputs for the array and return the random array in given constraints.

class user_integer_array():
    
    #Define the initial method for the class
    def __init__(self,user_array):
        self.user_array = user_array
    
    #PART A and PART B of the question
    #Remove all duplicate elements within the array and sort the array in assending order
    def duplicate_sort_list(self):
        set_sort_list = list(set(self.user_array))
        removeDuplicates_sortString = ("set and sort string: PART A & B",set_sort_list)
    
    #PART C and PART D
    #Find consecutive runs within the array, ignoring runs of length less than 2
    #Sum the contents of each consecutive run 
        step = 1
        consecutive_run_array = []
        sum_contents = []
        result = [consecutive_run_array]
        expect = None
        for set_value in set_sort_list:
            if (set_value == expect) or (expect is None):
                consecutive_run_array.append(set_value)
                sum_contents.append(sum(consecutive_run_array))
            else:
                consecutive_run_array = [set_value]
                result.append(consecutive_run_array)
            expect = set_value + step
        con_runs = ("The consecutive run:PART C ",result)
        sum_con_runs = ("This is the sum of consecutive array:PART D",sum_contents)
        return (removeDuplicates_sortString,con_runs,sum_con_runs)

       
#PART E
#find the maiden character
#Tried to bring output but running out of time. Little bit logic is given below not sure will work or not
'''       
class character_array():
    def __init__(self,character):
        self.character = character
        step = 1
        consecutive_run_ch_array = []
        result_ch = [consecutive_run_ch_array]
        expect = None
        for i in self.character:
            if (i == expect) or (expect is None):
                consecutive_run_ch_array.append(i)
                #find maiden charactor
                p =  len(consecutive_run_ch_array)//2
                print (consecutive_run_ch_array[p-1])
            else:
                consecutive_run_ch_array = [i]
                result_ch.append(consecutive_run_ch_array)
            expect = i + step
'''




#===================================== Global variable declaration =============================================================================

int_array = []
cha_array = []
a = []
b = []
c = []
lengthArray = 0
startRangeArray = 0
endRangeArray = 0
string_value = []
char_array = []
lenth_string = 0
exception = ''

#Handler methods for buttons
#================= Handler method for integer array which call text input method==================================================================

def integer_array():
    f.add_input("Enter start range of array", enter_start, 100)
    f.add_input("Enter end range of array", enter_end, 100)
    f.add_input("Enter length of array",enter_length,100)
    
#text input method for integer array

def enter_start(t):
    global startRangeArray,exception
    while True:
        try:
            startRangeArray = int(t)
            break
        except ValueError:
            exception = ("Sorry! The alphabet and special character are not valid please enter only numeric value.")
            f.set_draw_handler(draw_exception)
            break

def enter_end(t):
    global endRangeArray,exception
    while True:
        try:
            endRangeArray = int(t)
            break
        except ValueError:
            exception = ("Sorry! The alphabet and special character are not valid please enter only numeric value.")
            f.set_draw_handler(draw_exception)
            break
            
def enter_length(t):
    global lengthArray,exception
    while True:
        try:
            lengthArray = int(t)
            call_fun()
            break
        except ValueError:
            exception = ("Sorry! The alphabet and special character are not valid please enter only numeric value.")
            f.set_draw_handler(draw_exception)
            break
#==================== Creat an instentian for integer array class and call the class to perform an operation ======================================            

def call_fun():
    global lengthArray,endRangeArray,startRangeArray,int_array,exception
    while True:
        try:
            if endRangeArray > startRangeArray & endRangeArray != startRangeArray:
                inst1 = random_integers(lengthArray,startRangeArray,endRangeArray)
                int_array = (inst1.random_array())
                f.set_draw_handler(draw_intArray)
                break
        except ValueError:
            exception = ("Sorry! The end range of array should greater than start range of array.")
            f.set_draw_handler(draw_exception)
            break



#================= Handler method for character array which call text input method==================================================================

def cha_array():
    f.add_input("Enter your charactor string", char_string,100)
    f.add_input("Enter length of random string",char_length_string,100)
def char_string(t):
    global string_value,exception
    while True:
        try:
            string_value = str(t)
            if not string_value:
                exception = ("please do not put string null")
                f.set_draw_handler(draw_exception)
                break
            break
        except ValueError:
            exception = ("Please do not enter numeric values characters only")
            f.set_draw_handler(draw_exception)
            break
def char_length_string(t):
    global lenth_string,exception,string_value
    while True:
        try:
            if not string_value:
                exception = ("please enter string first and don't put null value")
                f.set_draw_handler(draw_exception)
                break
            elif string_value:
                lenth_string = int(t)
                call_fun_char()
                break
        except ValueError:
            exception = ("Please enter only numeric values no characters are allowed")
            f.set_draw_handler(draw_exception)
            break
        
#==================== Creat an instentian for character array class and call the class to perform an operation ======================================

def call_fun_char():
    global string_value,lenth_string,char_array
    inst2 = random_charactor(string_value,lenth_string)
    char_array = (inst2.random_array())
    f.set_draw_handler(draw_chaArray)

def process_array():
    global a,b,c
    inst1 = user_integer_array([8,9,12,3,7,20,16,2,8,16,17,20,7])
    a,b,c = inst1.duplicate_sort_list()
    f.set_draw_handler(draw_processString)

def exit_program():
    f.stop()

#================= Handler method for processing the string of array ==================================================================
def draw_processString(canvas):
    global a,b,c
    canvas.draw_text(str(a),[10, 50], 18, "Red")
    canvas.draw_text(str(b),[10, 100], 18, "Green")
    canvas.draw_text(str(c),[10, 150], 18, "Blue")



#===================================== Draw handler methodes ===========================================================================

#draw handler for integer string
def draw_intArray(canvas):
    global int_array
    canvas.draw_text(str(int_array),[10, 100], 18, "Blue")
    
#draw handler for character string array
def draw_chaArray(canvas):
    global cha_array
    canvas.draw_text(str(char_array),[10, 100], 28, "Red")


#draw handler method for exceptions
def draw_exception(canvas):
    global exception
    canvas.draw_text(str(exception),[10, 100], 18, "Yellow")

#============================================ create frame =============================================================================

f = simplegui.create_frame("Console Based User Interface",700,400)

#========================== register all event handlers for button =====================================================================

f.add_button("Random Integer Array", integer_array, 200)
f.add_button("Random character Array", cha_array, 200)
f.add_button("Process Array", process_array, 200)
f.add_button("Exit Program", exit_program,200)

#============================ Start the frame ==========================================================================================
f.start()
