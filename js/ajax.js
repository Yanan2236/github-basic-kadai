const url = 'https://jsonplaceholder.typicode.com/posts';

const button = document.querySelector('#ajax-btn');

button.addEventListener('click', () => {
    const dummyData = { name: '侍太郎', age: 30 };
    fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(dummyData)
    })
        .then(response => response.json())
        .then(data => console.log('サーバーからの応答：\n' + JSON.stringify(data, null, 2)));
});
