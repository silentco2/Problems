def decode_morse(morse_code):
    list_code = morse_code.strip().split(" ")
    sentence = ""
    dict_morse = {".-": 65, "-...": 66, "-.-.": 67, "-..": 68, ".": 69, "..-.": 70, "--.": 71, "....": 72, "..": 73,
                  ".---": 74, "-.-": 75, ".-..": 76, "--": 77, "-.": 78, "---": 79, ".--.": 80, "--.-": 81,
                  ".-.": 82, "...": 83, "-": 84, "..-": 85, "...-": 86, ".--": 87, "-..-": 88, "-.--": 89,
                  "--..": 90, "-----": 48, ".----": 49, "..---": 50, "...--": 51, "....-": 52, ".....": 53,
                  "-....": 54, "--...": 55, "---..": 56, "----.": 57, '': 32, "...---...":[83,79,83],".-.-.-":46,"-.-.--":33}
    for i in range(len(list_code)):
        if dict_morse[list_code[i-1]]==dict_morse[list_code[i]]==32:
            continue
        elif list_code[i]=="...---...":
            x,y,z=dict_morse[list_code[i]]
            sentence+=chr(x) + chr(y) + chr(z)
        else:
            sentence += chr(dict_morse[list_code[i]])
    return sentence
