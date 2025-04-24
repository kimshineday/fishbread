#주문, 관리자, 종료 이 3가지 선택을 통해서 각각 기능이 작동되도록 만들거예요
#input()을 통해서 3가지 중 한가지를 입력받아서 작동시킬 수가 있어요

stock = {   #key값을 이용해서 value  딕셔너리를 써야하는 상황은 어떤 스토리 기반으로 데이터가 구성되었을때 
    "팥붕어빵": 10,
    "슈크림붕어빵" : 8,
    "초코붕어빵" : 5
}

sales = {
    "팥붕어빵": 0,
    "슈크림붕어빵" : 0,
    "초코붕어빵" : 0
}

price = {
    "팥붕어빵" : 1000,
    "슈크림붕어빵" : 1200,
    "초코붕어빵" : 1500
}

def order_bread():
    while True:    
        bread_type = input("주문할 붕어빵을 선택하세요(팥붕어빵, 슈크림붕어빵, 초코붕어빵) 만약 뒤로가길 원하시면 뒤로가기를 입력해주세요: ")
        if bread_type == "뒤로가기":
            break
        if bread_type in stock:
            bread_count = int(input("주문할 개수를 입력하세요: ")) #8
            if  stock[bread_type] >= bread_count:
                stock[bread_type] -= bread_count
                sales[bread_type] += bread_count
                print(f"{bread_type} {bread_count}개가 판매되었습니다.")
            else:
                print(f"재고가 부족합니다. 현재 {stock[bread_type]}개만 주문 가능합니다.")
        else:
            print("정신을 똑바로 차리시고 주문을 다시해주세요👺")

def admin_mode():
    while True:
        bread_type = input("추가할 붕어빵 종류를 입력하세요 (팥붕어빵, 슈크림붕어빵, 초코붕어빵) 또는 '종료' 입력: ")
        if bread_type == "종료":
            break
        if bread_type in stock:
            bread_count = int(input("추가할 개수를 입력하세요: "))
            stock[bread_type] += bread_count
            print(f"{bread_type}의 재고가 {bread_count}개 추가되어 현재 {stock[bread_type]}개 입니다.")
        else:
            print("올바른 메뉴를 입력하세요.")

def calculate_sales():
    # total_sales = sum(sales[key] * price[key] for key in sales)
    total = 0
    for key in sales:
        # total = total + (sales[key] * price[key])
        total +=(sales[key] * price[key])
    print(f"오늘의 총 매출은 {total}원 입니다.")

while True:
    mode = input("원하는 모드를 선택하세요(주문, 관리자, 종료): ") #주문
    #mode = "종료"
    if mode == "종료":
        calculate_sales()
        print("시스템을 종료합니다.")
        break
    elif mode == "주문":
        order_bread()
    elif mode == "관리자":
        admin_mode()

