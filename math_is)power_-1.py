import random
import time

# --------------------------
# Player and Dragon Classes
# --------------------------
class Player:
    def __init__(self):
        self.hp = 20
        self.gears = []
        self.digits_collected = []
        self.heals_left = 3
        self.streak = 0  # chapter win streak for bonus gear
        self.password_ready = False
        self.password_code = ""

class Dragon:
    def __init__(self, chapter):
        self.level = chapter + 2  # fixed level per chapter
        self.hp = 10 + chapter * 2  # increases each chapter

# --------------------------
# Gear and Damage System
# --------------------------
type1_gears = ["Immunity", "Hourglass", "Brightness Lamp", "Invisibility"]
type2_gears = ["Shield", "Armor", "Helmet"]
type3_gears = ["Sword", "Fire", "Water"]

def calculate_player_attack(player):
    total_attack = 0
    for gear in player.gears:
        if gear in type3_gears:  # Type3
            total_attack += random.randint(8,10)
        elif gear in type2_gears:  # Type2
            if random.random() < 0.8:
                total_attack += random.randint(4,5)
            else:
                total_attack += 6
        elif gear in type1_gears:  # Type1
            total_attack += random.randint(0,1)
    return total_attack

def dragon_attack(player, immunity=False, difficulty='normal'):
    if immunity:
        print("🛡️ Immunity blocked the attack!")
        return 0

    if random.random() < 0.8:
        dmg = random.randint(1,3)
    else:
        dmg = random.randint(4,6)

    if difficulty == 'easy':
        dmg = max(1, int(dmg * 0.6))
    elif difficulty == 'hard':
        dmg = int(dmg * 1.3)

    player.hp -= dmg
    print(f"Dragon hits you for {dmg}! Your HP: {player.hp}")
    return dmg

# --------------------------
# Chapter Numbers (5 digits)
# --------------------------
def show_scroll(difficulty_code=None, narrator=True, page_flip_mode='manual'):
    print("\n📜 Scroll of Directions")
    print("- How to Play: (1) math challenge, (2) collect numbers, (3) collect gear, (4) fight dragon, (5) streak rewards.")
    print("- Narrator: on/off (current: " + ("on" if narrator else "off") + ").")
    print("- Page Flip Mode: manual/automatic (current: " + page_flip_mode + ").")
    print("- After chapter 1, you can play mini-games for extra gear.")
    print("- Difficulty codes: p1/p2=easy, p3/p4=normal, p5/p6=hard.")
    if difficulty_code:
        print(f"- You are playing at code: {difficulty_code}. Keep your strategy.")
    print("📜 End of scroll\n")


def title_screen():
    print("\n========================")
    print("      MATH IS POWER")
    print("========================")
    input("Press Enter to open the book...")

    while True:
        a = random.randint(2, 8)
        b = random.randint(2, 8)
        ans = a + b
        try:
            response = int(input(f"Unlock question: {a} + {b} = ? ").strip())
        except ValueError:
            print("Please enter a number.")
            continue

        if response == ans:
            print("🔓 The book opens! You may begin your journey.")
            break
        else:
            print("❌ Wrong answer. Try again.")


def collect_numbers(chapter):
    numbers = []
    for i in range(5):
        num = random.randint(0,9)
        numbers.append(num)
        print(f"🔢 Number found: {num}")
        time.sleep(0.2)
    print(f"Narrator: \"All 5 numbers collected for this chapter: {numbers}\"")
    return numbers


