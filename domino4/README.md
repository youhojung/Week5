#domino4

led 4개를 각각 10, 11, 12, 13번 핀에 연결해 1초 간격으로 순서대로 키고 끄는 코드

**실행할 동작 요약**

![Image](https://github.com/user-attachments/assets/3165dd15-b477-462d-b338-b7615bd460d8)

**코드 전문**

#!/usr/bin/bash

for i in {10..13}; do 
	pinctrl set $i op
done

while true; do
	for i in {10..13}; do 
		pinctrl set $i dh
		sleep 1
		pinctrl set $i dl
	done
done

**코드 설명**

이 코드는 bash로 작성되었다.
GPIO 10번 핀부터 GPIO 13번 핀까지 출력으로 설정한다.
무한히 반복하기 위해 while true를 사용한다.
i는 10부터 13까지의 상수이다.
i번 핀을 high로 설정하고, sleep 1을 사용해 1초 딜레이를 준다.
i번 핀을 low로 설정하고, 다음 i로 넘어간다.
이를 실행하면, LED가 1초간 켜져있다가 꺼지고, 다음 LED가 1초간 켜지는 것을 무한히 반복한다.

**동작 시연**

[https://youtube.com/shorts/4cBCcszGSww]

**회로 사진**

![Image](https://github.com/user-attachments/assets/a2bc791f-239e-44dc-929b-8c2fac604d96)