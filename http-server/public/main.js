testForm.onsubmit = function(e) {
  submitBtn.disabled = true;
  e.preventDefault();

  const formData = new FormData(testForm);
  setTimeout(function() {
    var xhr = new XMLHttpRequest();
    xhr.open(testForm.method, testForm.action, true);
    xhr.send(formData);
  }, 1000);
};
