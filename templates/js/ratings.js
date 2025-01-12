const ratingButtons = document.querySelectorAll('.rating-buttons');

ratingButtons.forEach(button => {
    button.addEventListener('click', event => {
        // Получаем действие (like или dislike) из data-атрибута кнопки
        const action = event.target.dataset.action; // 'like' или 'dislike'
        const postId = parseInt(event.target.dataset.post);
        const likesCountElement = button.querySelector('.likes-count');
        const dislikesCountElement = button.querySelector('.dislikes-count');

        // Создаем объект FormData для отправки данных на сервер
        const formData = new FormData();
        formData.append('post_id', postId);
        formData.append('action', action); // Отправляем действие (like/dislike)

        // Отправляем AJAX-запрос на сервер
        fetch("/rating/", {
            method: "POST",
            headers: {
                "X-CSRFToken": csrftoken,
                "X-Requested-With": "XMLHttpRequest",
            },
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            // Обновляем значения лайков и дизлайков на странице
            likesCountElement.textContent = data.likes_count;
            dislikesCountElement.textContent = data.dislikes_count;
        })
        .catch(error => console.error(error));
    });
});