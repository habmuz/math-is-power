# 📖 Math Is Power

A browser-based maths adventure game for Primary 1 to Primary 3 students. Players read through a magical book, answer maths questions, collect gears, battle a dragon, and unlock fun mini games as rewards.

**Made by:** Nazmin and Thiyazhini

---

## 🗺️ How the Game Works (Big Picture)

The game is shaped like a book. There are **10 chapters**, one for each maths topic. To finish a chapter, the player must:

1. **Answer 3 questions** → earn a gear
2. **Collect 3 gears** → the left strip of the book glows
3. **Flip the page** → face the Dragon
4. **Beat the Dragon** → enter the Password Machine
5. **Enter the password** → chapter complete! 🎉

Then the next chapter begins.

---

## 📚 The 10 Chapters

| Chapter | Topic |
|---------|-------|
| 1 | Addition (no carrying) |
| 2 | Subtraction (no borrowing) |
| 3 | Multiplication — ×2, ×5, ×10 |
| 4 | Division — ÷2, ÷1 |
| 5 | Addition with carrying |
| 6 | Subtraction with borrowing |
| 7 | Multiplication — ×2, ×4, ×6, ×8 |
| 8 | Division — ÷3, ÷1 |
| 9 | Mixed operations |
| 10 | All operations + patterns |

---

## 🎚️ Difficulty Levels

At any time, players can change their level in the **Bookmark menu** (top-right blue tab):

- **P1** — smallest numbers, easiest
- **P2** — medium numbers
- **P3** — harder numbers

The type of maths stays the same — only the size of the numbers changes.

---

## ⚙️ Gears — How They Work

After every set of 3 questions, the player earns a gear based on how many they got right:

| Score | Gear Earned |
|-------|-------------|
| 3 / 3 | ⚔️ Type 3 (strongest) |
| 2 / 3 | 🛡️ Type 2 |
| 1 / 3 | 💡 Type 1 |
| 0 / 3 | No gear |

Players need **3 gears** to unlock the Dragon Battle. The gears they collect affect how they fight the dragon.

---

## 🐉 Dragon Battle

Once 3 gears are collected, the player can flip the page and fight **Dralioster the Dragon**.

- ⚔️ **Attack** — deal damage to the dragon
- 🛡️ **Defend** — reduce damage taken
- ❤️ **Heal** — restore your health (limited uses)

Equipped gears give special powers during battle. Win the battle → unlock the Password Machine.

---

## 🔐 Password Machine

After the Dragon Battle, a password machine appears. The password digits were earned during the question rounds. Type the correct password to complete the chapter.

---

## 🔖 Bookmark Menu

The blue bookmark tab (top-right of the book) gives quick access to:

| Option | What it does |
|--------|-------------|
| Your Name | Set or change your player name |
| Level | Switch between P1, P2, P3 |
| Narrator | Turn hints ON or OFF |
| Page Flip | Manual (you click) or Auto (flips itself) |
| Mini Games | Opens the Mini Game World Map |
| Gear Base | See all gears collected across every chapter |
| How to Play | Full instructions |
| Tokens | See how many tokens you have |
| Reset Chapter | Redo the current chapter from scratch |
| Admin | Admin-only controls |
| Invite Friend | Start online multiplayer |
| Color Dash MP | Launch Color Dash for 2–5 players |

---

## 🪙 Tokens & Mini Games

- Earn **5 tokens** every time you complete a chapter
- Chapter 9 gives **20 tokens** as a bonus!
- Tokens unlock after completing Chapter 1
- Spend **1 token** to enter a Mini Game

Mini games are on the **Mini Game World Map** (open from the bookmark).

---

## 🎮 Mini Games

### 🌋 Lava Ruins
React fast and answer questions before the lava rises. Get it wrong and the lava gets closer!

### 🏃 Obstacle Park
Run and jump through obstacles. Answer correctly to keep going.

### 🧟 Zombie Temple
The temple is overrun — survive the zombie curse by answering questions.

### 🎨 Color Dash *(Solo)*
10 coloured tiles appear on screen. An announcer voice shouts a colour — step on that colour before the timer runs out! Wrong colour = you fall off. Survive all **50 rounds** to win.

- Use **arrow keys** to move (or swipe on mobile)
- The timer gets shorter every round
- Round 50 is the hardest!

---

## 🎨 Color Dash Multiplayer (2–5 Players)

Same as Color Dash solo, but everyone plays together on **one screen**.

**How to start:**
- Press **"Color Dash Multiplayer"** on the intro page, or
- Open the **Bookmark → Color Dash 2-5P**

**Controls (each player uses different keys):**

| Player | Keys |
|--------|------|
| P1 | W A S D |
| P2 | Arrow Keys |
| P3 | I J K L |
| P4 | T F G H |
| P5 | Numpad 8 4 5 6 |

**Rules:**
- Everyone moves to the announced colour tile before time runs out
- Wrong colour = fall and lose that round
- Rounds 1–49: eliminated players come back next round
- **Round 50:** if you fall, you're out for good
- 1 point per round survived
- After Round 50 → **Winners Podium** 🥇🥈🥉

---

## 🧩 Solo Player vs Play with Friend

### Solo Player
Play alone. Pick your hero character, answer questions, and face the dragon yourself.

### Play with Friend
Connect with a friend on another device using a code. Both players answer together and fight the dragon as a team.

---

## 💾 Saving Progress

The game saves automatically after each chapter is completed. When you come back, press **"Continue Adventure"** to pick up where you left off.

---

## 🏠 Gear Base

The Gear Base shows **every gear collected** across all 10 chapters. Access it from:
- The intro page button
- The bookmark menu → Gear Base

---

## 🗂️ Project Files

| File | What it is |
|------|-----------|
| `index.html` | Main game (the book) |
| `battle.html` | Dragon battle screen |
| `color-dash.html` | Color Dash solo mini game |
| `color-dash-mp.html` | Color Dash multiplayer (2–5 players) |
| `lava-ruins.html` | Lava Ruins mini game |
| `obstacle-park.html` | Obstacle Park mini game |
| `zombie-outbreak.html` | Zombie Temple mini game |
| `chars/` | Character portrait images |
| `gears/` | Gear images |
| `dragon-normal.png` | Dragon sprite (normal) |
| `dragon-hurt.jpg` | Dragon sprite (hurt) |
| `cave-bg.webp` | Cave background for battle scene |
