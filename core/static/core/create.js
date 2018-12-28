var update_button = document.getElementById("add");
var year = document.getElementById("id_year");
var gas = document.getElementById("id_gas");
var modal = document.getElementById('myModal');
var btn = document.getElementById("myBtn");
var span = document.getElementsByClassName("close")[0];
var form_create = document.getElementById("form_create");

btn.onclick = function(e) {
    modal.style.display = "block";
};

span.onclick = function() {
    modal.style.display = "none";
};

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
};

$("#id_year").on('click', function () {
    $("#id_year").removeClass('error');
});

$("#id_gas").on('click', function () {
    $("#id_gas").removeClass('error');
});

update_button.onclick = function (e) {
    e.preventDefault();

    const formData = new FormData(form_create);

    y = parseInt(year.value);
    g = parseInt(gas.value);

    $("#id_year").removeClass('error');
    $("#id_gas").removeClass('error');

    console.log(100)

    if (!(y < 1000 || y > 2018 || g < 0)) {
        $.ajax({
            type: 'POST',
            url: '/car/create/',
            data: formData,
            processData: false,
            contentType: false,

            success: (result) => {
              modal.style.display = "none";
              $("#cars").prepend(result);
            },

            error: (result) => {
              alert('Ошибка')
            }
        });
    }
    if (y < 1000 || y > 2018) {
        $("#id_year").addClass('error');
    }
    if (g < 0) {
        $("#id_mileage").addClass('error');
    }
};