def ask_quiz_question(choice):
    # Random question set for 3-in-a-row challenge
    candidates = []

    # Generate random questions for variety
    def gen_basic_add():
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        return f"Basic: {a} + {b} = ?", a + b

    def gen_basic_sub():
        a = random.randint(5, 25)
        b = random.randint(1, a)
        return f"Subtract: {a} - {b} = ?", a - b

    def gen_basic_mul():
        a = random.randint(2, 10)
        b = random.randint(2, 10)
        return f"Multiply: {a} × {b} = ?", a * b

    def gen_basic_div():
        a = random.randint(2, 10)
        b = random.randint(2, 10)
        prod = a * b
        return f"Divide: {prod} ÷ {a} = ?", b

    def gen_area():
        w = random.randint(2, 10)
        h = random.randint(2, 10)
        return f"Area: {w}x{h} rectangle area = ?", w * h

    def gen_fraction_add():
        p = random.randint(1, 5)
        q = random.randint(2, 5)
        r = random.randint(1, 5)
        s = random.randint(2, 5)
        correct = round(p/q + r/s, 2)
        return f"Fraction: {p}/{q} + {r}/{s} = ? (2 dp)", correct

    def gen_bodmas():
        a = random.randint(2, 5)
        b = random.randint(2, 5)
        c = random.randint(1, 5)
        correct = a * b + c
        return f"BODMAS: {a} × {b} + {c} = ?", correct

    # Add generators based on difficulty
    candidates.append(gen_basic_add)
    candidates.append(gen_basic_sub)
    candidates.append(gen_basic_mul)
    candidates.append(gen_basic_div)

    if choice in ('p3', 'p4', 'sec2', 'p5', 'p6', 'sec3'):
        candidates.append(gen_area)
        candidates.append(gen_fraction_add)

    if choice in ('p5', 'p6', 'sec3'):
        candidates.append(gen_bodmas)

    # Select and call a random generator
    q, correct = random.choice(candidates)()

    try:
        answer = float(input(f"Quiz question: {q} ").strip())
    except ValueError:
        print("❌ Invalid answer format")
        return False

    if abs(answer - correct) < 1e-2:
        print("✅ Correct")
        return True
    print(f"❌ Wrong, correct is {correct}")
    return False


def run_digit_streak(player, choice):
    if player.password_ready:
        print("🔐 Password already complete: use it at the machine.")
        return

    current_streak = 0
    print("\n🎯 3-in-a-row quiz to earn 1 password digit and 1 gear")
    while current_streak < 3:
        if ask_quiz_question(choice):
            current_streak += 1
            print("🔥 " + '●'*current_streak + '○'*(3-current_streak) + f" ({current_streak}/3)")
        else:
            current_streak = 0
            print("🔥 Reset streak to 0. Start again.")

    digit = random.randint(0, 9)
    player.digits_collected.append(str(digit))
    print(f"🏅 3-in-a-row complete! Digit earned: {digit}")

    bonus_gear = random.choice(type1_gears + type2_gears + type3_gears)
    if bonus_gear not in player.gears:
        player.gears.append(bonus_gear)
        print(f"⚙️ Bonus gear earned: {bonus_gear}")
    else:
        print(f"⚙️ Bonus gear would be {bonus_gear}, but you already have it. Extra bonus anyway!")

    if len(player.digits_collected) >= 5:
        player.password_ready = True
        player.password_code = ''.join(player.digits_collected[:5])
        print(f"🔐 Password complete: {player.password_code}. Use machine to unlock progression.")
    else:
        print(f"📜 Password progress: {''.join(player.digits_collected)} ({len(player.digits_collected)}/5)")


def run_password_machine(player):
    if not player.password_ready:
        print("🛠️ Machine locked: no full password yet. Collect 5 number streaks to build password.")
        return False

    print("\n🛠️ Chapter machine activated!")
    print(f"📜 Password paper: {player.password_code}")
    attempts = 3
    while attempts > 0:
        entry = input("Enter password into the machine: ").strip()
        if entry == player.password_code:
            print("🔓 Machine accepted the code! Chapter unlocked.")
            player.password_ready = False
            player.digits_collected = []
            player.password_code = ""
            return True
        attempts -= 1
        if attempts > 0:
            print(f"❌ Wrong code. {attempts} attempt(s) left.")

    print("⛔ Machine lockout! You can try again next chapter with streak rebuild.")
    return False


