const token = localStorage.getItem('jwt'); // Получаем токен из localStorage

fetch('/protected-route', {
    method: 'GET',
    headers: {
        'Authorization': `Bearer ${token}`, // Передаем токен в заголовке
        'Content-Type': 'application/json'
    }
})