class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0
        secret = list(secret)
        guess = list(guess)

        for i in range(len(guess)):
            if secret[i] == guess[i]:
                bulls += 1
                secret[i] = guess[i] = -1
        
        for s, g in zip(secret, guess):
            if g != -1 and g in secret:
                match = secret.index(g)
                cows += 1
                secret[match] = ''

        return f"{bulls}A{cows}B"