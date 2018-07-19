print("==============================")

def get_number_of_subjects():
    print("과목수를 입력하세요: ")
    number = int(input())
    return number

study_list = get_number_of_subjects()
study_score = 0

for i in range(1, study_list + 1):
    print("%d번째 과목의 점수를 입력하세요 : " % i)
    study_score += int(input())

def get_average_score(study_score, study_list):
    result = study_score/study_list
    return result

study_avg = get_average_score(study_score, study_list)

print("평균 점수: %f" % study_avg )
if(study_avg >= 90):
    print("학점: A")
elif( study_avg>=80):
    print("학점: B")
elif (study_avg>=70):
    print("학점: C")
elif(study_avg >=60):
    print("학점: D")
else:
    print("학점: F")

print("==============================")
