Date < - ymd("2017-04-12") - days(0: 365)  # 2017-04-12로부터 1년 동안의 날짜를 모두 나타냅니다.
df_2016 < - data.frame(Date)  # 데이터 프레임으로 변환합니다.
df_2016_format < - format(df_2016$Date, "%Y%m%d")  # yyyy-mm-dd의 구조를 url에 적용할 수 있도록 yyyymmdd의 형태로 바꿔줍니다.

for (d in 1:length(df_2016_format)) {
url_news < - paste0("http://news.naver.com/main/ranking/popularDay.nhn?mid=etc&sid1=111&date=", df_2016_format[d])  # 웹 스크래핑을 할 url을 입력합니다.
news_data < - read_html(url_news)  # 입력된 url에서 html을 읽어옵니다.

section_name < - c("Policy", "Economy", "Society", "Life", "World", "IT", "TV_Ent", "Sports")  # 카테고리 명칭 작성
popular_new_head < - data.frame(head_1=c(1:8), head_2 = NA, head_3 = NA, head_4 = NA, head_5 = NA)  # 헤드라인 5개를 각 카테고리 별로 입력하는 데이터 프레임
rownames(popular_new_head) < - section_name  # row name을 카테고리 명칭으로 변경 (추출하는 csv에서 첫 번째 열에 나타납니다.)

for (i in 1:(ncol(popular_new_head))){  # 1~5면의 헤드에 대한 for문입니다.
find_num < - paste0('.num', i)  # 헤드라인 마다 번호가 다르므로 번호를 바꿀 수 있도록 합니다.
num_head < - html_nodes(news_data, find_num)  # i가 1일 경우, num1에 해당하는 노드를 찾아냅니다.

for (j in 1:nrow(popular_new_head)){  # 정치 ~ 스포츠까지의 카테고리에 대한 for문입니다.
    head_text < - gsub("\t", "", num_head[j] % > % html_text())  # j 번째 노드에서 text를 추출한 후에 탭(\t)을 제거합니다.
head_text < - strsplit(head_text, "\r\n")[[1]]  # text를 "\r\n"으로 나눠줍니다. list로 반환됩니다. vector로 바꾸기 위해 [[1]]을 뒤에 붙여줍니다.
if (i == 1)
{
    popular_new_head[j, i] < - head_text[12]  # 첫 번재 카테고리인 정치의 경우는 12번째에 헤드라인이 들어있습니다. 이를 앞서 설정한 데이터 프레임에 넣어줍니다.
} else {
    popular_new_head[j, i] < - head_text[5]  # 나머지 카테고리들은 5번째에 헤드라인이 들어있습니다. 이를 앞서 설정한 데이터 프레임에 넣어줍니다.
}
}
}
write.csv(popular_new_head,
          paste0(df_2016_format[d], "_popular_news_head.csv"))  # 날짜별로 csv 파일로 저장합니다. 디렉토리 설정을 안하면 문서 폴더 내에 저장됩니다.
}
[출처][R]
네이버
뉴스
웹
페이지
스크래핑(크롤링)
하기 | 작성자
nife0719