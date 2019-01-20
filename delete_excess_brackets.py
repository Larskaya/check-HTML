user_data = '<html> <body> </body> <html> <html> <body> </html>'
user_data = user_data.split()

alone_tag = '<img>'

def delete_alone_tag(user_data):
	counter = 0
	while counter < len(user_data):
		if user_data[counter] == alone_tag:
			del user_data[counter]
		counter += 1
	print(user_data)
	return user_data

def find_nesting(without_unnecessary_tags):
	nesting = 0
	counter_of_reset = 0
	all_nesting = []
	for tag in without_unnecessary_tags:
		if '/' not in tag:
			nesting += 1
			all_nesting.append(nesting)
		else:
			counter_of_reset += 1
			nesting = 0
	print('all nestings', all_nesting)
	max_nesting = max(all_nesting)
	print(max_nesting, 'max nesting')
	return max_nesting, counter_of_reset

def list_of_el_for_nesting(user_data, max_nesting, reset_nesting):
	el_for_max_nesting = []
	counter = 0
	print(reset_nesting)
	while counter < len(user_data):
		#print(counter, '--count')
		if reset_nesting < counter:
			el_for_max_nesting.append(user_data[counter])
		counter += 1

	return el_for_max_nesting

def tags_are_correct(user_data):
	without_unnecessary_tags = delete_alone_tag(user_data)
	max_nesting_and_reset = find_nesting(without_unnecessary_tags)
	max_nesting = max_nesting_and_reset[0]
	reset = max_nesting_and_reset[1]
	el_after_close_tag = list_of_el_for_nesting(without_unnecessary_tags, reset, max_nesting)
	print(el_after_close_tag)
	return False

print(tags_are_correct(user_data))
