def ask_math_question(choice, chapter):
    # p3 onwards area/perimeter/fractions, p5 onwards BODMAS
    if choice in ('p5', 'p6', 'sec3'):
        # p5+: BODMAS or fraction
        if random.random() < 0.5:
            a = random.randint(2, 10)
            b = random.randint(2, 10)
            c = random.randint(1, 5)
            expr = f"{a} × {b} + {c}"
            correct = a * b + c
            q = f"BODMAS: {expr} = ?"
        else:
            p = random.randint(1, 9)
            q2 = random.randint(1, 9)
            r = random.randint(1, 9)
            s = q2
            expr = f"({p}/{q2}) + ({r}/{s})"
            correct = p/q2 + r/s
            q = f"Fraction: {expr} = ? (as decimal, 2 dp)"
            correct = round(correct, 2)
    elif choice in ('p3', 'p4', 'sec2'):
        # p3+: area/perimeter or fraction
        if random.random() < 0.5:
            width = random.randint(2, 10)
            height = random.randint(2, 10)
            correct = width * height
            q = f"Area: rectangle {width}x{height}, area = ?"
        else:
            p = random.randint(1, 9)
            q2 = random.randint(1, 9)
            r = random.randint(1, 9)
            s = random.randint(1, 9)
            correct = p/q2 - r/s
            correct = round(correct, 2)
            q = f"Fraction: {p}/{q2} - {r}/{s} = ? (2 dp)"
    else:
        # basic addition/subtraction
        a = random.randint(1, 15)
        b = random.randint(1, 15)
        correct = a + b
        q = f"Basic maths: {a} + {b} = ?"

    try:
        ans = float(input(f"Math question: {q} ").strip())
    except ValueError:
        print("Invalid number, question failed.")
        return False

    if abs(ans - correct) < 1e-2:
        print("✅ Correct math answer!")
        return True
    else:
        print(f"❌ Wrong. Correct was {correct}.")
        return False


def mini_game_bonus(player):
    print("\n🎮 Mini-game selection (name to play):")
    print("1. add agents")
    print("2. subtraction statics")
    print("3. multiplication mania")
    print("4. division drops")
    print("5. DAMSs (all 4)")
    choice = input("Enter 1-5: ").strip()

    def ask_simple(op):
        a = random.randint(2, 12)
        b = random.randint(2, 12)
        if op == 'add':
            corr = a + b
            q = f"{a} + {b} = ?"
        elif op == 'sub':
            corr = a - b
            q = f"{a} - {b} = ?"
        elif op == 'mul':
            corr = a * b
            q = f"{a} × {b} = ?"
        else:
            corr = a // b
            q = f"{a*b} ÷ {a} = ?"  # clean division
        try:
            a_ans = int(input(q + ' ').strip())
        except ValueError:
            return False
        return a_ans == corr

    success = False
    if choice == '1':
        success = ask_simple('add')
    elif choice == '2':
        success = ask_simple('sub')
    elif choice == '3':
        success = ask_simple('mul')
    elif choice == '4':
        success = ask_simple('div')
    elif choice == '5':
        success = all([ask_simple(op) for op in ['add','sub','mul','div']])
    else:
        print('Invalid mini-game choice.')
        return

    if success:
        bonus_gear = random.choice(type1_gears + type2_gears + type3_gears)
        if bonus_gear not in player.gears:
            player.gears.append(bonus_gear)
            print(f"🏅 Mini-game success! Gear earned: {bonus_gear}")
        else:
            print(f"🏅 You already have {bonus_gear}, but nice work! Keep going.")
    else:
        print("☹️ Mini-game failed. No bonus gear this time.")

# --------------------------
# Gear Assignment
# --------------------------
def collect_gears():
    collected = []
    collected.append(random.choice(type1_gears))
    collected.append(random.choice(type2_gears))
    collected.append(random.choice(type3_gears))
    print("Narrator: \"You collected some gears to aid in your battle!\"")
    for gear in collected:
        print(f"⚙️ {gear} collected")
    return collected


def display_gear_overview(player):
    print("\n🧾 Gear overview:")
    print("Type1 (heal/powerups): Hourglass, Brightness Lamp, Invisibility, Immunity")
    print("Type2 (defense/body): Shield, Armor, Helmet")
    print("Type3 (attack): Sword, Fire, Water")
    print("Your current gears:")
    for gear in player.gears:
        role = 'unknown'
        if gear in type1_gears:
            role = 'Heal/Power'
        elif gear in type2_gears:
            role = 'Defense'
        elif gear in type3_gears:
            role = 'Attack'
        print(f" - {gear}: {role}")


