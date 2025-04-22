import random
import time

def user_choice():
    choices = ['rock', 'paper', 'scissors']
    while True:
        print("\nOptions: rock, paper, scissors")
        user_input = input("Your choice: ").lower().strip()
        if user_input in choices:
            return user_input
        else:
            print("❌ Invalid choice. Please try again.")

def comp_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def winner(user, computer):
    if user == computer:
        return "tie"
    win = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }
    return "user" if win[user] == computer else "computer"

def animate():
    for _ in range(3):
        print(".", end='', flush=True)
        time.sleep(0.3)
    print()

def result(user, computer, winner, scores):
    print(f"\nYou chose: {user.upper()}")
    print(f"Computer chose: {computer.upper()}")
    
    animate()
    
    if winner == "tie":
        print("🤝 IT'S A TIE!")
    elif winner == "user":
        print(f"🎉 YOU WIN! {user.upper()} beats {computer.upper()}")
    else:
        print(f"💻 COMPUTER WINS! {computer.upper()} beats {user.upper()}")
    
    print(f"\nSCOREBOARD - You: {scores['user']} | Computer: {scores['computer']}")

def ascii_game(choice):
    art = {
        'rock': '''
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        ''',
        'paper': '''
            _______
        ---'   ____)____
                  ______)
                 _______)
                _______)
        ---.__________)
        ''',
        'scissors': '''
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        '''
    }
    print(art.get(choice, ""))

scores = {'user': 0, 'computer': 0}
cnt = 1

while True:
    print(f"\n=== ROUND {cnt} ===")
    user = user_choice()
    computer = comp_choice()
    
    ascii_game(user)
    print("\n                                                               VS\n")
    ascii_game(computer)
    
    winner = winner(user, computer)
    
    if winner == "user":
        scores['user'] += 1
    elif winner == "computer":
        scores['computer'] += 1
    
    result(user, computer, winner, scores)
    cnt += 1
    
    if input("\nPlay again? (yes/no): ").lower() != 'yes':
        print("\n=== FINAL RESULTS ===")
        print(f"🏆 You: {scores['user']} | Computer: {scores['computer']}")
        if scores['user'] > scores['computer']:
            print("✨ YOU ARE THE CHAMPION! ✨")
        elif scores['user'] < scores['computer']:
            print("🤖 COMPUTER WINS THE GAME!")
        else:
            print("🤝 IT'S A DRAW!")
        break
