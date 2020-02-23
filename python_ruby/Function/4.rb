puts("아이디를 입력하세요.")
input_id = gets.chomp()

def login(_id)
    members = ['egoing','krsc0707','kiddo']
    for member in members do
      if member == _id
        return true
    end
  end
  return false
end

if login(input_id)
  puts("Hi ! " + input_id)
else
  puts('who are you?')
end
