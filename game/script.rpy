# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.)
define ne = Character("유나은", color="#f7b1cb")
define so = Character("???", color="#214bac")
define bb = Character("브리엔츠 보이", color="#214bac")

define na = Character(None)
define narrator = Character(None, kind=nvl)


init -999:
    $ main_point = 3
    $ sub_point = 1
    $ minus_point = -1

    $ healthy = 0  # 건강
    $ happy = 0    # 행복
    $ funny = 0    # 재미
    $ money = 0    # 금전


# 여기에서부터 게임이 시작합니다.
label start:

    ## prologue ##

    nvl clear
    "반복되고 지루한 회사일에 찌든 유나은.."
    "오늘도 어김없이 회사를 출근하며 피곤한 삶을 살아간다 ㅠㅠ"
    "지금은 너무나도 힐링이 필요한 시간..!"
    "그렇게 몇일을 보내던 어느 날"
    "누군가에게 인스타 DM이 하나 왔는데.."

    
    so "(인스타 디엠 받는 이미지) 당신을 프위스로 초대합니다!" with fade

    ne "엥? 누구지..?"
    ne "누가 보낸건진 모르겠지만.."
    ne "프위스?!?!" with vpunch
    ne "대박이잖아~!~!"
    ne "금방이라도 가고 싶은걸~? ㅎㅎ"
    ne "언제 출발인거지??"
    ne "헉..! 당장 다음주잖아!! ㅎㅁㅎ" with hpunch
    ne "어여 짐도 싸고 준비도 하고,, 가족들이랑 친구들한테도 말해두어야 하고,, 아 맞다! 회사도 휴가 써야하는데,,\n..."
    ne "이럴 때가 아니지! 일단 뭐라도 해보자!!"
    
    menu:
        "금강산도 식후경! 일단은 밥이라도 먹으며 흥분을 가라앉히자":
            $ healthy += main_point
            ne "역시 밥을 먹으니 진정이되네 ㅎㅎ"
        "짐부터 챙겨둘까? 프위스 가서 뭐 입지~? 흐흐":
            $ happy += main_point
            ne "하루에 2벌씩 갈아 입어야 하니 가득가득! ^^"
        "우선? 가족들이랑 친구들한테 자랑해야지~!~! ㅋㅋㅋ":
            $ funny += main_point
            ne "엄마~~~ 나 프위스 간다~~~"
        "비행기표랑 숙소는 제공해준다고 했으니, 여행 경비 준비랑 환전좀 해야하나?":
            $ money += main_point
            ne "이정도만 바꿔두면 되겠다! 다행히 돈은 충분한 것 같네"
    
    na "(이것저것 준비를 마친뒤)" with fade
    ne "오케이~ 좋았어!!"
    ne "벌써부터 여행이 기다려지는군 ㅎ"
    ne "(현재 상태 => 건강: [healthy], 행복: [happy], 재미: [funny], 금전: [money])"


    nvl clear
    "유나은은 그렇게 들뜬 마음으로 DM을 보며 여행갈 상상에 빠진다"
    "그렇게 몇일이 지나 드디어 다가온 여행 당일!"
    "유나은의 좌충우돌 7일간의 프위스 여행이 시작된다!!!"


    ## Day 1 ##

    $ renpy.notify("프위스 여행 1일차")
    
    na "(공항에 도착한 유나은)" with fade
    ne "드디어 이 날이 오는구나!!"
    ne "크으~ 몇일 안됐는데도 벌써 설렌다 ㅎㅎ 프위스 여행이라니"
    ne "아차! 이제 곧 비행기 탈 시간인데..!!"
    ne "서둘러 출발해야겠다!"
    ne "음 어디보자 내가 탈 비행기 몇 번 게이트지?"

    menu:
        "Gate 1 (뭐든지 1이 최고야 ><)":
            $ money += main_point
        "Gate 2 (나는 뭔가 2가 좋더라~)":
            $ funny += main_point
        "Gate 7 (행복 가득 7번!!)":
            $ happy += main_point
        "Gate 8 (조랭이떡 같이 생긴게 맛나보여 ㅎㅎ)":
            $ healthy += main_point
    
    ne "휴 다행이다~ 바로 앞 게이트였구나 ㅎㅎ"
    ne "늦기 전에 얼른 들어가쟝~~"
    ne "(현재 상태 => 건강: [healthy], 행복: [happy], 재미: [funny], 금전: [money])"

    return
