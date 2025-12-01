import unicodedata
from typing import List

HANGMAN_PICS: List[str] = [
r"""  
  _______
 |/      
 |       
 |       
 |        
 |       
_|___
""",
r"""
  _______
 |/      |
 |       
 |       
 |        
 |       
_|___
""",
r"""
  _______
 |/      |
 |      (_)
 |       
 |        
 |       
_|___
""",
r"""
  _______
 |/      |
 |      (_)
 |       |
 |       |
 |       
_|___
""",
r"""
  _______
 |/      |
 |      (_)
 |      \|
 |       |
 |       
_|___
""",
r"""
  _______
 |/      |
 |      (_)
 |      \|/
 |       |
 |       
_|___
""",
r"""
  _______
 |/      |
 |      (_)
 |      \|/
 |       |
 |      / \
_|___

"""
]

def chose_hangman_stage(attemps_left: int, max_attempts: int) -> str:
    """
    Mapeia a quantidade de erros para um índice dentro de HANGMAN_PICS.
    Funciona proporcionalmente mesmo se max_attempts != len(HANGMAN_PICS)-1.
    """
    try:
        max_attempts = max(1, int(max_attempts))
        attemps_left = max(0, int(attemps_left))
    except Exception:
        return HANGMAN_PICS[0]
    
    errors = max_attempts - attemps_left
    max_attempts - attemps_left
    max_errors = len(HANGMAN_PICS) - 1 

    if max_attempts == 0:
        index = 0
    else:
        index = round((errors / max_attempts) * max_attempts)
        index = min(max_errors, max(0, index))

    return HANGMAN_PICS[index]