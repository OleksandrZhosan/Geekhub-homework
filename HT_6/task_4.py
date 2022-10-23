morse_dict = { 'A':'.-', 'B':'-...', 'C':'-.-.',
             'D':'-..', 'E':'.', 'F':'..-.',
             'G':'--.', 'H':'....', 'I':'..', 
             'J':'.---', 'K':'-.-', 'L':'.-..', 
             'M':'--', 'N':'-.', 'O':'---', 
             'P':'.--.', 'Q':'--.-', 'R':'.-.', 
             'S':'...', 'T':'-', 'U':'..-', 
             'V':'...-', 'W':'.--', 'X':'-..-', 
             'Y':'-.--', 'Z':'--..', 'SOS': '...---...',
}

morse_code_reversed = {v: k for k, v in morse_dict.items()}

def decode(s):
    s = s.split('   ')
    result = ''
    for word in s:
        for letter in word.split():
            result += morse_code_reversed[letter]
        result += ' '    
    return result.strip()    
    
    
print(decode('--. . . -.- .... ..- -...   .. ...   .... . .-. .'))
print(decode('...---...'))