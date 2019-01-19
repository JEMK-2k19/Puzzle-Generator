/**
document.addEventListener('DOMContentLoaded', () => {
  setInterval(count, 1000);
});
*/
document.addEventListener('DOMContentLoaded', function() {
  document.querySelector('button').onclick = count;
  /* document.querySelector('#blue').onclick = function() {
    document.querySelector('#counter').style.color = 'blue';
  };
  document.querySelector('#green').onclick = function() {
    document.querySelector('#counter').style.color = 'green';
  };
  */
  document.querySelectorAll('.color-change').forEach(function(button) {
    button.onclick = () => {
      document.querySelector('#counter').style.color = button.dataset.color;
    }
  });
  document.querySelector('#color-change').onchange = function() {
      document.querySelector('#counter').style.color = this.value;
  };

  document.querySelector('#task').onkeyup = () => {
    if (document.querySelector('#task').value.lenth > 0) {
      document.querySelector('#submit').disabled = false;
    } else {
      document.querySelector('#submit').disabled = true;
    }
  }

  document.querySelector("#new-task").onsubmit = () => {
    const li = document.createElement('li');
    li.innerHTML = document.querySelector('#task').value;

    document.querySelector('#tasks').append(li);
    document.querySelector('#task').value = '';
    return false;
  }
});
