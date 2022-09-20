var input = document.getElementById("main__div-input");
var resultDiv = document.getElementById("result__div");
var accountNumber;

var PaymentFormHTML = (clientName) => {
    return `
    <div class="result__from-js">
    <div>
        <div> <strong>Фамилия:</strong> ${clientName}</div>
        <div style="display: flex;">
            <div>
                Сумма платежа
            </div>
            <div style="margin-left: 20px;">
                <input type"number" class="result__from-js-input-sum" id="amount-id"> сом.
            </div>
        </div>
    </div>
    <div> 
        <button onclick="but()" class="result__from-js__button">Оплатить</button>
    </div>
    </div>
`
}

const print = () => {
    const request = new Request('http://127.0.0.1:8000/api/check-account', {
        method: 'POST',
        body: JSON.stringify({
            "account_number": parseInt(input.value)
        })
    });


    fetch(request)
        .then((response) => response.json())
        .then((data) => {
            if (data.success === true) {
                clientName = data.message;

                resultDiv.innerHTML = PaymentFormHTML(clientName, "London");
                accountNumber = input.value;
                input.value = "";

                return data;
            } else {
                input.value = " ";
                resultDiv.innerHTML = data.message;
            }
        }).catch(error => {
            console.log("error");
            console.error(error);
        });
}

var but = () => {
    var input_amount = document.getElementById("amount-id");

    const body_data = JSON.stringify({
        account_number: parseInt(accountNumber),
        amount: parseInt(input_amount.value)
    });

    console.log(body_data);

    const request = new Request('http://127.0.0.1:8000/api/make-payment', {
        method: 'POST',
        body: body_data
    });

    fetch(request)
        .then((response) => response.json())
        .then((data) => {
            if (data.success === true) {
                input_amount.value = "";
                resultDiv.innerHTML += `<h6>${data.message}</h6>`;
            } else {
                resultDiv.innerHTML += `<h6>${data.message}</h6>`;
            }
        }).catch(error => {
            console.error(error);
        });

}