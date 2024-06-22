function toggleDropdown() {
    var dropdown = document.getElementById("myDropdown");
    if (dropdown.style.display === "none") {
        dropdown.style.display = "block";
    } else {
        dropdown.style.display = "none";
    }
}

window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        for (var i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.style.display === "block") {
                openDropdown.style.display = "none";
            }
        }
    }
}

// JavaScript код
document.addEventListener("DOMContentLoaded", function() {
    // Проверяем количество досок при загрузке страницы
    checkBoardCount();
});

function checkBoardCount() {
    // Получаем количество досок
    var boardCount = document.querySelectorAll(".board-card").length;
    // Если количество досок больше 4, скрываем пустую доску для добавления новой
    if (boardCount >= 50) {
        document.getElementById("add-board-card").style.display = "none";
    } else {
        document.getElementById("add-board-card").style.display = "block";
    }
}

// Получаем элемент пустой доски
const emptyCard = document.getElementById('empty-card');

// Обработчик события для добавления нового списка
emptyCard.addEventListener('click', () => {
    // Перемещаем пустую доску направо с помощью анимации
    emptyCard.style.animation = 'moveRight 0.3s ease-in-out forwards';
});

// static/task_manager/js/script.js

// Логика для боковой панели
function openNav() {
    document.getElementById("mySidebar").style.width = "250px";
    document.getElementById("mainContent").style.marginLeft = "250px";
}

function closeNav() {
    document.getElementById("mySidebar").style.width = "0";
    document.getElementById("mainContent").style.marginLeft = "0";
}

$('.delete-board').on('click', function () {
    let is_delete = confirm('udalit?');
    console.log(is_delete);
});

