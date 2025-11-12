const btn = document.querySelector("#output-btn");
const addBtn = document.querySelector("#add-btn");
const ul = document.querySelector("#parent-list");

const createListItem = (text) => {
  const li = document.createElement("li");
  li.textContent = text;
  return li;
};

btn.addEventListener("click", () => {
  console.log("クリックされました！");
});

addBtn.addEventListener("click", () => {
  ul.appendChild(createListItem("これはリスト要素です"));
});

const countBtn = document.querySelector("#count-btn");
countBtn.addEventListener("click", () => {
  const textForm = document.querySelector("#text-box");
  console.log(textForm.value.length + "文字");
});

const areaBtn = document.querySelector("#area-btn");
areaBtn.addEventListener("click", () => {
  const area = document.querySelector('input[name="area"]:checked');
  console.log(area.value);
});
