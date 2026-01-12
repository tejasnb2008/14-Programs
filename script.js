const total = 14;
const container = document.getElementById("container");

for (let i = 1; i <= total; i++) {
  fetch(`programs/program_${i}.${i==13||i==14?"sql":"py"}`)
    .then(r => r.text())
    .then(code => {
      const box = document.createElement("div");
      box.className = "box";

      box.innerHTML = `
        <h3>Program ${i}</h3>
        <pre>${code}</pre>
        <a class="btn" href="programs/program_${i}.${i==13||i==14?"sql":"py"}" download>Download</a>
      `;

      container.appendChild(box);
    });
}
