const lists = document.querySelectorAll('li');
lists.forEach(list => console.log(list));

const createListItem = (text, href = '#') => {
    const li = document.createElement('li');
    const a = document.createElement('a');
    a.href = href;
    a.textContent = text;
    li.appendChild(a);
    return li;
}

const ul = document.querySelector('ul');
ul.appendChild(createListItem('NewList'));