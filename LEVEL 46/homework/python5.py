# შექმენით ფუნქცია რომელიც გააქრობს დუპლიკატებს string'იდან (გამოიყენეთ set())


def remove_duplicates_preserve_order(input_string):
    seen = set()
    result = []
    for char in input_string:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)


string_with_duplicates = "hello world"
result = remove_duplicates_preserve_order(string_with_duplicates)
print(result)  
