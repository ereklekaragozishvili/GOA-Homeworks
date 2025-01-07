# 2) გააკეთეთ manual_replace ფუნქცია

def manual_replace(text, old, new):
    result = ""
    i = 0
    while i < len(text):
        if text[i:i+len(old)] == old:
            result += new
            i += len(old)  
        else:
            result += text[i]
            i += 1
    return result
