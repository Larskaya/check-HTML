#data = '<body class="rf">оара </body>'
#data = '<html> </html>'
def brute_force(data):
	all_indexes = []
	index = 0
	for el in data:
		if el == '<':
			all_indexes.append(index)
		elif el == '>':
			all_indexes.append(index)
		index += 1
	return all_indexes

def learn_tag(start_tag, end_tag, data):
	tag = ''
	counter = start_tag + 1
	while counter < end_tag and counter > start_tag:
		tag += data[counter]
		counter += 1
	return tag

def delete_excess(data):
	all_tags = []
	all_indexes = brute_force(data)
	for_cicle = len(all_indexes)/2
	counter = 0
	while for_cicle > counter:
		tag = learn_tag(all_indexes[0], all_indexes[1], data)
		del all_indexes[0]
		del all_indexes[0]

		all_tags.append(tag)
		counter += 1
	return all_tags

def replace_pairs(user_tags):
	tags_len = len(user_tags)
	a = 0
	while a < tags_len-1:
		open_tag = user_tags[a]
		close_tag = user_tags[a+1]
		if '/' + open_tag == close_tag:
		#if user_tags[a] in user_tags[a+1] and '/' in user_tags[a+1]:
			user_tags[a] = '-'
			user_tags[a+1] = '-'
		a += 1
	return user_tags

def compare_length(tags_before_clean):
	if len(tags_before_clean) == 0:
		return True
	return False

def delete_alone_tags(tags):
	counter = 0
	while counter < len(tags):
		if tags[counter][-1] == '/':
			del tags[counter]
			counter = 0
		counter += 1
	return tags

def delete_excess_symbols(tags):
	counter = 0
	while counter < len(tags):
		tag_before_split = tags[counter].split()
		if len(tag_before_split) > 1:
			tags[counter] = tag_before_split[0]
		counter += 1
	return tags

def delete_hyphens(tags):
	counter = 0
	while counter < len(tags):
		if tags[counter] == '-':
			del tags[counter]
			counter -= 1
		counter += 1
	return tags

def cicle(whithout_excess_symbols):
	length = len(whithout_excess_symbols)
	len_of_tags = []
	counter = 0
	number = 0
	while counter < length:
		tags_without_hyphens = replace_pairs(whithout_excess_symbols)
		whithout_excess_symbols = delete_hyphens(tags_without_hyphens)
		print(whithout_excess_symbols)

		if len(len_of_tags) > 0:
			number = len_of_tags[-1]

		len_of_tags.append(len(whithout_excess_symbols))

		if len_of_tags[-1] == number:
			break 
		counter += 1
	return whithout_excess_symbols

def check_double_tags(user_tags):
	tags_without_alone_tags = delete_alone_tags(user_tags)
	whithout_excess_symbols = delete_excess_symbols(tags_without_alone_tags)
	whithout_excess_symbols = cicle(whithout_excess_symbols)

	answer = compare_length(whithout_excess_symbols)
	return answer

#user_tags = delete_excess(data) 
#print(check_double_tags(user_tags))




