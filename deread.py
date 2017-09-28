import sys

def decrypt(chars):
    numbers = chars.split()
    numvalues = {}
    i = 28
    new_string = ""
    
    numvalues = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", ",",".","/", "(", ")", ":","?","\n", "!","-","'"]
         
    for char in numbers:
        if char.isalnum():
            char = int(char)/52
            new_string += str(numvalues[int(char)])
        
    return new_string
    
def main():
    filename = sys.argv[1]
    with open(filename, "r+") as f:
        txt = f.read()
        
        print (decrypt(txt))
        
if __name__ == "__main__":
    main()
    

