﻿# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.)
define ne = Character("유나은", color="#f7b1cb")
define so = Character("???", color="#214bac")
define bb = Character("동해", color="#214bac")
define bb = Character("진예", color="#dca236")

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
    ne "(현재 상태 => 건강: [healthy], 행복: [happy], 재미: [funny], 금전: [money]\n히든 포인트: [hidden])"

    nvl clear
    "유나은은 그렇게 들뜬 마음으로 DM을 보며 여행갈 상상에 빠진다"
    "그렇게 몇일이 지나 드디어 다가온 여행 당일!"
    "유나은의 좌충우돌 6일간의 프위스 여행이 시작된다!!!"


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
    ne "(현재 상태 => 건강: [healthy], 행복: [happy], 재미: [funny], 금전: [money]\n히든 포인트: [hidden])"

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
    ne "(현재 상태 => 건강: [healthy], 행복: [happy], 재미: [funny], 금전: [money]\n히든 포인트: [hidden])"

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
    # image: 파른 숙소 사진
    ne "나이스~~ 드뎌 도착!!!" with vpunch
    ne "이라고 했지만,, 벌써 시간이 저녁 6시네 ㅠㅠ"
    ne "뭐 사실 첫째날은 어느정도 예상한 것이니 다음날에 더 활기차게 놀아보자~!"
    ne "그렇다고 오늘을 그대로 버리긴 아까운데.."
    ne "마침 이 호텔이 프위스의 명물 <둥동탑> 근처였지??"
    ne "야경도 구경할 겸 얼른 둥동탑 보러 나가봐야겠다~"
    ne "(현재 상태 => 건강: [healthy], 행복: [happy], 재미: [funny], 금전: [money]\n히든 포인트: [hidden])"

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
    
    # image: 파른 숙소 사진
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
    "주변에 미켈란젤로의 영향을 받은 건물들이 아름답게 펼쳐져 있다"
    "(어디선가 공찍이라는 소리도 들리는 것 같다..? ㅇㅅㅇ)"
    "크흠.. 무튼 그렇게 유나은은 빵집까지 순조롭게 잘 찾아갔는데.."
    
    # image: 빵집
    na "(빵을 왕창 사들고 나온 유나은)" with fade
    ne "너무 맛있어보여서 사려던거 말고 이것저것 다 사버렸잖아?"
    ne "에이 뭐 아무렴 어때 ㅎㅎ"
    ne "자 그럼 내가 제일 먹고 싶었던 [choice_word]부터 한번 먹어볼까~?"
    ne "와-앙~"
    ne "!!! 너무 맛있어 ㅠㅠ" with hpunch
    ne "역시 프위스라 그런지 이 분위기에 취해 빵도 맛있구나~~"
    ne "(현재 상태 => 건강: [healthy], 행복: [happy], 재미: [funny], 금전: [money]\n히든 포인트: [hidden])"
    
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
    ne "(현재 상태 => 건강: [healthy], 행복: [happy], 재미: [funny], 금전: [money]\n히든 포인트: [hidden])"

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
    ne "(현재 상태 => 건강: [healthy], 행복: [happy], 재미: [funny], 금전: [money]\n히든 포인트: [hidden])"
    ne "어디보자 이제 시간이 한 두세시가 넘었네"
    ne "그렇다면 그 다음에 갈 곳은 바로~~"
    ne "프위스 유명 백화점 <갤럭시아>" with vpunch
    ne "프위스까지 왔는데 쇼핑은 한번 해야지 흐흐"
    ne "요 백화점에 명품이란 명품은 다 있다고 했고 심지어 한국에서 사는 것보다 싸다고 했으니..!"
    ne "늦기전에 얼른 가쟝~~"

    # image: 백화점 내부
    na "(백화점에 도착한 유나은)" with fade
    ne "진짜 명품이란 명품은 다 있잖아..!! ㅎㅁㅎ"
    ne "샤넬에 구찌, 루이비똥, 티파니앤코, 셀린느, .."
    ne "다 구경하는 것만으로 한 세월이겠군"
    ne "그치만 난 미리 살 것을 알아놨지 ㅎㅎ"
    ne "내가 살 것은 바로~~"

    menu:
        "<스카이실버>의 세련되고 심플한 검은색 카드 지갑!":
            $ happy += main_point
            ne "안그래도 카드 지갑 필요했는데~! 흐흐 역시 쇼핑은 언제나 행복하군"
        "<쏘스윗>의 상큼 발랄한 노란색 티셔츠!":
            $ funny += main_point
            ne "이 옷 색깔하며 디자인이 너무 이쁘자나~!~!"
        "<디에이치>의 포근하고 따뜻한 느낌의 가디건!":
            $ healthy += main_point
            ne "걸치기만 해도 마음이 따뜻해지는 느낌이야 ㅎㅎ"
        "사실 없어 ㅋㅋ 그냥 구경하러 온거야 ㅎㅅㅎ":
            $ money += main_point
            $ hidden += sub_point
            ne "아이쇼핑이 최고지 ㅋㅋ 👍"
    
    nvl clear
    "이후에도 유나은은 이곳 저곳 돌아다니며 백화점을 신나게 구경했다"
    "백화점에는 다양한 것들을 판매하고 있었다"
    "하나하나 구경하다 보니 어느새 꼭대기까지 올라갔는데"
    "그 앞에 전망대로 이어지는 길이 있었다"
    "유나은은 그렇게 전망대로 향하는데"

    # image: 백화점 전망대
    ne "우와.. 이게 정녕 백화점 전망이란 말인가.." with fade
    ne "너무 아름답다.."
    ne "도심이 쫙 펼쳐지는 이 광경"
    ne "그리고 저 멀리 보이는 둥동탑까지"
    ne "이런 도심이라면 매일 매일 살고 싶을거 같아"
    ne "(꼬르륵..)"
    ne "하하.. 이게 왠걸 이 타이밍에 기가막히게 배에서 밥 달라고 하네"
    ne "그래! 이제 슬슬 해도 지는 것 같고~"
    ne "어서 미리 예약해둔 재즈바로 가자!!"
    ne "(현재 상태 => 건강: [healthy], 행복: [happy], 재미: [funny], 금전: [money]\n히든 포인트: [hidden])"

    # image: 재즈바
    na "(재즈바로 이동한 유나은)" with fade
    ne "오호!! 여기가 프위스에 유명하다는 재즈바 <딩가딩가>로군!"
    ne "주변 외국인들도 즐겁게 술 마시고 있고~"
    ne "때마침 노래도 시작하고~"
    ne "음흠음흠~~ 분위기 너~~~~므 좋다 ㅎㅎ"
    ne "엇! 잠시만..!!"
    ne "신청곡도 할 수 있잖아!"
    ne "오호~ 그러면 나도 하나 신청해볼까~?"

    menu:
        "요새 푹 빠진 노래!! <Wave to Earth - Bad>":
            # music: Wave to Earth - Bad
            $ money += main_point
            ne "대박!! 이걸 재즈바에서 듣게 되다니..! 그것도 프위스에서"
            ne "재즈바 온 보람이 있어! 돈이 하나도 안아깝잖아!!"
        "재즈바하면 이 노래징~~ <Daniel Caesar - Best Part>":
            # music: Daniel Caesar - Best Part
            $ healthy += main_point
            ne "크으~~ 감성 쥑인다~~"
            ne "술을 마시지 않아도 취하는 구나 ^^"
        "이런거 신청해도 해주나? <백예린 - 산책>":
            # music: 백예린 - 산책
            $ happy += main_point
            ne "ㅎㅁㅎ 이왜진????"
            ne "그런데 프위스 재즈바에서 듣는 산책이라니.. 묘하면서 행복하다 ㅎㅎ"
        "아몰랑 국뽕이 최고여 >< <BTS - 다이너마이트>":
            # music: BTS - 다이너마이트
            $ funny += main_point
            ne "진짜 틀어주네?!?! ㅋㅋㅋ"
            ne "으어어어ㅓ 국뽕이 차오른드아아ㅏㅏㅏ.."

    ne "(현재 상태 => 건강: [healthy], 행복: [happy], 재미: [funny], 금전: [money]\n히든 포인트: [hidden])"

    nvl clear
    "유나은은 그렇게 재즈바에 취해간다"
    "신청한 노래 뿐만 아니라 다른 재즈곡들도 들으며 마음의 힐링을 하게된다"
    "그렇게 프위스의 두번째 밤이 유나은을 은은하게 비치다 어두워진다"
    "(이 다음은 다음 날 입니다~\n노래를 더 듣고 싶으면 잠깐 여기서 감상하세요 ^^)"


    ## Day 3 ##

    $ renpy.notify("프위스 여행 3일차")
    
    # image: 파른 숙소 사진
    na "(유나은 공주님 일어나세요~)" with fade
    ne "으어어어ㅓ.."
    ne "역시 아침은 눈뽑 하루군 ㅋㅋ.."
    ne "그래도 아름다운 이 프위스 ㅎㅎ"
    ne "오늘은 프위스의 소도시 안모니에 가는 날이지!!"
    ne "얼른 준비하고 기차타러 쇼숑하자~~"

    nvl clear
    "유나은은 부랴부랴 준비한 뒤 기차를 타러 숙소를 나섰다"
    "이틀밤밖에 자지 않은 숙소지만"
    "정든 숙소를 떠나는 길에 왠지 마음이 뭉클해진다"
    "하지만 아쉬운 마음을 뒤로한채 기차역까지 들뜬 마음으로 발걸음을 옮겼다"
    
    # image: 기차안 사진
    na "(기차역에 도착한 뒤 좌석에 앉은 유나은)" with fade
    ne "휴.. 간신 세이프..!!"
    ne "때 마침 출발하는 기차라니~~"
    ne "역시 난 운이 좋은가봐 후훗 ㅎ"
    ne "어디보자 기차는 자고로 밖 풍경을 보는 재미도 쏠쏠하지!"
    ne "이 터널이 지나면 어떤 풍경이 펼쳐질까? ><"

    menu:
        "드넓은 산이 웅장하게 나타났음 좋겠다!":
            # image: 웅장하고 드넓은 산 사진 (열차안에서 보이는 풍경처럼?)
            $ funny += main_point
            $ choice_word = "산"
        "운치있는 호수가 아름답게 펼쳐졌음 좋겠다!":
            # image: 아름답고 운치있는 호수 사진 (열차안에서 보이는 풍경처럼?)
            $ happy += main_point
            $ hidden += sub_point
            $ choice_word = "호수"
        "삐까뻔쩍한 건물들이 으리으리하게 보였으면 좋겠다!":
            # image: 삐까뻔쩍하고 으리으리한 건물 사진 (열차안에서 보이는 풍경처럼?)
            $ money += main_point
            $ choice_word = "건물"
        "광활한 벌판이 푸르르게 펼쳐졌음 좋겠다!":
            # image: 푸르르고 광활한 벌판 사진 (동물도 있음 좋고) (열차안에서 보이는 풍경처럼?)
            $ healthy += main_point
            $ choice_word = "벌판"

    ne "헐 대박!!" with vpunch
    ne "진짜로 내가 기대하던 [choice_word] 풍경이 나타났잖아!!!"
    ne "너무 낭만있고 너무 좋다.."
    ne "한 폭의 그림같은 이 순간 ㅎㅎ 행복 그잡채"
    ne "(현재 상태 => 건강: [healthy], 행복: [happy], 재미: [funny], 금전: [money]\n히든 포인트: [hidden])"

    nvl clear
    "유나은은 창밖 풍경을 보며 기차 여행의 설렘을 즐기다가"
    "아름다운 풍경에 정신을 빼앗기며 스르르 잠에 들었다"
    "얼마만큼의 시간이 지났을까 유나은은 금새 목적지에 도착하게 되었다"

    # image: 안시 소도시 (구시가지) 사진
    ne "여기가 안모니인건가? ㅎㅎ" with fade
    ne "역시 어제 있었던 프위스 수도인 파른과는 또 다른 느낌이군"
    ne "후~~~ 하~~~~"
    ne "이 상쾌한 공기!"
    ne "너무나 평온하다 ^^"
    ne "엇 아닛!!" with vpunch
    ne "저기는 호수인가..!! ㅎㅁㅎ"
    # image: 안시 호수 및 공원 사진
    ne "헐 대박!!!"
    ne "너무 이쁘다.. ㅠㅠ"
    ne "저기 패들보트도 있는 것 같은데 저거나 타면서 호수 구경 제대로 해볼까~?"

    nvl clear
    menu:
        "보트타고 호수 위에서 둥둥 떠다니자!!":
            $ happy += main_point
            $ funny += main_point
            $ hidden += sub_point
            "유나은은 보트를 다고 호수를 유유자적 거닐었다"
        "흐흐 짐도 있는데 귀찮으니까 호수 공원 벤치에서 나른하게 쉬자":
            $ healthy += main_point
            $ money += main_point
            "유나은은 근처 벤치에 앉아 주변을 구경했다"
    
    "기차때부터 이어진 한 폭의 그림같은 순간들이 계속 이어진다"
    "나른한 햇살 아래 유나은은 잠시 휴식을 취하며 힐링을 한다"
    "..."
    "그렇게 몇분이 지나고 유나은은 꿀맛같은 휴식을 마친뒤"
    "발걸음을 옮기기 시작했다"

    ne "후하~ 잘 즐겼다 ㅎㅎ" with fade
    ne "이제 어서 짐을 숙소에 두고 오후 일정을 하러 가보자!!"
    ne "(현재 상태 => 건강: [healthy], 행복: [happy], 재미: [funny], 금전: [money]\n히든 포인트: [hidden])"

    nvl clear
    "유나은은 숙소에 짐을 두고 컵라면으로 끼니를 떼운 뒤"
    "안모니의 대표적인 설산인 동블랑을 등반하기 위해"
    "케이블카가 있는 곳으로 향했다"

    # image: 샤모니 산 아래 케이블카 사진
    na "(산 아래 케이블카가 있는 곳에 도착한 유나은)" with fade
    ne "오오"
    ne "여기가 세계 최고의 설산인 동블랑이 있는 곳인가..!!"
    ne "케이블카를 타고가면 한번에 3842 고지 만큼 올라간다는데"
    ne "이건 안탈수가 없지 ㅇㅇ"
    ne "하나 둘~ 바로가쟝~"

    # image: 샤모니 설산 사진
    na "(케이블카를 타고 산 위로 올라온 유나은)" with fade
    ne "히이이이익" with vpunch
    ne "이건 진짜 미친거 아냐!!!"
    ne "대박 이렇게 멋지고 아름다울 수 있는 것인가..!!"
    ne "날씨도 너무 좋아서 저 멀리 있는 설산까지 한눈에 다 보인다 ㅎㅁㅎ"
    ne "이건 무.적.권 사진 찍어야해!!"
    na "(찰칵 찰칵)"  # (괜찮은 transition 있으면 추가)
    ne "흠흠~ 내 사진도 찍어둘까~?"
    ne "포즈는.."

    menu:
        "이 설산은 내가 지킨다! 슈퍼 히로인 자세!!":
            $ healthy += main_point
        "설산에도 꽃이 폈다고? 그건 바로~ 유나은 꽃 ㅎ":
            $ funny += main_point
        "손하트! 볼하트!! 대빵하트 포즈!!!":
            $ happy += main_point
        "무심한듯 시크하게.. 하지만 약간은 새침하면서도 은은한 미소":
            $ money += main_point

    na "(찰칵!)"
    ne "헤헤.. 잘 나왔다 헤헤"
    ne "그건 그렇고.. 약간 고산이라 그른지 고산병이 사알짝 도져지는 느낌은 기분 탓이려나..? ㅎㅎ"
    ne "너무 오래는 있지말자 ㅎㅎ.."
    ne "그래도 이 설산은.. 한국가면 또 생각날거 같아"
    ne "너무나 아름다운 이 풍경"
    ne "눈으로라도 잔뜩 담아두고 오자!!"
    ne "(현재 상태 => 건강: [healthy], 행복: [happy], 재미: [funny], 금전: [money]\n히든 포인트: [hidden])"

    nvl clear
    "그렇게 몇분을 더 구경하던 유나은은"
    "고산병이 아닌 으슬으슬 추워서(??) 다시 케이블카를 타고 하산했다"
    "근처 카페나 브랜드들도 있어서 간단히 쇼핑도 했다"
    "높은 설산에서부터 타고 흐른건지 모를 푸르른 계곡이"
    "차갑게 만든 유나은의 손발을 따뜻하게 반긴다"
    "이렇게 동블랑의 일정을 모두 소화하고 유나은은 다시 숙소로 이동했다"

    # image: 안시 숙소 사진
    na "(숙소에 도착한 유나은)" with fade
    ne "으아아아아ㅏㅏㅏ"
    ne "오늘은 다양하게 많은걸 하진 않았지만.."
    ne "그래도 너무 알찼다 ㅎㅎ"
    ne "아름다운 풍경들도 잔뜩보고"
    ne "행복한 순간들만 가득가득 했네~"
    ne "저녁은 아까 포장해온 베트남 쌀국수!"
    ne "왠지는 모르겠지만,, 뭔가에 홀린듯(?) 사게된 거 같아..!"
    ne "유럽가면 누가 베트남 쌀국수가 땡긴다고 했던거 같기도 하고..?"
    ne "에라 아몰랑~"
    ne "일단 흐흐 잘먹겠습니다~~ 와앙"

    nvl clear
    "오랫동안(?) 동양 음식을 먹지 못했던 것인지"
    "쌀국수의 맛에 흠칫 놀라며"
    "따뜻한 국물 또한 마음까지 편하게 만들어 주었다"
    "너무나 힐링한 저녁이였을까?"
    "유나은은 배부르게 먹고 행복한 순간들만 껴안은채"
    "언제가 됐는지도 모르게 잠에 들었다"


    ## Day 4 ##

    $ renpy.notify("프위스 여행 4일차")
    
    # image: 안시 숙소 사진
    na "(유나은 공주님 일어나세요~)" with fade
    ne "으어어어ㅓ.."
    ne "맨날 똑같은 느낌으로 일어나는데 기분탓인가.. ㅎㅎ"
    ne "흠냐 흠냐"
    ne "아냐 정신차려!"
    ne "오늘은 내가 이번 프위스 여행에서 제일 기대하던 브리오슈의 샬레에 가는 날이지?!?!"
    ne "키야!! 내가 이 날만을 얼마나 기다렸던가~~"
    ne "물론 지금까지의 날들도 너무 좋았지만 크흠 ㅋㅋ.."
    ne "오전에 이동해야하니 어여 씻고 준비해보자!!"

    nvl clear
    "유나은은 빠르게 샤워를 하고 짐을 챙겼다"
    "안모니에서의 일정은 하루 밖에 없어서 아쉬운 마음이 컸지만"
    "근처 구시가지 시장과 함께 아침해가 뜨는 모습만 봐도"
    "아쉬움 보단 행복만을 가득 안고 떠날 수 있었다"
    "무튼 유나은은 브리오슈까지의 여정으로 유람선을 타기로 했는데.."

    # image: 루체른 유람선 사진
    na "(유람선에 도착한 유나은)" with fade
    ne "읏챠~ 유람선 탑승 완료!!"
    ne "브리오슈까지 이 유람선을 타면 한번에 이동할 수 있다니~!~!"
    ne "이렇게 낭만 넘치는 프위스.. 날 어떻게 할 셈인거냐!!!"
    ne "호수 풍경도 너무 좋고~"
    ne "후-하- 날씨도 최상이고~"
    ne "그리고 가는 길 배고프지 않게 아까 구시가지에서 사온..!"

    menu:
        "황금..은 아니지만 황금 사과가 되고픈 뻘건 사과 🍎":
            $ money += main_point
        "행복을 가져다 줄 것만 같은 네알 달린 체리 🍒":
            $ happy += main_point
        "이게 복숭아 맞아 ㅋㄷ? 납작 복숭아 🍑":
            $ funny += main_point
            $ hidden += sub_point
        "역시 아침엔 기운 쑥쑥 노랑 바나나 🍌":
            $ healthy += main_point

    ne "한 입에 와-앙~"
    ne "우와!! 대박!!!" with vpunch
    ne "짱 맛있잖아..??"
    ne "이렇게 맛있을 줄 알았으면 여러개 사올껄 ㅠ"
    ne "아니지 유나은! 정신차려!"
    ne "지금은 과일에 신경쓸 시간이 아니라 바깥 풍경을 볼 시간이야!!"
    ne "이 아름다운 윤슬을 보며~!~!"
    ne "힘차게 출발~~~"
    ne "(현재 상태 => 건강: [healthy], 행복: [happy], 재미: [funny], 금전: [money]\n히든 포인트: [hidden])"

    nvl clear
    "유나은은 두둥실 떠가는 유람선 위에서"
    "따스히 호수 위에 비친 윤슬을 바라보며 브로오슈로 떠났다"
    "중간 중간 여러 경유지를 거치며"
    "프위스의 다양한 섬과 자연 경관을 즐길 수 있었다"
    "얼마 지나지 않은 것 같은데 유나은은 그렇게 브리오슈까지 도착했다"

    # image: 브리엔츠 호수가 사진
    na "(브리오슈에 도착한 유나은)" with fade
    ne "우와.. 여기가 그 말로만 듣던 브리오슈..??"
    ne "호수 물 색깔 좀 봐.. 에메랄드 빛이 따로 없어"
    ne "너무나 아름답다 여긴~!~!"
    ne "그리고 이 한적한 느낌과 왠지 모를 시골같은 느낌!!"
    ne "지금까지 가본 프위스 장소중에 제일 평화로운거 같아~~"
    ne "너무 좋은데 샬레까지 산책하며 가볼까~? ㅎㅎ"
    so "(슈슉!)" with hpunch
    ne "엇..!! 잠깐만..!!"
    ne "저건 뭐였지..! ㅎㅁㅎ"

    menu:
        "팔다리가 쬐끔해서 보기만 해도 웃음이 나오는 귀여운 댕댕이":
            $ funny += main_point
            ne "이그~!~! 완전 겸둥애기자나!!"
            ne "브리오슈의 강아지도 우리집 슈마냥 귀엽자나~~"
        "이 지역의 수호신이라 불리는 늠름한 사슴":
            $ money += main_point
            $ hidden += sub_point
            ne "아아 사슴이구나~~"
            ne "엥?? 사슴???" with vpunch
            ne "여긴 진짜 자연 그잡채로군.. wow"
        "당근을 야무지게 먹고 있는 토끼":
            $ healthy += main_point
            ne "헐 대박 토끼였어!!"
            ne "완전 토끼도 건강챙기려고 당근을 먹어~~"
        "뱃살도 포동포동한채 길거리에서 뒹굴 거리는 고양이":
            $ happy += main_point
            ne "헤헤 보기만 해도 흐뭇해지는 고양이네 ㅎㅎ"
            ne "나도 어여 샬레 들어가서 늘어지게 누워있어야지 흐흐"
    
    ne "(현재 상태 => 건강: [healthy], 행복: [happy], 재미: [funny], 금전: [money]\n히든 포인트: [hidden])"

    nvl clear
    "유나은은 그렇게 뜻밖의 동물 친구(?)와도 조우하며"
    "숙소까지의 산책을 이어갔다"
    "푸르른 날씨와 한적한 마을이 유나은의 마음도 편안하게 만들었다"
    "걷다보니 어느새 샬레 앞까지 도착한 유나은"
    "드디어 샬레 내부로 들어가게 되는데.."

    # image: 샬레 내부 사진 (메인 화면)
    ne "히이이이잉ㄱ" with vpunch
    ne "샬레 호수뷰 미쳤다잇~!~!"
    ne "오늘 나 너무 놀라는거 아냐??"
    ne "아니지!! 이정도면 또 놀랄만해!!"
    ne "이것보다 더 좋은 호수뷰가 있을까?? 경치 죽인다 크으~~"
    ne "샬레에서 이 경치만 구경해도 너무나 좋을거 같아.."
    ne "그러면 오늘은 샬레와 이 근처 구경으로만 일정을 세워볼까~?"
    ne "자! 그러면 일단 아까 올라오면서 점찍어둔 카페를 가서 빵을 사가지고 와서 동네 산책 죠지장~~"

    # image: 브리엔츠 -> 샬레 길거리 사진
    na "(샬레에서 나온 유나은)" with fade
    ne "룰루랄라~~"
    ne "엇..! 올라올 때는 몰랐는데 길이 두갈래 길이 있었네..??"
    ne "어디로 가야 아까 올라오면서 본 카페로 갈 수 있는 길이지?"

    menu:
        "왼쪽 길! 왠지 걷기만 해도 건강해지고 행복해질 것 같은 느낌이?!":
            $ happy += main_point
            $ healthy += main_point
        "오른쪽 길! 왠지 재밌어보이고 길가다 돈도 주울 수 있을 것 같은 느낌이?!":
            $ healthy += main_point
            $ money += main_point

    ne "오케이! 여기로 정했으!!"
    ne "(현재 상태 => 건강: [healthy], 행복: [happy], 재미: [funny], 금전: [money]\n히든 포인트: [hidden])"

    nvl clear
    "라고 했으나 사실 아무일도 일어나지 않았고"
    "그냥 카페에 무사히 도착할 수 있었다 ㅇㅅㅇ"
    "카페에는 마침 유나은이 원하던 빵과 커피가 있어서"
    "테이크아웃 하여 챙겨나왔다"
    "맛있는 빵과 커피를 마시며"
    "아까 마저 못느꼈던 자연과 아름다움을 한껏 느꼈다"
    "..."
    "이렇게 시간을 보내다 어느덧 저녁이 되어"
    "유나은은 샬레에서 요리를 할 저녁거리를 사고 다시 샬레에 들어왔다"

    # image: 샬레 내부 사진 (메인 화면)
    ne "자~ 오늘의 저녁 메뉴는~~"
    ne "두구두구두구두구.."
    ne "바로 바로..!!"
    ne "삼겹살~!~!~!" with vpunch
    ne "크으.. 타지에서 먹는 근본 한식이라니.. 이건 못참지!!"
    ne "얼른 꿔서 맛나게 먹쟝 ㅎㅎ"
    
    na "(배터지게 먹고난 유나은)" with fade
    ne "어우.. 너무 맛있게 잘먹었다.. 꺼억-"
    ne "넘 배부른데.. 밤산책 한번더 스슥할까?? ㅋㅋ"
    ne "말해 뭐해~ 바로 고고씽~"

    # image: 밤 샬레 or 별 사진
    na "(밖에 나온 유나은)" with fade
    ne "벌써 저녁이라 그런지 아주 깜깜하구만..!! ㅎㅁㅎ"
    ne "엇 근데 하늘에 별이.."
    ne "우와...!! 이렇게나 별이 잘보인다고~?~?"
    ne "헐 대박이야 진짜~~"
    ne "맑은 공기에 하늘이라 그런지 별자리도 보인드아..!"
    ne "어디보자 저 별자리는.."
    
    menu:
        "격자무늬 별들이 거북이 등껍질 같으니 <엉금자리>가 틀림없군!":
            $ happy += main_point
        "가운데 별을 중심으로 고양이 수염 모양이니 <춘식자리>가 틀림없군!":
            $ funny += main_point
        "네모난 식빵 모양으로 별들이 있으니 <냠냠자리>가 틀림없군!":
            $ healthy += main_point
        "동그란 모양이 숫자 0을 나타내고 있으니 <월급자리>가 틀림없군!":
            $ money += main_point
        
    ne "라곤 했지만 사실 난 별자리를 볼 줄 모르니 대충 말한거다 ㅋㄷ"
    ne "아무렴 어때~ 나만 좋으면 됐지머 ㅎㅎ"
    ne "엇.. 근데 저녁이라 그런지 약간 으슬으슬 춥네잉\n(어디선가 한몸처럼 착붙이라는 말이 들리는거 같기도?)"
    ne "어서 빨리 들어가서 하루 마무리하고 자야겠다~"
    ne "(현재 상태 => 건강: [healthy], 행복: [happy], 재미: [funny], 금전: [money]\n히든 포인트: [hidden])"

    nvl clear
    "유나은은 그렇게 샬레에 들어와 씻고 침대에 누웠다"
    "창 밖으로 깜깜한 밤 사이에 환히 빛나는 달과 별들이 보인다"
    "아까도 보고 왔지만 이 아름다움에 취해 잠시 밖을 멍하니 바라보았는데"
    "유나은은 언제가 됐는지도 모르게 꿈나라로 빠지게 되었다"


    ## Day 5 ##
    # 오후: 프라이탁 가방 구매, 호수 구경, 교환학생 친구 만나 저녁

    $ renpy.notify("프위스 여행 5일차")
    
    # image: 샬레 사진
    na "(유나은 공주님 일어나세요~)" with fade
    ne "드르렁 쿨~ 드르렁 쿨~"
    
    nvl clear
    "그렇다"
    "유나은은 너무나도 편안한 분위기에 취해 꿀잠을 자고 있었다"
    "ㅋㅋ"
    
    na "(그렇게 한 두시간을 더 자다가 깬 유나은)" with fade
    ne "흠냐 흠냐"
    ne "엥!!! 오전 내내 자버렸잖아..!!" with vpunch
    ne "여행 와서 잠으로 너무 많은 시간을 쏟은거 같아 조금 속상하지만 ㅠㅠ"
    ne "그만큼 이 샬레가 나에게 너무 아늑한 공간이란 뜻이였나 ㅎㅎ.."
    ne "나도 나중에 이런 샬레나 숙소(?) 같은거 하나 잘 만들어서"
    ne "제주도에서 손님들 받고 숙박업이나 해볼까~~"
    ne "물론 내가 살 집도 짓고 흐흐"
    ne "에휴 정신차리자 나은아.. 현실을 생각해..!"
    ne "일단 꿀잠도 잤겠다 어여 준비하고 출발하자!!"

    nvl clear
    "유나은은 빠르게 씻고 준비를 마쳤다"
    "잠을 충분히 자서 그런지 오늘따라 더 기운찬 하루인 것 같다"
    "유나은은 프위스 여행에서 학수고대하던 것 중 하나가 있었는데"
    "그것은 <프리데이> 가방을 사는 것이였다!!"
    "프리데이는 프위스의 대표적인 업사이클링 업체로"
    "이미 국내외에서도 유명한 브랜드이다 ㅎㅎ"
    "무튼.. 그렇게 프리데이 본점이 있는 히리취로 향했는데.."

    # image: 프라이탁 매장 사진
    na "(프리데이 본점에 도착한 유나은)" with fade
    ne "우와~!~! 여기가 프리데이 본점..!!"
    ne "내가 여기를 직접 방문하는 순간이 오다니.. 넘 감격스럽다 ㅠㅠ"
    ne "흠흠 그럼 내가 입양할 아가를 하나 골라볼까~?"

    menu:
        "유광의 깔끔하고 모던한 회색 제이미 가방":
            $ healthy += main_point
            ne "키야!! 이렇게 깨끗하고 세련된 회색 가방이라니~!~!"
            ne "너무 갖고 싶었는데 잘됐다 ㅎㅎ"
        "LALA 라고 적힌 흰색 하와이 파이브오 가방":
            $ happy += main_point
            ne "완전 이건 날 위한 가방 아냐?!?!"
            ne "당장 입양해야지!!"
        "윤티드 로고색의 깜찍한 소니 가방":
            $ funny += main_point
            ne "끼야!! >< 요렇게 겸둥탱 가방은 한국에선 절대 볼 수 없는데!!"
            ne "오케이 너로 정했어~~~~"
        "이중엔 마음에 드는게 없어.. 이번 여행에선 꾹 참자..":
            $ money += main_point
            bb "큼큼.."
            bb "갑자기 튀어나와서 많이 당황하셨죠? ㅎ"
            bb "개발자인 저도 이걸 플레이하시는 분이 이 선택지를 고를지 몰랐네요"
            bb "요 선택지는 당연 선택 안할 줄 알아서 개발을 안해놨답니다~"
            bb "뭐가 그리 당당하냐고요?"
            bb "이스터에그라고 생각해주세요 ><"
            bb "아마 다음 멘트는 셋 중 무언갈 산 뒤의 멘트로 이어질겁니다 ^^"
            bb "그럼 다시 게임으로 숑~"

    ne "(현재 상태 => 건강: [healthy], 행복: [happy], 재미: [funny], 금전: [money]\n히든 포인트: [hidden])"

    nvl clear
    "프리데이 본점에서 너무나도 맘에 쏙드는 가방을 구입했다는 사실이"
    "유나은을 더할나위 없이 행복하게 만들었다"
    "안그래도 오늘 오후에는 프위스로 교환학생 갔던 친구를 만나기로 했는데"
    "그 친구에게도 자랑할 생각에 마음이 들떠있었다"
    "유나은은 그렇게 가방을 잘 구매하고 친구를 만나러 른체루로 이동했다"

    # image: 루체른 사진
    na "(른체루에 도착한 유나은)" with fade
    ne "여기가 른체루구나!!"
    ne "오 여긴 도시같은 느낌인데 그렇다고 파른이랑은 또 다른 느낌이다!!"
    ne "여긴 진짜 낭만의 도시구나~~"
    ne "이 쯤에서 친구를 만나기로 했는데 어디쯤에 있지??"
    ne "아 맞다! 그전에 꽃 사들고 선물해줘야겠다 ㅎㅎ"
    ne "요 근처에 꽃집이 있었던거 같은데.."
    ne "앗 저기있다!!"
    ne "음~ 그럼 어떤 꽃을 살까?"

    menu:
        "행복을 가져다 줄 것만 같은 파란 국화!":
            $ happy += main_point
        "건강을 가져다 줄 것만 같은 노란 메리골드!":
            $ healthy += main_point
        "부귀를 가져다 줄 것만 같은 진분홍 모란!":
            $ money += main_point
        "즐거움을 가져다 줄 것만 같은 흰분홍 철쭉!":
            $ funny += main_point

    ne "오케이! 이 꽃으로 정했드아아아!!"

    nvl clear
    "그렇게 꽃을 사고 몇분 있다가 친구를 만나게 되었다"
    "오랜만에 만나는거라 약간은 어색할 줄 알았지만"
    "생각보다 너무 반갑고 즐거웠다"
    
    # image: 각 대사마다 루체른 호수 이미지 변경
    na "이야기하면서 걷다가 어느새 근처 호수 앞까지 온 두 사람" with fade
    na "공원에 돗자리를 깔고 수다를 이어갔다" with fade
    na "프위스에서 먹은 음식들.. 보고 경험한 일들.. 프리데이 가방 자랑.. 등등" with fade
    na "시간 가는줄 모르게 떠들던 둘은 어느새 날이 저무는 풍경을 바라보며 운치에 젖어들었다" with fade
    na "그렇게 몇시간이 지났을까? 곧 저녁 시간이 다가왔다" with fade

    ne "후아!!" with fade
    ne "벌써 저녁이 다 되어버렸네..! ㅎㅁㅎ"
    ne "진예야! 같이 저녁 먹고 가자! ㅎㅎ"
    ne "(현재 상태 => 건강: [healthy], 행복: [happy], 재미: [funny], 금전: [money]\n히든 포인트: [hidden])"


    ## Day 6 ##
    # 오전: 리기산 등산, 돗자리 펴고 낮잠
    # 비행기 타러 출발 -> 비행기에서 잠을 자는데..


    ## Ending ##
    # 자고 일어나니 꿈
    # 1-1. 행복: 이렇게 행복한 꿈이라니.. 오늘 하루는 뭔가 기분 좋은 일이 일어날 것만 같아~ (진짜 프위스 여행권 DM 받음)
    # 1-2. 재미: 꿈에서 너무 재밌었어!! 그래!! 이 재미를 또 한번 찾고자 진짜 여행을 떠나보자!! (마침 친구에게 당첨된 여행권이 있다며 연락이 오는데)
    # 1-3. 건강: 좋은 꿈을 꾸니까 몸도 마음도 건강해진 기분이야!! 엇 근데 나 이렇게 날씬했나..? (몸무게 46키로 됨)
    # 1-4. 금전: 이건 거의 준돼지꿈이야..!! 아참 지난번에 산 복권 어떻게 됐지?! (당첨)
    # 2. 진엔딩: 눈을 떠보니 10월 스위스 샬레에서의 아침.. 아직 우리의 유럽 여행은 끝나지 않았다..!!!

    return
