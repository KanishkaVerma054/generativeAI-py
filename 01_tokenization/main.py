import tiktoken

# enc = encoder
enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey There!, My name is Kanishk Verma"
tokens = enc.encode(text)

print("Tokens: ", tokens)

decoded = enc.decode([25216, 3274, 27942, 3673, 1308, 382, 658, 17145, 74, 3852, 809])

print("decoded: ", decoded)