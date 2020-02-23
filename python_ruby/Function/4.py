input_id = input('아이디를 입력하세요.')

def login(_id):
    members = ['egoing', 'kiddo', 'krsc0707']
    for member in members:
        if member == _id:
            return True
    return False

if login(input_id):
    print("Hi," + input_id)
else:
    print('who are you')
