domino4

led 3개를 이용해 0부터 7까지를 이진수로 나타내는 코드

**실행할 동작 요약**

![Image](https://github.com/user-attachments/assets/3309b5c4-aa34-4db8-8aeb-7875ffc2efc6)

**코드 전문**

#!/usr/bin/bash
for i in {10..12}; do
	pinctrl set $i op
	pinctrl set $i dl
done
while true; do
	for j in {0..7}; do
		k=$((  (j>>0) & 1 ))
		m=$((  (j>>1) & 1 ))
		n=$((  (j>>2) & 1 ))

		if [ "$k" -eq 1 ]; then
			pinctrl set 12 dh
		else
			pinctrl set 12 dl
		fi
		if [ "$m" -eq 1 ]; then
			pinctrl set 11 dh
		else
			pinctrl set 11 dl
		fi
		if [ "$n" -eq 1 ]; then
			pinctrl set 10 dh
		else
			pinctrl set 10 dl
		fi
		sleep 1
	done
done

**코드 설명**

이 코드는 bash로 작성되었다.
GPIO 10번 핀부터 GPIO 12번 핀까지 출력으로 설정하고, dl 상태로 두어 LED를 끈 상태로 시작한다.
무한히 반복하기 위해 while true를 사용한다.
k는 2^0, m은 2^1, n은 2^2의 비트값을 저장한다.
k가 1이면 12번 핀을 high로, 0이면 low로 설정한다.
m가 1이면 11번 핀을 high로, 0이면 low로 설정한다.
n가 1이면 10번 핀을 high로, 0이면 low로 설정한다.
high인 핀에 연결된 LED는 불이 들어올 것이고, low인 핀에 연결된 LED는 불이 꺼질 것이다.
sleep1을 통해, i값이 변할 때 1초의 딜레이를 준다.

**동작 시연**

[https://youtube.com/shorts/fahEarMhVDQ]

**회로 사진**

![Image](https://github.com/user-attachments/assets/1ece78fb-0a37-4774-b68d-114928570e51)
