class Cal
  def initialize(v1,v2)
    @v1 = v1
    @v2 = v2
  end
  def add()
    return @v1+@v2
  end
  def subtract()
    return @v1-@v2
  end
end
c1 = Cal.new(10,10)
# 인스턴스를 생성할때 제일먼저
# 이니셜라이즈 메소드를 자동으로 사용하도록약속

p c1.add()
p c1.subtract()

c2 = Cal.new(30,20)

p c2.add()
p c2.subtract()
#c1,c2는 인스턴스 v1,v2 인스턴스 변수
