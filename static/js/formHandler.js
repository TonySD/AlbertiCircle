const myForm = document.getElementById("myForm");

myForm.addEventListener("submit", async (event) => {
event.preventDefault(); // Предотвращаем стандартное действие отправки формы

const formData = new FormData(myForm);
const formObj = Object.fromEntries(formData.entries());
const keychoose2 = document.getElementById("keychoose2");

delete formObj.keychoose;

if (!keychoose2.checked) {
    delete formObj.keyinput2;
}

const requestOptions = {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(formObj),
};
response = NaN;
try {
    response = await fetch("/mode/", requestOptions);
    response = await response.json();
} catch (error) {
    console.error("Ошибка:", error);
}

const resultDiv = document.createElement("div");
resultDiv.innerHTML = `
    <h2>Результат запроса:</h2>
    <p><strong>Шифр-текст:</strong> ${response.ciphertext}</p>
    <p><strong>Ключ:</strong> ${response.key}</p>
    <p><strong>Пароль:</strong> ${response.password}</p>
    <p><strong>Индикаторная буква:</strong> ${response.indicator}</p>
    <p><strong>Результат:</strong> ${response.plaintext} </p>
`;
document.body.appendChild(resultDiv);
});