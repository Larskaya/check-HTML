data = [{'first_one': 7654}, {'one': ['a', 'b', 1, 'g', 'iy', 126, 'uytr', 'iy', 16, 'uytr', 12, 234, 'ouytt']}]
path = '1.on.11'

def find_new_value_in_DICT(el, data):
	new_data = ''
	keys = data.keys()
	for key in keys:	
		if el == key:
			new_data = data[el]
	return new_data

def find_new_value_in_LIST_or_STR_or_INT(key, data, numbers):
	new_data = ''
	print('key:', key)
	print('data:', data)
	if int(key) < len(data):
		new_data = data[int(key)]
	elif key in data:
		new_data = data[key]
	return new_data

def data_path(path, data):
	numbers = '0987654321'
	path = path.split('.')
	print(path)
	new_data = data

	counter = 0
	length = len(path)
	while counter < length:

		type_ = type(new_data)
		print('type:', type_)
		
		print('element PATH:', path[counter])

		int_path_counter = path[counter].isdigit()
		print('is digit -->', int_path_counter)
		if int_path_counter == True:
			print('IN IF')

			if len(new_data) < int(path[counter]):
				print('1111111')
				return None

			elif len(new_data) > int(int_path_counter):
				print('2222222')
				new_data = find_new_value_in_LIST_or_STR_or_INT(path[counter], new_data, numbers)

		else:
			print('IN ELSE')
			if 'list' in str(type_) and 'int' in str(type(path[counter])):
				print('3333333')
				return None

			elif 'dict' in str(type_):
				print('4444444')
				new_data = find_new_value_in_DICT(path[counter], new_data)

			elif 'list' in str(type_) or 'str' in str(type_):
				print('5555555')
				new_data = find_new_value_in_LIST_or_STR_or_INT(path[counter], new_data, numbers)
		print('new data', new_data)
		counter += 1

	return new_data

print(data_path(path, data))





