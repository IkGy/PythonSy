i = 0

while True:
    print("{}번째 반복중입니다.".format(i));
    i += 1;

    endInput = input("종료하시겠습니까? (Y)")
    if endInput in ['y',"Y"]:
        print("종료")
        break;
