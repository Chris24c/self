import sys

def encrypt(chars):
    words = list(chars)
    numvalues = {}
    i = 0
    new_string = ""
    
    for letter in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", ",",".","/", "(", ")", ":","?","\n", "!","-","'"]:
        numvalues[letter] = i
        i += 1
        
    for char in words:
        if char.isalpha():
            char = char.lower()
        if char in numvalues:
            new_string += str(int(numvalues[char]) * 52) + " "
        elif char.isalnum():
            new_string += char
    
    return new_string
    
def main():
    filename = sys.argv[1]
    with open(filename, "r+") as f:
        txt = f.read()
        
    open(filename, 'w').close()
    with open(filename, "r+") as f:
        f.write("" + encrypt(txt))
        
    print (encrypt(txt))
    
if __name__ == "__main__":
    main()
    

