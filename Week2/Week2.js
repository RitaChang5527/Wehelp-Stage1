console.log("============Task1============");
//*我先將跟成人有關的關鍵字取出來，用if做判斷，
// *若詞句中有出線的話，請幫我判別為成人

function findAndPrint(messages) {
    for (let sender in messages) {
        let message = messages[sender]; //*[sender]傳送訊息的人
        if (//*如果有包含這些字的話
            message.includes("legal age") ||
            message.includes("18") ||
            message.includes("vote") ||
            message.includes("college")
        ) {
            console.log(sender);//*就回傳sender
        }
        }
    }
    findAndPrint({
        Bob: "My name is Bob. I'm 18 years old.",
        Mary: "Hello, glad to meet you.",
        Copper: "I'm a college student. Nice to meet you.",
        Leslie: "I am of legal age in Taiwan.",
        Vivian: "I will vote for Donald Trump next week",
        Jenny: "Good morning.",
    });
console.log("============Task2============");
//*因為在salary中，資料類型都不同，有str 有int 有逗號 有匯率
//*所以我先將資料類型都轉換成相同的
//*再去進行計算
//*計算方式只有用performance去評估
function calculateSumOfBonus(data) {
    let bonusSum = 0;
    let totalSalary = 0;
  
    const roleBonus = {
      Engineer: 1.2,
      CEO: 1.5,
      Sales: 1.1,
    };
  
    for (const employee of data.employees) {
      const performance = employee.performance;//*建立資料變數performance
      let salary = employee.salary;//*建立資料變數salary
      const role = employee.role;//*建立資料變數role
  
      if (typeof salary === "string" && salary.endsWith("USD")) {//*處理"salary": "1000USD",
        salary = parseFloat(salary.slice(0, -3)) * 30;
        salary = parseInt(salary);
      } else if (typeof salary === "string") {//*處理"salary": 60000,
        salary = parseInt(salary.replace(/,/g, ""));//*(/,/g, ""))用意是全部的逗號都會被替換 不是只有第一個
      }
  
      let bonus = 0;
  
      if (performance === "above average") {
        bonus = 3000;
      } else if (performance === "average") {
        bonus = 2000;
      } else if (performance === "below average") {
        bonus = 1000;
      }
  
      const roleSum = roleBonus[role] || 1.0;//*乘上對應的職位獎金
      bonusSum += bonus * roleSum;//*bonus乘上職位獎金
      totalSalary += salary;//*薪水加總
    }
  
    const totalAmount = totalSalary + bonusSum;//*加薪總額
  
    // 顯示結果
    console.log(`The sum of bonuses is: ${bonusSum.toLocaleString()} TWD`);//*toLocaleString轉換成特定形式
    console.log(`The total amount is: ${totalAmount.toLocaleString()} TWD`);
  }
  
  calculateSumOfBonus({
    employees: [
      {
        name: "John",
        salary: "1000USD",
        performance: "above average",
        role: "Engineer",
      },
      {
        name: "Bob",
        salary: 60000,
        performance: "average",
        role: "CEO",
      },
      {
        name: "Jenny",
        salary: "50,000",
        performance: "below average",
        role: "Sales",
      },
    ],
  });
  

console.log("============Task3============");


    function func(...data) {//*有多組參數
    let middle_chars = data.map(name => name[1]);//*取第二個字
    let unique_middle_char = null;//*設定一個空間

    for (let i = 0; i < middle_chars.length; i++) {//*判斷第二個字是不是只出現過一次
    if (middle_chars.filter(char => char === middle_chars[i]).length === 1) {
        //*比較每個字的第二個字 如果長度為1 就可以確定那個字只出現過一次
        unique_middle_char = middle_chars[i];//*將那個字丟進unique_middle_char
        break;
    }
}

    if (unique_middle_char) {//*如果只出現過一次的字
    for (let i = 0; i < data.length; i++) {//*進行找出人名的迴圈
        if (data[i][1] === unique_middle_char) {//*尋找剛剛只出現過一次的第二個字 回傳人名
        let result = data[i];//*找到人名
        console.log(result);
        return result;
        }
    }
} else {
    let result = "沒有";
    console.log(result);
    return result;
    }
}

func("彭⼤牆", "王明雅", "吳明"); //彭⼤牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花"); // 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // 沒有

console.log("============Task4============");
//*發現奇數項位每個都+3 如第一項：0 第三項 ：3 第五項：6
//*   偶數項位每個都+3 如第二項：4 第四項 ：7 第六項：10
function getNumber(index) {
    let result;
    if (index < 1) {
        result = null; //*<1不做判斷式
    } else if (index % 2 === 1) {//*奇數項位
        let n = Math.floor((index + 1) / 2); //*找出是第幾項位
        result = n * 3 + 1;//*每個項位差三 先乘3再加1
    } else {
        let n = index / 2;//*偶數項位
        result = n * 3;//*直接乘3
    }

    console.log(result);
    return result;
}

getNumber(1); // print 4
getNumber(5); // print 10
getNumber(10); // print 15
