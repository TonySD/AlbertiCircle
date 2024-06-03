const myForm = document.getElementById("cipher");

myForm.addEventListener("submit", async (event) => {
  event.preventDefault(); // Предотвращаем стандартное действие отправки формы

  const formData = new FormData(myForm);
  const formObj = Object.fromEntries(formData.entries());
  if (formObj.keychoose == "0") {
	formObj.key = document.getElementById("keyinput1").value;
  }
  if (formObj.keychoose == "1") {
	formObj.key = document.getElementById("keyinput2").value;
  }

	delete formObj.keychoose;
//   const keychoose2 = document.getElementById("keychoose2_btn");

//   delete formObj.keychoose;

//   if (!keychoose2.checked) {
//     delete formObj.keyinput2;
//   }

  const requestOptions = {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(formObj),
  };
  response = NaN;
  try {
    response = await fetch(
      "/mode/",
      requestOptions
    );
    response = await response.json();
  } catch (error) {
    console.error("Ошибка:", error);
  }

  const resultDiv = document.createElement("div");
  resultDiv.innerHTML = `
  <div class="row">
      <div class="col-4"></div>
      <div class="col-4 response">
        <h2>Результат запроса:</h2>
        <p><strong>Шифр-текст:</strong> ${response.ciphertext} </p>
        <p><strong>Ключ:</strong> ${response.key} </p>
        <p><strong>Пароль:</strong> ${response.password} </p>
        <p><strong>Индикаторная буква:</strong> ${response.indicator} </p>
        <p><strong>Результат:</strong> ${response.plaintext} </p>
      </div>
      <div class="col-4"></div>
    </div>`;
  document.body.appendChild(resultDiv);
});
