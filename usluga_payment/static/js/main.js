var input = document.getElementById("main__div-input");
var resultDiv = document.getElementById("result__div");

var but = () => {
    console.log("success")
}



var clientName = "Elizoveta";
var clientStyle = "London";

var text = `<div class="result__from-js">
<div> 
<div> <strong>Фамилия:</strong> ${clientName}</div>
<div> <strong>Адрес:</strong> ${clientStyle}</div>
<div style="display: flex;">
<div>
Сумма платежа
</div>
<div style="margin-left: 20px;">
<input type"number" class="result__from-js-input-sum"> сом.
</div>
</div>
</div>

<div> 
<button onclick="but()" class="result__from-js__button">Оплатить</button>
</div>

</div>
`

const print = () => {
    console.log(input.value);
    resultDiv.innerHTML = text;
    input.value = " "
}