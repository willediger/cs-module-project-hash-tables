def word_count(s):
    # Your code here
    escaped = ['\r', '\n', '\t']
    characters = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
    new_string = s.lower()
    
    for e in escaped:
        new_string = new_string.replace(e, ' ')
    
    for c in characters:
        new_string = new_string.replace(c, ' ')
    
    words = new_string.split(' ')

    word_dist = {}
    for word in words:
        if word in word_dist:
            word_dist[word] += 1
        else:
            word_dist[word] = 1

    word_dist.pop('', None)

    return word_dist



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("  Hello  "))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))