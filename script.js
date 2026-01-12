const base =
  "https://raw.githubusercontent.com/tejasnb2008/14-Programs/main/programs/";

const files = [
  "program_1.py",
  "program_2.py",
  "program_3.py",
  "program_4.py",
  "program_5.py",
  "program_6.py",
  "program_7.py",
  "program_8.py",
  "program_9.py",
  "program_10.py",
  "program_11.py",
  "program_12.py",
  "program_13.sql",
  "program_14.sql"
];

const container = document.getElementById("container");

files.forEach((file, index) => {
  fetch(base + file)
    .then((res) => {
      if (!res.ok) {
        throw new Error("File not found");
      }
      return res.text();
    })
    .then((code) => {
      const box = document.createElement("div");
      box.className = "box";

      box.innerHTML = `
        <h3>${index + 1}. ${file}</h3>
        <pre>${code}</pre>
        <a class="btn" href="${base + file}" download="${file}">Download</a>
      `;

      container.appendChild(box);
    })
    .catch((err) => {
      console.error("Failed to load:", file, err);
    });
});
