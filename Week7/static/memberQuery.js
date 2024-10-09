document.addEventListener("DOMContentLoaded", () => {
    const queryButton = document.getElementById("queryButton");
    const usernameInput = document.getElementById("usernameInput");
    const memberInfo = document.getElementById("memberInfo");

    queryButton.addEventListener("click", () => {
        const username = usernameInput.value.trim();

        if (username) {
            fetch(`/api/member?username=${username}`)
                .then(response => response.json())
                .then(data => {
                    if (data.data) {
                        const memberData = data.data;
                        const memberInfoHTML = `
                            <div>${memberData.name}(${memberData.username})</div>
                        `;
                        memberInfo.innerHTML = memberInfoHTML;
                        console.log("Button clicked!");
                    } else {
                        memberInfo.innerHTML = "查無該會員資料";
                    }
                })
                .catch(error => {
                    console.error("Error:", error);
                    memberInfo.innerHTML = "查詢會員資料時出現錯誤";
                });
        } else {
            memberInfo.innerHTML = "請輸入要查詢的會員帳號";
        }
    });
});
