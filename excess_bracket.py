all_brackets = '<>()[]'
user_data = '<(12(3)4)()[567]8>9()'

# если открывающихся скобок больше вернуть false
# (лишняя скобка)
def excess_bracket(user_data):
	open_trigon_brackets = 0
	open_round_brackets = 0
	open_square_brackets = 0
	open_brace = 0

	close_trigon_brackets = 0
	close_round_brackets = 0
	close_square_brackets = 0
	close_brace = 0

	for el in user_data:
		if el == '<':
			open_trigon_brackets += 1
		elif el == '(':
			open_round_brackets += 1
		elif el == '[':
			open_square_brackets += 1
		elif el == '{':
			open_brace += 1

		elif el == '>':
			close_trigon_brackets += 1
		elif el == ')':
			close_round_brackets += 1
		elif el == ']':
			close_square_brackets += 1
		elif el == '}':
			close_brace += 1

	all_open_brackets = open_trigon_brackets + open_round_brackets + open_square_brackets + open_brace
	all_close_brackets = close_trigon_brackets + close_round_brackets + close_square_brackets + close_brace
		
	return all_open_brackets, all_close_brackets

# удалить рядом стоящие парные скобки
def find_nearby_pairs_of_brackets(user_data):
	counter = 0
	while counter < len(user_data):
		if user_data[counter] == '<' and user_data[counter+1] == '>':
			del user_data[counter]
			del user_data[counter]
			counter = 0
		elif user_data[counter] == '(' and user_data[counter+1] == ')':
			del user_data[counter]
			del user_data[counter]
			counter = 0
		elif user_data[counter] == '{' and user_data[counter+1] == '}':
			del user_data[counter]
			del user_data[counter]
			counter = 0
		elif user_data[counter] == '[' and user_data[counter+1] == ']':
			del user_data[counter]
			del user_data[counter]
			counter = 0
		counter += 1 

	return user_data

def main_function(user_data):
	print(user_data)
	# узнать равное ли кол-во отк. и зкт. скобок 
	excess = excess_bracket(user_data)
	remaining = ''
	# оставшиеся скобки после удаление парных и рядом стоящих скобок
	remaining_brackets = find_nearby_pairs_of_brackets(list(user_data))
	print(remaining_brackets, 'remaining brackets STRING')

	counter = 0
	while counter < len(remaining_brackets):
		el = remaining_brackets[counter]

		if el not in all_brackets:
			#print('elem -->', el)
			remaining_brackets.remove(el)
			counter -= 1
		counter += 1
	print(remaining_brackets)

	remaining = remaining_brackets
	open_brackets = excess[0]
	counter = 0
	while counter < open_brackets:
		remaining = find_nearby_pairs_of_brackets(remaining)
		counter += 1

	print(len(remaining), 'lenght')
	if len(remaining) != 0:
		return False
	return True

print(main_function(user_data))





