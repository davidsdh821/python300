string = 'abcd'
string.replace('b', 'B');
print(string);

#abcd가 그대로 출력
#replace 메서드를 사용하면 원본은 그대로 둔채로 변경된 새로운 문자열 객체를 리턴해줍니다.
#하지만 앞에 따로 선언을 안하면 그냥 그대로다 기존에 있는거를 바꾸지 않기 때문이다.