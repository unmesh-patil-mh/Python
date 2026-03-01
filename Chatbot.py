def Introduce(name,year):
    print("Welcome To the Chatbot User")
    print("Hello! Welcome User my name is: ",name)
    print("I was created in the year: ",year)
    
def ask_name():
    n = input("What is Your Name? \n")
    print("Nice to meet you ",n," ,Hope you are doing well")
    return n
    
def show_world_cup_history():
    choice = input("Do you want me to print last 5 winners of world cup? (y/n)\n")
    
    if choice.lower() == 'y':
        print("Here are the winners of the last 5 ODI Cricket World Cups:")
        print("2023 - Australia")
        print("2019 - England")
        print("2015 - Australia")
        print("2011 - India")
        print("2007 - Australia\n")
    else:
        print("Ok No Worries") 
    
def guess_age():
    print("Let's Play a fun game i will try to guess your age \n")
    
    r3=int(input("What is remainder when we divide your age by 3: "))
    r5=int(input("What is remainder when we divide your age by 5: "))
    r7=int(input("What is remainder when we divide your age by 7: "))
    
    age = ((r3*70)+(r5*21)+(r7*15))%105
    
    print("I Guess your age is: ",age)
    
def show_team_india():
    userdesi = input("Do you want me to show the playing 11 for world cup?(y/n) \n")
    
    if userdesi.lower() == 'y':
        print("Here is Team India's Playing 11 for T20 World Cup:\n")
        players = [
            "Rohit Sharma",
            "Virat Kohli",
            "Rishabh Pant",
            "Suryakumar Yadav",
            "Hardik Pandya",
            "Shivam Dube",
            "Ravindra Jadeja",
            "Axar Patel",
            "Jasprit Bumrah",
            "Mohammed Siraj",
            "Kuldeep Yadav"
        ]

        for player in players:
            print(player)

        print()
        
    else:
        print("Ok no worries")

def main():
    Introduce("ubot","2026")
    ask_name()
    show_world_cup_history()
    guess_age()
    show_team_india()
    print("Thank you for chatting with me ")
    
if __name__ == "__main__":    
    main()