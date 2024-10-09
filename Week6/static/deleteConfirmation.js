function confirmDelete(userId, messageId) {
    if (confirm("確定要刪除此留言嗎？")) {
        fetch('/deleteMessage', {
            method: 'POST',
            body: new URLSearchParams({
                message_id: messageId,
                user_id: userId
            }),
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                window.location.reload();  // Refresh the page after successful deletion
            } else {
                alert("刪除失敗，您無權刪除此留言。");
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert("刪除留言時出現錯誤。");
        });
    }
}
