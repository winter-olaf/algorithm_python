T = 10

for tc in range(1, T+1):
    N = int(input())
    pw = list(input().split())
    C = int(input())
    command = []
    data = input().split('I')
    for i in data[1:]:
        command.append(i.strip())

    for i in command:
        np = i.split()
        idx = int(np[0])
        pw = pw[:idx] + np[2:] + pw[idx:]

    print('#{}'.format(tc), *pw[:10])

'''
11
449047 855428 425117 532416 358612 929816 313459 311433 472478 589139 568205
7
I 1 5 400905 139831 966064 336948 119288 I 8 6 436704 702451 762737 557561 810021 771706 I 3 8 389953 706628 552108 238749 661021 498160 493414 377808 I 13 4 237017 301569 243869 252994 I 3 4 408347 618608 822798 370982 I 8 2 424216 356268 I 4 10 512816 992679 693002 835918 768525 949227 628969 521945 839380 479976
'''