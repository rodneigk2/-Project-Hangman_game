
def create_state(word, max_attempts=6):
    return {
    "word": word,
    "lines": ["_"] * len(word),
    "wrong": [],  
    "attempts": max_attempts
}


def process_guess(state, letter):
    letter = letter.lower().strip()

    if not letter:
        return "Empty"
    
    if len(letter) != 1:
        return "Enter only one letter"
    
    if not letter.isalpha():
        return "Enter only letters"
    
    if letter in state["wrong"] or letter in state["lines"]:
        return "Repeated Entry"
    
    hit = False
    for i, ch in enumerate(state["word"]):
        if ch == letter:
            state["lines"][i] = ch
            hit = True

    if not hit:
        state["attempts"] -= 1
        state["wrong"].append(letter)

    if "_" not in state["lines"]:
        return "You win"
    
    if state["attempts"] <= 0:
        return "You lose"

    return "hit" if hit else "miss"

