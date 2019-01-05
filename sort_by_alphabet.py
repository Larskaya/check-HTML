alph='abcde'
user_data=':c@ea@#2a:/1'
numbers='0987654321'
symbols='-:/@%$#&'

def find_the_same_letters(user_data,answer):
	lenght_of_user_data=len(user_data)
	for letter in alph:
		for el in user_data:
			if el==letter:
				answer+=el
				if el in user_data:
					user_data.remove(el)
	return answer

def find_all_numbers(user_data):
	nums_in_user_data=''
	for num in numbers:
		for el in user_data:
			if el==num:
				nums_in_user_data+=num
				user_data.remove(num)
	return nums_in_user_data

def find_spec_symbols(user_data):
	symbols_in_user_data = ''
	print(user_data,'-------user data')
	for el in user_data:
		print('el:', el)

		for sym in symbols:
			if el==sym:
				symbols_in_user_data += sym
				print('   add sym:', sym)
	return symbols_in_user_data

def find_the_fewer(nums_in_user_data,answer):
	for num in nums_in_user_data:
		el=max(nums_in_user_data)
		nums_in_user_data=list(nums_in_user_data)
		nums_in_user_data.remove(el)
		answer=el+answer
	return answer

def sort_by_alph(user_data):
	answer=''
	user_data=list(user_data)

	answer=find_the_same_letters(user_data,answer)
	nums_in_user_data=find_all_numbers(user_data)

	if len(nums_in_user_data)>0:
		answer=find_the_fewer(nums_in_user_data,answer)

	symbols_in_user_data=find_spec_symbols(user_data)
	print(symbols_in_user_data,'symbols')

	answer=symbols_in_user_data+answer
	return answer

print('answer:', sort_by_alph(user_data))
