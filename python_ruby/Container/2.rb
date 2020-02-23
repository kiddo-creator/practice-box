al = ['A', 'B', 'C', 'D']
puts(al.length) #4

al.push('E') # 배열의 마지막에 'E' 추가
print(al) # ['A', 'B', 'C', 'D','E']

puts()

al.delete_at(0) #배열 삭제 메서드
print(al) #['B','C','D','E']
