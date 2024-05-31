const textinput = document.getElementById("textinput");
const keyinput = document.getElementById("keyinput");
const passinput = document.getElementById("passinput");
const indicatorinput = document.getElementById("indicatorinput");

function resetAllFields() {
    textinput.style.display = "none";
    keyinput.style.display = "none";
    passinput.style.display = "none";
    indicatorinput.style.display = "none";
}

function enableFields(elements) {
    resetAllFields();
    elements.forEach(function(element) {
        element.style.display = "block";
    });
}

const mode1Radio = document.getElementById("mode1Radio");
const mode2Radio = document.getElementById("mode2Radio");
const mode3Radio = document.getElementById("mode3Radio");
const mode4Radio = document.getElementById("mode4Radio");
const mode5Radio = document.getElementById("mode5Radio");

mode1Radio.addEventListener("change", () => {
    if (mode1Radio.checked) {
        enableFields([textinput, keyinput]);
    }
});

mode2Radio.addEventListener("change", () => {
    if (mode2Radio.checked) {
        enableFields([textinput, keyinput]);
    }
});

mode3Radio.addEventListener("change", () => {
    if (mode3Radio.checked) {
        enableFields([textinput, keyinput, indicatorinput]);
    }
});

mode4Radio.addEventListener("change", () => {
    if (mode4Radio.checked) {
        enableFields([textinput, keyinput]);
    }
});

mode5Radio.addEventListener("change", () => {
    if (mode5Radio.checked) {
        enableFields([textinput, keyinput, passinput]);
    }
});

// const keychoose1 = document.getElementById("keychoose1");
// const keychoose2 = document.getElementById("keychoose2");
// const keyinput1 = document.getElementById("keyinput1");
// const keyinput2 = document.getElementById("keyinput2");

// keychoose1.addEventListener("change", () => {
//     if (keychoose1.checked) {
//         keyinput2.disabled = true;
//     }
// });

// keychoose2.addEventListener("change", () => {
//     if (keychoose2.checked) {
//         keyinput2.disabled = false;
//         keyinput2.focus();
//     }
// });