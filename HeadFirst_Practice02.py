movies = ["THe Holy Grail", "The Life of Brian",["Fall in love", "Wind"], "The Meaning of LIfe"]
for each_item in movies:
	if isinstance(each_item, list): #list�� ��� ����~
		for	nested_item in each_item: #list�ϰ�쿡�� ���.
			print(nested_item)#�ϳ��� ����Ǹ鼭 ��µ�.
	else: #list�ƴϸ� for������ ���.
		print(each_item)

print(movies) #�׳� print�ϸ� [] ���� �׳� �ϴ� ��µ