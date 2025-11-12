'''
백준이나 swea와 같은 온라인 채점 플랫폼에서는 사람이 직접 입력하는게 아닌
입력파일을 자동으로 프로그램에 파이프로 연결하여 실행하는 방식임

ex) python3 main.py < input.txt
input.txt:
apple
banana 

->
apple\nbanana\n<EOF>
이런 형식으로 받기 때문에 EOF를 만나면 EOF예외를 던지게 되면서 프로그램 종료

로컬환경(vscode)에서는 엔터를 치면 ""로 입력받기 때문에 ""를 만나면 종료 처리

'''

while True:
    try:
        s = input()
        s = s.strip().upper()
        print(">>", s)
    except EOFError:
        break
