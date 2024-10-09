#Task1
print('============Task1============')
#*我先將跟成人有關的關鍵字取出來，用if做判斷，
# *若詞句中有出線的話，請幫我判別為成人

def find_and_print(messages):
    for sender, message in messages.items():
        if "legal age" in message or"18" in message or "vote" in message or "college" in message:
            print(f"{sender}")

find_and_print({
    "Bob": "My name is Bob. I'm 18 years old.",
    "Mary": "Hello, glad to meet you.",
    "Copper": "I'm a college student. Nice to meet you.",
    "Leslie": "I am of legal age in Taiwan.",
    "Vivian": "I will vote for Donald Trump next week",
    "Jenny": "Good morning."
})

#Task2
print('============Task2============')
#*因為在salary中，資料類型都不同，有str 有int 有逗號 有匯率
#*所以我先將資料類型都轉換成相同的
#*再去進行計算
#*計算方式只有用performance去評估
def calculate_sum_of_bonus(data):
    bonus_sum = 0
    total_salary = 0

    role_bonus = {      #*新增職位獎金
        "Engineer": 1.2,
        "CEO": 1.5,
        "Sales": 1.1
    }

    for employee in data["employees"]:
        performance = employee["performance"]
        salary = employee["salary"]
        role = employee["role"]

        if isinstance(salary, str) and salary.endswith("USD"):
            salary = float(salary[:-3]) * 30  # 處理 "salary": "1000USD"
            salary = int(salary)
        elif isinstance(salary, str):
            salary = int(salary.replace(",", ""))  # 處理 "salary": "50,000"

        # print(f"Employee: {employee['name']}, Salary: {salary}")

        if performance == "above average":
            bonus = 3000
        elif performance == "average":
            bonus = 2000
        elif performance == "below average":
            bonus = 1000
        else:
            bonus = 0
        
        role_sum = role_bonus.get(role, 1.0)#*乘上對應的職位獎金
        bonus_sum += bonus * role_sum #*bonus*職位獎金 就是將金加總
        total_salary += salary  # 將薪水加總
    total_amount = total_salary + bonus_sum  # 薪水及 bonus 加總
    
    # 顯示結果
    print(f"The sum of bonuses is: {int(bonus_sum):,} TWD")
    print(f"The total amount is: {int(total_amount):,} TWD")



calculate_sum_of_bonus({
    "employees": [
        {
            "name": "John",
            "salary": "1000USD",
            "performance": "above average",
            "role": "Engineer"
        },
        {
            "name": "Bob",
            "salary": 60000,
            "performance": "average",
            "role": "CEO"
        },
        {
            "name": "Jenny",
            "salary": "50,000",
            "performance": "below average",
            "role": "Sales"
        }
    ]
})

print('============Task3============')
#*先將名字第二個字取出，一一進行對比

def func(*data):
    middle_chars = [name[1] for name in data]  #*取出名字中第二個字
    unique_middle_char = None #*放入容器

    for i in range(len(middle_chars)):#*比對不同名字
        if middle_chars.count(middle_chars[i]) == 1:#*計算出現的次數
            unique_middle_char = middle_chars[i]#*如果只出現一次 就取出這個字
            break

    if unique_middle_char:#*取出出現一次的字
        for i in range(len(data)):#*與其他名字對比
            if data[i][1] == unique_middle_char:#*如果剛好與中間的字相符
                result = data[i]#*就回傳全名
                print(result)
                return result
    else:
        result = "沒有"
        print(result)
        return result

func("彭⼤牆", "王明雅", "吳明"); #彭⼤牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花"); #林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); #沒有

print('============Task4============')
#*發現奇數項位每個都+3 如第一項：0 第三項 ：3 第五項：6
#*   偶數項位每個都+3 如第二項：4 第四項 ：7 第六項：10
def get_number(index):
    if index < 1: #*如果index<1回傳沒有
        return None
    elif index % 2 == 1:#*如果index除二於一(奇數項位)
        n = (index + 1) // 2#*在程式中從第零項開始 所以要+1 除2
        result= n * 3 + 1 #* 每個項位都差三 所以找出index是第幾項後 +*3+1
    else:
        n = index // 2#*偶數項位就比較簡單
        result= n * 3
    print(result)
    return result

get_number(1) # print 4
get_number(5) # print 10
get_number(10) # print 15

