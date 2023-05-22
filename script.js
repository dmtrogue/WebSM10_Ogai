alert("Вы попадаете на сайт главного производителя деталей в РФ")



console.log("Easter egg",a*b)

function myfunction() {
    n = document.getElementById("in_name").value;
    a = document.getElementById("in_age").value;
    response = n +" "+ a + " лет"+" вступил в ряды нашей кафедры"
    alert(response)

    t=document.getElementById("mytable")
    var row = t.insertRow(4);
    var c_name = row.insertCell(0);
    var c_photo = row.insertCell(1);
    var c_task = row.insertCell(2);
    var c_salary = row.insertCell(3);
    c_name.innerHTML = n;
    c_photo.innerHTML = '<img src="./dog2.jpg" width="200"></img>';
    c_task.innerHTML = "Главный сборщик";
    c_salary.innerHTML = "5000";

    
    

}