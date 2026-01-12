const files = [
  "fibonacci.py","factorial_sum.py","interest.py","file_vowels.py",
  "file_details.py","bubble_sort.py","selection_sort.py","insertion_sort.py",
  "linear_search.py","binary_search.py","stack.py","queue.py","bescom.sql","student.sql"
];

files.forEach((file,i)=>{
  fetch("programs/"+file)
    .then(r=>r.text())
    .then(t=> document.getElementById("p"+(i+1)).textContent=t );
});
