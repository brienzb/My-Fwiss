﻿# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.)
define ne = Character("유나은", color="#f7b1cb")
define so = Character("???", color="#214bac")
define bb = Character("동해", color="#214bac")

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
    $ hidden = 0   # 히든 포인트 (특정 점수 이상이면 히든 엔딩)

    $ choice_word = ""


# 여기에서부터 게임이 시작합니다.
label start:

    ## prologue ##

    nvl clear
    "반복되고 지루한 회사일에 찌든 유나은.."
    "오늘도 어김없이 회사를 출근하며 피곤한 삶을 살아간다 ㅠㅠ"
    "지금은 너무나도 힐링이 필요한 시간..!"
    "그렇게 몇일을 보내던 어느 날"
    "누군가에게 인스타 DM이 하나 왔는데.."

    # image: 라인 회사 배경
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
    
    # image: 공항 사진
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

    # image: 비행기 내부 안 사잔
    na "(비행기 좌석에 탑승한 뒤)" with fade
    ne "읏차~! 좌석 탑승 완료!!"
    ne "히히 오랜만에 타는 비행기라 그러는지 좀 떨리는데?"
    ne "음.. 어디보자 예정 비행 시간은.."
    ne "12시간!!!!!" with vpunch
    ne "뭐 ㅎ.. 사실 어느정도 예상하긴 했지만 ㅎㅎ;;"
    ne "그러면 이 지루한 비행 시간을 달랠 무언가가 필요하겠지?"
    ne "내가 준비한 것은 바로..."

    menu:
        "최고의 안대와 최고의 목베게!!":
            $ healthy += main_point
            ne "흐흐 이것만 있으면 꿀잠 예약이라구~ ><"
        "짜자잔! 미리 다운 받아놓은 루미큐브~":
            $ funny += main_point
            ne "한 판에 30분 정도한다 치면 24번만 하면 도착 ㅋㅋ"
        "역시 영화지!! 영화는 <라따뚜이>":
            $ happy += main_point
            $ hidden += sub_point
            ne "역시 이 영화는 언제봐도 재밌어 ㅎㅎ"
        "전자책~!~! 평소 보고 싶었던 것들도 잔뜩 다운 받아놨다!":
            $ money += main_point
            ne "비행기에서 책 읽는 나란 여자~ 교양이 쌓이는 기분이군 ㅎ"

    na "(그렇게 몇분이 지나다 자게된 유나은..)" with fade
    ne "흠냐 흠냐"
    ne "음.. 얼만큼 왔지..??"
    ne "엥?? 착륙까지 벌써 1시간 밖에 안남았네!!!" with hpunch
    ne "나.. 도대체 얼마나 잔걸까..?? 🤔"
    ne "암튼 곧 도착이니! 얼른 내릴 준비를 하자!"
    ne "(현재 상태 => 건강: [healthy], 행복: [happy], 재미: [funny], 금전: [money])"

    nvl clear
    "아- 아- 레이디스 앤 젠틀맨 디스 이즈 캡틴 스피킹"
    "어쩌구 저쩌구"
    "..."
    "그렇게 유나은은 무사 착륙하고 프위스 공항에 도착했다!"

    # image: 프위스(프랑스 or 스위스) 공항 사진
    ne "키야~~ 프위스 공기" with fade
    ne "후- 하~"
    ne "너무 좋다!! 꺄륵"
    ne "이럴때가 아니지!! 어서 숙소가서 짐 두고 본격적으로 여행을 즐겨보자!"
    ne "어디보자 숙소까지는..!!"

    menu:
        "편안하게 택시 ㅎㅎ":
            $ healthy += main_point
            $ money += minus_point
            ne "돈은 좀 나가지만,, 그래도 편하게 가야 첫날부터 화이팅 할 수 있지 ㅎ"
        "제일 저렴한 버스 가즈아~":
            $ money += main_point
            $ happy += minus_point
            ne "먹을거랑 액티비티할게 많은데 가성비 있게 버스도 좋지~"
        "타지에 왔으니 지하철도 한번 타볼까~?":
            $ funny += main_point
            $ healthy += minus_point
            ne "한국과는 다른 쾌쾌한 느낌.. 하지만 이것마저 운치로구나"
        "숙소를 가는 길부터 여행의 시작! 기차타고 숑숑":
            $ happy += main_point
            $ funny += minus_point
            ne "도시라 너무 슉슉 지나가지만! 얼른 짐두고 여행을 즐겨야징~~"

    na "(어찌어찌 잘 이동해서 숙소에 도착한 유나은)" with fade
    # image: 숙소 사진
    ne "나이스~~ 드뎌 도착!!!" with vpunch
    ne "이라고 했지만,, 벌써 시간이 저녁 6시네 ㅠㅠ"
    ne "뭐 사실 첫째날은 어느정도 예상한 것이니 다음날에 더 활기차게 놀아보자~!"
    ne "그렇다고 오늘을 그대로 버리긴 아까운데.."
    ne "마침 이 호텔이 프위스의 명물 <둥동탑> 근처였지??"
    ne "야경도 구경할 겸 얼른 둥동탑 보러 나가봐야겠다~"
    ne "(현재 상태 => 건강: [healthy], 행복: [happy], 재미: [funny], 금전: [money])"

    # image: 에펠탑 야경 사진, music: 스텔라장 - L’Amour, Les Baguettes, Paris
    ne "우와 대박!!" with fade
    ne "너무 멋지다.."
    ne "내가 둥동탑을 실제로 보게될 줄은 ㅠㅠ.. 크으 감격스럽다"
    ne "야경도 너무 예쁘다 ㅎㅎ"
    ne "좀있으면 반짝인다고도 하는데"
    ne "같이 사온 피자와 와인이랑 이 둥동탑 구경을 즐겨봐야지~~"
    ne "그건 그렇고 나란 여자 어떻게 이 프위스 여행에 당첨된거지??"
    ne "난 아무것도 응모한게 없는거 같긴한데.. 흠.."
    ne "에라 모르겠다~ 일단은 다 잊고 탑멍이나 때리자 ><"

    nvl clear
    "유나은은 그렇게 둥동탑을 보며 운치에 젖어들었다"
    "둥동탑을 보니 어딘가에서 흘러나오는 노래도 나를 반긴다"
    "회사 생활로 찌든 몸과 마음이"
    "지금 이 순간으로 풀리는 느낌이다"
    "남은 모든 여행이 오늘만 같기를 바라며"
    "유나은은 늦게까지 구경하다 숙소에 들어와 잠을 청했다"


    ## Day 2 ##

    $ renpy.notify("프위스 여행 2일차")
    
    # image: 숙소 사진
    na "(유나은 공주님 일어나세요~)" with fade
    ne "으어어어ㅓ.."
    ne "벌써 아침인가..??"
    ne "아 맞다! 내가 오늘 아침 일찍부터 가야할 빵집이 있어서 일찍 알람을 맞췄지?"
    ne "어디보자 지금 시간이.."
    ne "오오 아직 아침 6시인거 보니 잘 일어났군 ㅎ"
    ne "왠지 2일차 시작부터 느낌이 좋은걸~?"
    ne "지금 딱 준비해서 출발하면 맞겠어!"
    ne "자 그럼 어제 찾아놓은 빵집이 어디였더라.."

    menu:
        "근본 오브 근본! 도넛이 맛있는 <윤티드> 프위스점!":
            $ happy += main_point
            $ hidden += sub_point
            $ choice_word = "도넛"
            ne "윤티드라면 이미 알바 경력으로도 다져진 몸! 해외까지 섭렵해주겠어 흐흐"
        "앗 지금까지 이런 빵은 없었다! 크로와상이 맛있는 <크로코코>!":
            $ money += main_point
            $ choice_word = "크로와상"
            ne "평점만 무려 4.9!! 가격도 저렴해! 어맛! 이건 사야해~"
        "본사가 초콜릿 공장?! 에끌레르가 맛있는 <웡카's브레드>!":
            $ funny += main_point
            $ choice_word = "에끌레르"
            ne "이름부터 믿음이 가버린다.. ㅎㅁㅎ 어서 빨리 먹고 싶다~"
        "프위스식 정통 샌디치~ 샌드위치가 맛있는 <메인웨이>!":
            $ healthy += main_point
            $ choice_word = "샌드위치"
            ne "프위스는 바게트가 유명한걸로 아는데,, 그 바게트로 만든 샌드위치? 이건 못참지 ㅋㄷ"

    nvl clear
    "유나은은 들뜬 마음으로 준비를 호다닥 마치고 찾아놓은 빵집으로 향했다"
    "빵집을 가는길 마저 상쾌한 공기가 유나은을 반긴다"
    "그렇게 빵집까지 순조롭게 잘 찾아갔는데.."
    
    # image: 빵집
    na "(빵을 왕창 사들고 나온 유나은)" with fade
    ne "너무 맛있어보여서 사려던거 말고 이것저것 다 사버렸잖아?"
    ne "에이 뭐 아무렴 어때 ㅎㅎ"
    ne "자 그럼 내가 제일 먹고 싶었던 [choice_word]부터 한번 먹어볼까~?"
    ne "와-앙~"
    ne "!!! 너무 맛있어 ㅠㅠ" with hpunch
    ne "역시 프위스라 그런지 이 분위기에 취해 빵도 맛있구나~~"
    ne "(현재 상태 => 건강: [healthy], 행복: [happy], 재미: [funny], 금전: [money])"
    
    # image: 유럽 프랑스 다리 or 거리
    na "(빵을 다 먹고 난 뒤)" with fade
    ne "아~~ 잘 먹었다~~ ^^"
    ne "먹다보니 아침의 프위스 거리를 구경하게 되었네 ㅎㅎ"
    ne "자! 그럼 이제 다음 목적지는.."
    ne "프위스에 제일 유명한 미술관인 <오렌지 미술관>!!"
    ne "얼른 가보자 흐흐"

    nvl clear
    "프위스 아침 거리를 거닐며 오렌지 미술관으로 향하는 유나은"
    "프위스만의 독특한 건물 양식과 달리기하는 프위스 주민들을 보며"
    "행복함을 느끼면서 오렌지 미술관으로 향했다"

    # image: 미술관
    na "(오렌지 미술관에 도착한 유나은)" with fade
    ne "여기가 내가 좋아하는 모네 그림도 있고 여러 다른 작가들의 그림도 있는 미술관이라 했지?"
    ne "우와~!~!" with vpunch
    ne "너무 멋진 그림들이 잔뜩 있잖아!!"
    ne "이 색감과 그림 표현의 질감.. 너무 예쁘다.."
    ne "흠 어디보자~"
    ne "이 중에서 내 최애 그림은!"

    menu:
        "돗자리 위에서 루미큐브가 있는 그림 <작품명: 봐주지마>":
            $ funny += main_point
            $ hidden += sub_point
        "식탁 위에 음식이 한가득 있는 그림 <작품명: 다이어트는 어려워>":
            $ healthy += main_point
        "노란 은행나무 아래 우수수 떨어진 은행나뭇잎 그림 <작품명: 이게 다 돈이였으면>":
            $ money += main_point
        "한적한 공원에 아이들이 뛰어놀고 있는 그림 <작품명: 얼음땡>":
            $ happy += main_point

    ne "역시 이 그림이 최고야~!~!"
    ne "묘하게 빠져든다 흐흐흐.."
    ne "(현재 상태 => 건강: [healthy], 행복: [happy], 재미: [funny], 금전: [money])"

    nvl clear
    "한동안 넋을 놓고 그림을 구경하던 유나은은"
    "몇시간이 지났는지도 모르게 계속 그림들을 봤다"
    "아름다운 그림들을 보며 마음의 평화와 양식을 찾게 된 유나은"
    "그러다 보니 배가 고파져서 점심을 먹기 위해 미술관을 나왔는데.."

    # image: 공원(??)
    ne "으아아아ㅏ.. 교양을 너무 쌓았더니(?) 배가 고프네?" with fade
    ne "ㅋㅋㅋㅋㅋㅋ"
    ne "뭐~ 아무렴 어때~? 밥이나 먹으러 가자~"
    ne "오늘 점심은 뭘 먹는게 좋으려나 흠흠"
    
    menu:
        "프위스에 왔으니 프위스식 식당을 가야지!":
            $ funny += main_point
            $ healthy += main_point
            $ choice_word = "프위스식 식당"
        "프위스에 왔어도 역시 한식당은 이길 수 없지!":
            $ happy += main_point
            $ money += main_point
            $ choice_word = "한식당"
    
    ne "오케이! 너로 정했다~ 가즈아~~"

    nvl clear
    "배가 고파진 유나은은 빠르게 [choice_word]을 찾았다"
    "미리 한국에서 서치해 놓은 덕분에(?) 괜찮은 식당을 바로 찾을 수 있었다"
    "그리고 식당에 가서 허겁지겁 음식을 먹었다"
    "프위스에서 만든 음식이라 그런지 꽤나 신선하고 좋았다"
    "음식으로도 특별한 경험을 할 수 있단걸 느낀 유나은은"
    "밥을 다 먹고 2차 행선지를 향해 나아갔다"

    # image: 식당 앞 or 길거리
    ne "꺼-억 잘먹었다~ ㅎ" with fade
    ne "(현재 상태 => 건강: [healthy], 행복: [happy], 재미: [funny], 금전: [money])"
    ne "어디보자 이제 시간이 한 두세시가 넘었네"
    ne "그렇다면 그 다음에 갈 곳은 바로~~"
    ne "프위스 유명 백화점 <갤럭시아>" with vpunch
    ne "프위스까지 왔는데 쇼핑은 한번 해야지 흐흐"
    ne "요 백화점에 명품이란 명품은 다 있다고 했고 심지어 한국에서 사는 것보다 싸다고 했으니..!"
    ne "늦기전에 얼른 가쟝~~"

    # image: 백화점
    na "(백화점에 도착한 유나은)" with fade

    # 저녁 재즈바 -> menu: 노래 선택


    ## Day 3 ##
    # 오전: 안시 호수공원 (오리배)
    # 오후: 샤모니 산 등산


    ## Day 4 ##
    # 오전: 한적한 시골마을 이동
    # 오후: 샬레에서 보내는 동네 산책, 카페, 별구경, 집밥 요리


    ## Day 5 ##
    # 오전: 유람선 타기
    # 오후: 돗자리 펴고 호수 구경, 교환학생 친구 만나 저녁


    ## Day 6 ##
    # 오전: 리기산 등산
    # 오후: 프라이탁 가방 구매


    ## Day 7 ##
    # 비행기 타러 출발 -> 비행기에서 잠을 자는데..


    ## Ending ##
    # 자고 일어나니 꿈
    # 1-1. 행복: 이렇게 행복한 꿈이라니.. 오늘 하루는 뭔가 기분 좋은 일이 일어날 것만 같아~ (진짜 프위스 여행권 DM 받음)
    # 1-2. 재미: 꿈에서 너무 재밌었어!! 그래!! 이 재미를 또 한번 찾고자 진짜 여행을 떠나보자!! (마침 친구에게 당첨된 여행권이 있다며 연락이 오는데)
    # 1-3. 건강: 좋은 꿈을 꾸니까 몸도 마음도 건강해진 기분이야!! 엇 근데 나 이렇게 날씬했나..? (몸무게 46키로 됨)
    # 1-4. 금전: 이건 거의 준돼지꿈이야..!! 아참 지난번에 산 복권 어떻게 됐지?! (당첨)
    # 2. 진엔딩: 눈을 떠보니 10월 스위스 샬레에서의 아침.. 아직 우리의 유럽 여행은 끝나지 않았다..!!!

    return
