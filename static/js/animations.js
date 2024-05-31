const textinput = document.getElementById("textinput");
      const keyinput = document.getElementById("keyinput");
      const passinput = document.getElementById("passinput");
      const indicatorinput = document.getElementById("indicatorinput");

      const mode1Radio = document.getElementById("mode1Radio");
      const mode2Radio = document.getElementById("mode2Radio");
      const mode3Radio = document.getElementById("mode3Radio");
      const mode4Radio = document.getElementById("mode4Radio");
      const mode5Radio = document.getElementById("mode5Radio");

      mode1Radio.addEventListener("change", () => {
        if (mode1Radio.checked) {
          textinput.style.display = "block";
          keyinput.style.display = "block";
          passinput.style.display = "none";
          indicatorinput.style.display = "none";
        }
      });

      mode2Radio.addEventListener("change", () => {
        if (mode2Radio.checked) {
          textinput.style.display = "block";
          keyinput.style.display = "block";
          passinput.style.display = "none";
          indicatorinput.style.display = "none";
        }
      });

      mode3Radio.addEventListener("change", () => {
        if (mode3Radio.checked) {
          textinput.style.display = "block";
          keyinput.style.display = "block";
          passinput.style.display = "none";
          indicatorinput.style.display = "block";
        }
      });

      mode4Radio.addEventListener("change", () => {
        if (mode4Radio.checked) {
          textinput.style.display = "block";
          keyinput.style.display = "block";
          passinput.style.display = "none";
          indicatorinput.style.display = "none";
        }
      });

      mode5Radio.addEventListener("change", () => {
        if (mode5Radio.checked) {
          textinput.style.display = "block";
          keyinput.style.display = "block";
          passinput.style.display = "block";
          indicatorinput.style.display = "none";
        }
      });

      const keychoose1 = document.getElementById("keychoose1");
      const keychoose2 = document.getElementById("keychoose2");
      const keyinput1 = document.getElementById("keyinput1");
      const keyinput2 = document.getElementById("keyinput2");

      keychoose1.addEventListener("change", () => {
        if (keychoose1.checked) {
          keyinput2.disabled = true;
        }
      });

      keychoose2.addEventListener("change", () => {
        if (keychoose2.checked) {
          keyinput2.disabled = false;
          keyinput2.focus();
        }
      });