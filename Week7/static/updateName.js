document.addEventListener("DOMContentLoaded", () => {
    const updateNameButton = document.getElementById("updateNameButton");
    const newNameInput = document.getElementById("newNameInput");
    const updateResult = document.getElementById("updateResult");

    updateNameButton.addEventListener("click", () => {
        const newName = newNameInput.value.trim();

        if (newName) {
            fetch("/api/member", {
                method: "PATCH",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ name: newName })
            })
            .then(response => response.json())
            .then(data => {
                if (data.ok) {
                    updateResult.innerHTML = "姓名更新成功";
                } else {
                    updateResult.innerHTML = "姓名更新失敗";
                }
            })
            .catch(error => {
                console.error("Error:", error);
                updateResult.innerHTML = "更新姓名時出現錯誤";
            });
        } else {
            updateResult.innerHTML = "請輸入新的使用者姓名";
        }
    });
});
