data = '<body>оара</body>'

def add_space(data):
	counter = 0
	change_data = ''
	while counter < len(data)-1:
		if data[counter] == '>' and data[counter+1] == '<':
			change_data += '> '
		else:
			change_data += data[counter]
		counter += 1
	change_data += data[-1]
	print(change_data, 'change data')

	change_data = change_data.split()
	return change_data

all_tags = ['<body>', '<html>', '<p>', '</body>', '</html>', '</p>']
need_simbols = '<>/bodyhtmlp'

def delete_alone_tag_and_excess_symbols(user_data):
	counter = 0
	user_data = user_data.split()
	while counter < len(user_data):
		#print('	element in user_data --->', user_data[counter])
		a = 0
		while a < len(user_data[counter]):
			print('el in el -->', user_data[counter][a])
			if user_data[counter][a] not in need_simbols:
				print('del', user_data[counter][a])
				del user_data[counter][a]
				a = 0
			a += 1
		counter += 1
		print(user_data, 'user data before clean')
		return user_data

def delete_pairs_tags(user_data, tag):
	close_tag = ''
	counter = 0
	while counter < len(user_data)-1:
		if tag in user_data[counter] and tag in user_data[counter+1]:
			if '/' not in user_data[counter] and '/' in user_data[counter+1]:
				user_data[counter] = '-'
				user_data[counter+1] = '-'

				counter -= 1
		counter += 1
	return user_data

def delete_brackets(tag):
	counter = 0
	change_tag = ''
	while counter < len(tag):
		if tag[counter] != '<' and tag[counter] != '>':
			change_tag += tag[counter]
		counter += 1
	return change_tag

def empty_string(user_data):
	counter = 0
	for el in user_data:
		if el == '-':
			counter += 1
	if counter == len(user_data):
		return True
	return False

def delete_tag(user_data):
	clean_data = delete_alone_tag_and_excess_symbols(user_data)
	without_spaces = add_space(clean_data)
	print('user_data without spaces', without_spaces)
	counter = 0
	while counter < len(without_spaces):
		if '/' not in without_spaces[counter]:
			tag_name = delete_brackets(without_spaces[counter])
			print('name of tag -->', tag_name)
			without_spaces = delete_pairs_tags(without_spaces, tag_name)
		counter += 1

	answer = empty_string(clean_data)
	return answer

print(delete_tag(data))





