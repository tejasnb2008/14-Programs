const raw =
  "https://raw.githubusercontent.com/tejasnb2008/14-Programs/main/programs/";

const proxy = "/.netlify/functions/fetch?url=";

const programs = [
  { file: "program_1.py",  title: "Fibonacci Series" },
  { file: "program_2.py",  title: "Factorial & Sum" },
  { file: "program_3.py",  title: "Simple & Compound Interest" },
  { file: "program_4.py",  title: "Vowel & Case Counter" },
  { file: "program_5.py",  title: "File Details" },
  { file: "program_6.py",  title: "Bubble Sort" },
  { file: "program_7.py",  title: "Selection Sort" },
  { file: "program_8.py",  title: "Insertion Sort" },
  { file: "program_9.py",  title: "Linear Search" },
  { file: "program_10.py", title: "Binary Search" },
  { file: "program_11.py", title: "Stack" },
  { file: "program_12.py", title: "Queue" },
  { file: "program_13.sql", title: "BESCOM SQL" },
  { file: "program_14.sql", title: "Student SQL" }
];

const container = document.getElementById("container");

programs.forEach((p, i) => {
  fetch(proxy + encodeURIComponent(raw + p.file))
    .then(res => res.text())
    .then(code => {
      const box = document.createElement("div");
      box.className = "box";

      box.innerHTML = `
        <h3>${i + 1}. ${p.title}</h3>
        <pre>${code}</pre>
        <a class="btn" href="${raw + p.file}" download>Download</a>
      `;

      container.appendChild(box);
    })
    .catch(() => {
      console.log("Failed:", p.file);
    });
});
