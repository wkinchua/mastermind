import random

shapes = ["circle", "square", "triangle", "star", "heart", "rectangle", "pentagon"]
guess = []
secret_code = []

def generate_secret_code(): #create a secret code/answer
    return random.choices(shapes, k=4)

def choose_difficulty(diff): #difficulty settings
    if diff.lower() == "easy":
        return "E"
    elif diff.lower() == "hard":
        return "H"
    else:
        return None

def get_user_guess(): #gets user input
    guess = []

    for i in range(4): #get the 4 guesses from user
        g = input(f"Enter shape #{i + 1} (type 'stop' to stop): ").strip().lower()
        guess.append(g)
        if g == "stop":
            break

    
    if "stop" in guess: #stop for easy mode
        return g
    else:
        return guess

    
def evaluate_guess(user_guess, secret_code): #check and compare user guess to actual answer
    correct_place = 0
    correct_shape = 0

    temp_secret = secret_code.copy()
    temp_guess = user_guess.copy()

    
    for i in range(4): # check if user guess is correct
        if temp_guess[i] == temp_secret[i]:
            correct_place += 1
            

    
    for i in range(4): #check how many user enter is actually correct but wrong place
        if temp_guess[i] in temp_secret:
            correct_shape += 1
            index = temp_secret.index(temp_guess[i])
            

    print(f"Correct position: {correct_place}, Wrong position: {correct_shape}")
    

    if correct_place == 4: #check for win
        return "Win"
    

 


def print_game_summary(attempt,guess,secret_code): #print summary
    
    print("-------- Game Result Summary --------")
    print(f"Secret Code: {secret_code}")
    print(f"Final Guess: {guess}")
    print(f"Total Attempt: {attempt}")


end = False

while not end: #main game loop (start of the game)
    print("Welcome to Mastermind Shapes")
    print("To stop, type exit")
    inp = input("Choose your difficulty (Easy/Hard)\n")

    if inp.lower() == "exit":
        end = True

    if choose_difficulty(inp) == "E": #if user wants to play easy mode
        attempt = 0 
        secret_code = generate_secret_code()
        print(secret_code)
        while True: #they get unlimited tries until they get it
            attempt += 1
            
            users_guess = get_user_guess()

            if users_guess == "stop": # if they want to stop, they type stop
                break

            if evaluate_guess(users_guess,secret_code) == "Win":
                print_game_summary(attempt,users_guess,secret_code) #print summary breaking this loop return to main loop
                break

    elif choose_difficulty(inp) == "H": # choosing hard difficulty
        win = False
        attempt = 0
        secret_code = generate_secret_code() 
        while attempt != 10: #user only have 10 attempt in hard difficulty
            attempt += 1
            
            users_guess = get_user_guess()

            if evaluate_guess(users_guess,secret_code) == "Win": # if they win print summary and break out of this loop, back to main loop
                print_game_summary(attempt,users_guess,secret_code)
                win = True
                break
        
        if win == False: # if they ran out of 10 attempt, print summary and break out of loop, back to main loop
            print_game_summary(attempt,users_guess,secret_code)

      
        
              


            





            

            