def chapter_quiz_reward(player, chapter):
    # No quiz questions; reward on 3 chapter-win streak
    player.streak += 1
    circles = '●' * min(player.streak, 3) + '○' * max(0, 3 - player.streak)
    print(f"🔥 {circles}  (streak {player.streak}/3)")

    if player.streak >= 3:
        player.streak = 0
        digit = random.randint(0, 9)
        player.digits_collected.append(digit)
        print(f"🏅 Streak reward! You earned password digit: {digit}")

        bonus_gear = random.choice(type1_gears + type2_gears + type3_gears)
        if bonus_gear not in player.gears:
            player.gears.append(bonus_gear)
            print(f"⚙️ Bonus gear earned: {bonus_gear}")
        else:
            print(f"⚙️ Bonus gear would be {bonus_gear}, but you already have it. Still, keep the momentum!")

        print("� Dots reset for next chapter")
        return True

    print("🌟 Keep going to fill all 3 circles for the digit and gear!")
    return False

# --------------------------
# Battle System
# --------------------------
def fight_dragon(player, chapter, difficulty='normal', narrator=True):
    dragon = Dragon(chapter)
    if narrator:
        print(f"\n⚡ The book pauses as you enter the cave... Zooming in for battle!")
        print(f"🔊 Dragon roar! RRRRRAAAARRR! Level {dragon.level}, HP {dragon.hp}\n")
    
    base_hp = 20 + chapter
    if difficulty == 'easy':
        player.hp = base_hp + 10
        player.heals_left = 5
    elif difficulty == 'hard':
        player.hp = max(5, base_hp - 5)
        player.heals_left = 2
    else:
        player.hp = base_hp
        player.heals_left = 3

    immunity = "Immunity" in player.gears
    
    start_time = time.time()
    time_limit = 180  # seconds
    
    while dragon.hp > 0 and player.hp > 0:
        print("\nChoose your action:")
        print("1. Attack")
        print("2. Defend")
        print(f"3. Heal ({player.heals_left} left)")
        action = input("Enter 1/2/3: ").strip().lower()

        if action in ("1", "attack", "a"):
            attack = calculate_player_attack(player)
            dragon.hp -= attack
            print(f"Narrator: \"Your gears strike the dragon for {attack} damage! Dragon HP: {max(0, dragon.hp)}\"")
            print("🔊 Clang! ⚡")
            defend_mode = False

        elif action in ("2", "defend", "d"):
            print("🛡️ You brace for the dragon's attack and reduce incoming damage.")
            attack = 0
            defend_mode = True

        elif action in ("3", "heal", "h"):
            if player.heals_left > 0:
                heal_amount = random.randint(2, 5)
                player.hp += heal_amount
                player.heals_left -= 1
                print(f"❤️ You recover {heal_amount} HP. Current HP: {player.hp}")
            else:
                print("❌ No heals left! You waste your turn.")
            attack = 0
            defend_mode = False

        else:
            print("⚠️ Invalid action, you lose your turn.")
            attack = 0
            defend_mode = False

        if dragon.hp > 0:
            if defend_mode:
                print("🛡️ You defend this turn.")
                before_hp = player.hp
                dmg = dragon_attack(player, immunity=False, difficulty=difficulty)
                reduced = max(0, int(dmg * 0.5))
                player.hp = before_hp - reduced
                print(f"🛡️ Defense reduced damage to {reduced}. Your HP: {player.hp}")
            else:
                dragon_attack(player, immunity, difficulty=difficulty)

            print("🔊 Dragon swipe sound! 🐉")
            time.sleep(0.3)

        # Time check
        if time.time() - start_time > time_limit:
            print("⏰ Time's up!")
            break
    
    if player.hp > 0:
        print("🏆 YOU WIN! The book stays open.\n")
        return True
    else:
        print("💀 You lost. The book closes. Retry this chapter to continue.\n")
        return False

