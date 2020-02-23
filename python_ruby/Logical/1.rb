puts("아이디를 입력하세요.")
input_id = gets.chomp()

puts("비밀번호를 입력하세요.")
input_pw = gets.chomp()

real_id = "egoing"
real_pw = "1111"

if real_id == input_id
  if real_pw == input_pw
    puts("hello, egoing")
  elsif
    puts("wrong password")
  end
else
  puts("wrong ID")
end
