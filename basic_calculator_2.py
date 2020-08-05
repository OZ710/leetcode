import re
s = "42 * 2 + 16 - 3 / 2"
tokens = re.findall(r'\d+|\-|\+|\*|\/', s)

stack = []
symbol = '+'

for token in tokens:
	if token.isdigit():
		if symbol == '+':
			stack.append(int(token))
		elif symbol == '-':
			stack.append(-int(token))
		elif symbol == '*':
			stack.append(stack.pop() * int(token))
		else:
			stack.append(int(stack.pop() / float(token)))
	else:
		symbol = token
print(sum(stack))