# --------------------------
# Page Flip System
# --------------------------
def flip_pages(total_pages, mode="manual"):
    for i in range(1, total_pages+1):
        if mode == "manual":
            print(f"➡ Simulating manual page flip to page {i}...")
        else:
            print(f"➡ Auto-flipping page {i}...")
        print(f"📖 Flipped to page {i}")
        time.sleep(0.2)

def normalize_difficulty(choice):
    choice = choice.strip().lower()
    if choice in ('easy', 'p1', 'p2', 'sec1'):
        return 'easy'
    if choice in ('normal', 'p3', 'p4', 'sec2'):
        return 'normal'
    if choice in ('hard', 'p5', 'p6', 'sec3'):
        return 'hard'
    return None

# --------------------------
# Main Game
# --------------------------
def game():
    print("📖 Welcome to 'Math Is Power'!")
    difficulty = 'normal'
    while True:
        choice = input("Choose difficulty (p1/p2/p3/p4/p5/p6/sec1/sec2/sec3): ").strip().lower()
        mapped = normalize_difficulty(choice)
        if mapped:
            difficulty = mapped
            break
        print("Please enter a valid difficulty code (p1-p6, sec1-sec3).")

    narrator_choice = input("Narrator on or off? (on/off): ").strip().lower()
    narrator_on = narrator_choice != 'off'

    flip_choice = input("Flip mode (manual/auto): ").strip().lower()
    if flip_choice not in ('manual', 'auto'):
        flip_choice = 'manual'

    title_screen()
    print(f"Difficulty set to: {choice} ({difficulty})\n")
    show_scroll(choice, narrator=narrator_on, page_flip_mode=flip_choice)
    player = Player()
    
    for chapter in range(1, 51):  # 50 chapters total
        print(f"\n=== Chapter {chapter} ===")
        # math question before numbers
        ask_math_question(choice, chapter)

        # Must complete 5-digit password via 5 x (3 correct in a row) first
        while len(player.digits_collected) < 5:
            print("\n⏳ You need complete 5 digits of password before proceeding. Keep answering.")
            run_digit_streak(player, choice)

        # Collect 5 numbers for chapter
        numbers = collect_numbers(chapter)

        # Collect gears
        player.gears = collect_gears()
        display_gear_overview(player)

        # Scroll opens mini-game access outside of battle
        if chapter > 1:
            open_scroll = input("Open scroll for mini-games? (y/n): ").strip().lower()
            if open_scroll in ('y','yes'):
                print("📜 Scroll is open. Mini-games available now.")
                mini_game_bonus(player)
            else:
                print("📜 Scroll is closed. Continue to the chapter fight.")

        # Battle (starts after day 3 = chapter 3)
        if chapter < 3:
            print("🛡️ Training days: no dragon fight yet. Prepare for the beast.")
            victory = True
        else:
            victory = fight_dragon(player, chapter, difficulty=difficulty, narrator=narrator_on)
            while not victory:
                if narrator_on:
                    print("Narrator: \"Retrying the chapter...\"")
                player.gears = collect_gears()
                victory = fight_dragon(player, chapter, difficulty=difficulty, narrator=narrator_on)

        # 3-correct-answers-to-earn-a-digit-and-gear (up to 5 digits)
        if len(player.digits_collected) < 5:
            run_digit_streak(player, choice)

        # After having full password, unlock the machine
        if player.password_ready:
            unlocked = run_password_machine(player)
            if not unlocked:
                print("🔐 You must rebuild your password and try again next chapter.")

        # After chapter 1, mini-games are unlocked for extra gear
        if chapter > 1:
            wants = input("Do you want to play a mini-game for extra gear? (y/n): ").strip().lower()
            if wants in ('y','yes'):
                mini_game_bonus(player)

        time.sleep(0.5)
        
    print("\n🏆 The Book Is Now At Peace. You won the game!")
    restart = input("Play again? (y/n): ").strip().lower()
    if restart in ('y','yes'):
        game()
    else:
        print("📖 Thank you for playing!")

# --------------------------
# Start Game
# --------------------------
if __name__ == "__main__":
    game()