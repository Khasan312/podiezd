from datetime import datetime

css_text = """ /* ALL */
        *,
        *::after,
        *::before {
          margin: 0;
          padding: 0;
          box-sizing: border-box;
        }

        /* ALL END  */

        /* CONTAINER */

        .container {
          width: 750px;
          margin: 100px auto;

          font-family: "Roboto Condensed", sans-serif;
        }

        /* CONTAINER END */

        /* HEADER */

        .header__div {
          background-color: #f5f5f5;
          border: 1px solid #ddd;
          border-radius: 6px 6px 0 0;
        }

        .header__div-item-label {
          font-size: 18px;
          font-weight: 700;
          margin: 0 0 2px 35px;
        }

        .main__div-text {
          font-size: 18px;
        }

        /* HEADER END */

        /* MAIN */

        .main {
          width: 750px;
          height: 100%;
          min-height: 210px;
          background-color: #f5f5f5;
          border: 1px solid #ddd;
          border-radius: 0 0 6px 6px;
        }

        .main__div {
          margin: 15px 0px 0px 35px;
          display: flex;
          flex-wrap: wrap;
        }

        .main__div-text {
          margin-top: 1px;
        }

        .main__div-input-type {
          margin-left: 40px;
          margin-top: 0px;
        }

        .main__div-input {
          width: 200px;
          height: 30px;
          border: 1px solid #ddd;
          border-radius: 6px;
          padding: 5px;
        }

        .main__div-input:focus {
          box-shadow: 1px 1px 10px #008000;
        }

        .main__div-button-type {
          margin: 2px 0px 0px 40px;
        }

        .main__div-button {
          width: 95px;
          height: 28px;
          border-radius: 6px;
          border: 1px solid #ddd;
        }

        .main__div-button:hover {
          background-color: bisque;
        }
        .main__div-button:active {
          background-color: #fff;
        }

        .result__from-js {
          width: 75%;
          margin: 20px 0;
          line-height: 2;
          display: flex;
          justify-content: space-around;
        }

        .result__from-js__button {
          width: 95px;
          height: 28px;
          border-radius: 6px;
          border: 1px solid #ddd;
        }

        .result__from-js__button:hover {
          background-color: bisque;
        }
        .result__from-js__button:active {
          background-color: #fff;
        }

        .result__from-js-input-sum {
          width: 130px;
          height: 30px;
          border: 1px solid #ddd;
          border-radius: 6px;
          padding: 5px;
        }

        .result__from-js-input-sum:focus {
          box-shadow: 1px 1px 10px #008000;
        }

        #cancel-payment{
          width: 95px;
          height: 28px;
          border-radius: 6px;
          border: 1px solid #ddd;
          /* margin-top : 50px; */
          /* margin-left : 5%; */
        }
        #cancel-payment:hover {
          background-color: bisque;
        }
        .cancel-payment:active {
          background-color: #fff;
        }

        #close-window, #back-to-acc{
          width: 95px;
          height: 28px;
          border-radius: 6px;
          border: 1px solid #ddd;
          /* margin-left : 56%; */
        }


        #close-window:hover, #back-to-acc:hover {
          background-color: bisque;
        }
        #close-window:active {
          background-color: #fff;
        }

        #cancel-transaction{
          width: 200px;
          height: 30px;
          border: 1px solid #ddd;
          border-radius: 6px;
          padding: 5px;
          margin-left : 23%;
        }



        #cancel-payment-button{
          width: 120px;
          height: 33px;
          border-radius: 6px;
          border: 1px solid #ddd;
          width: auto;
          margin-bottom: 20%;
        }
        #cancel-payment-button:hover {
          background-color: bisque;
        }
        #cancel-payment-button:active {
          background-color: #fff;
        }

        #cancel-transaction-text{
          font-size: 18px;
          margin-left: 30px;
        }

    """


def js_file2():
    return """function cancelFormHTML() {
    var text =
        `<div style="display:flex; justify-content: space-evenly">
              <strong id='cancel-transaction-text'> ???????????? ????????????????????</strong>
              <p><input type="number" min="0" id="cancel-transaction" placeholder="?????????? ????????????????????"</p>
              <div><button  id="cancel-payment-button" onclick="cancelPayment()">???????????????? ????????????????????</button></div>
              <h2 id='customerName' ></h2>
            </div>`
    return text;
}


function cancelTransactionFormHTML(clientName) {
    // cancelButton = document.getElementById('cancel-payment-button')
    var text =
        '<div class="result__from-js">' +
        "<div>" +
        "<div>" +
        "<strong>" +
        "??????????????:</strong> " +
        clientName +
        "</div>"

    return text;

}

function cancelPayment() {
    var customerNameDiv = document.getElementById('customerName');
    customerNameDiv.innerText = customerName
    var cancelTrn = document.getElementById("cancel-transaction");
    var inputNumber = cancelTrn.value;
    var jsonRandomNumber = JSON.stringify({
        transaction_id: inputNumber,
        operator_id: operator_id,
    });

    var xhr_can = new XMLHttpRequest();

    xhr_can.open("POST", urlcancelAccount, true);
    // xhr_can.setRequestHeader("x-csrf-token", getCookie("csrftoken"));
    xhr_can.setRequestHeader("Accept", "application/json");
    xhr_can.setRequestHeader(
        "Content-Type",
        "application/json; charset=utf-8"
    );
    xhr_can.responseType = "json";



    xhr_can.send(jsonRandomNumber);

    xhr_can.onload = function() {
        var cancelObj = xhr_can.response;
        cancelDiv.innerHTML = cancelFormHTML();

    };
}

function openInput() {
    main = document.getElementsByClassName('main__div')[0];
    var back = document.getElementById('back-to-acc')
    cancelDiv.innerHTML = cancelFormHTML();
    main.style.display = "none";
    back.style.display = 'block'
}

function openAccountNumber() {
    main = document.getElementsByClassName('main__div')[0]
    var back = document.getElementById('back-to-acc')
    cancelDiv.innerHTML = '';
    main.style.display = "flex"
    back.style.display = 'none'
}"""


def js_file(
    cashregister_id=None,
    kiosk_id=None,
    receipt_id=None,
    productcode=None,
    partner_id=None,
    user_name=None,
    signature=None,
):

    return """var input = document.getElementById("main__div-input");
var resultDiv = document.getElementById("result__div");
var cancelDiv = document.getElementById("cancel-payment-div");
var accountNumber;
var urlCheckAccount = "http://192.168.3.190:8000/api/check-account?cashregister_id=%(cashregister_id)d&kiosk_id=%(kiosk_id)d&receipt_id=%(receipt_id)d&productcode=2280001003660&language=ru&partner_id=%(partner_id)d&user_name=%(user_name)d&time=%(user_name)s&signature=%(user_name)d";
var urlpayAccount = "http://192.168.3.190:8000/api/make-payment?cashregister_id=%(cashregister_id)d&kiosk_id=%(kiosk_id)d&receipt_id=%(receipt_id)d&productcode=2280001003660&language=ru&partner_id=%(partner_id)d&user_name=%(user_name)d&time=%(user_name)s&signature=%(user_name)d";
var urlcancelAccount = "http://192.168.3.190:8000/api/cancel-payment?cashregister_id=%(cashregister_id)d&kiosk_id=%(kiosk_id)d&receipt_id=%(receipt_id)d&productcode=2280001003660&language=ru&partner_id=%(partner_id)d&user_name=%(user_name)d&time=%(user_name)s&signature=%(user_name)d";
var urlOperatorInfo = "http://192.168.3.190:8000/api/operator-info?cashregister_id=%(cashregister_id)d&kiosk_id=%(kiosk_id)d&receipt_id=%(receipt_id)d&productcode=2280001003660&language=ru&partner_id=%(partner_id)d&user_name=%(user_name)d&time=%(user_name)s&signature=%(user_name)d";
var customerName;


function CookiesDelete() {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i];
        var eqPos = cookie.indexOf("=");
        var name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
        document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT;";
        document.cookie = name + '=; path=/; expires=Thu, 01 Jan 1970 00:00:01 GMT;';
    }
}


function getParameterByName(name) {
    var url =
        arguments.length <= 1 || arguments[1] === undefined ?
        window.location.href :
        arguments[1];

    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return "";
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}

var cashregister_id = getParameterByName("cashregister_id");
var kiosk_id = getParameterByName("kiosk_id");
var receipt_id = getParameterByName("receipt_id");
var partner_id = getParameterByName("partner_id");
var operator_id;

// transaction related info
var transaction_id;

// var urlCheckAccount = 'http://127.0.0.1:8000/api/check-account';
// var urlpayAccount = 'http://127.0.0.1:8000/api/make-payment';
// var urlcancelAccount = 'http://127.0.0.1:8000/api/make-payment';

function getOperatorId() {
    var request = new XMLHttpRequest();
    var params = JSON.stringify({
        cashregister_id: cashregister_id,
        kiosk_id: kiosk_id,
        receipt_id: receipt_id,
        partner_id: partner_id,
    });

    request.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            console.log(this.response.operator_id);
            operator_id = this.response.operator_id;
        }
    };

    request.open("POST", urlOperatorInfo);
    request.setRequestHeader("Content-Type", "application/json");
    request.responseType = "json";
    request.send(params);
}

// get the current operator backend ID
getOperatorId();

function btnClose() {
    window.close();
}

function paymentFormHTML(clientName) {
    var text =
        '<div class="result__from-js">' +
        "<div>" +
        "<div>" +
        "<strong>" +
        "??????????????:</strong> " +
        clientName +
        "</div>" +
        '<div style="display: flex;">' +
        "<div>" +
        "?????????? ??????????????" +
        "</div>" +
        '<div style="margin-left: 20px;">' +
        '<input type"number" class="result__from-js-input-sum" id="amount-id"> ??????.' +
        "</div>" +
        "</div>" +
        "</div>" +
        "<div>" +
        '<button onclick="make_payment()" class="result__from-js__button">????????????????</button>' +
        "</div>" +
        '</div>"';
    return text;
}

function getInfo() {
    // console.log(checkAccountInput.value);
    var inputNumber = input.value;
    var jsonIdStudent = JSON.stringify({
        account_number: inputNumber,
        operator_id: operator_id,
    });

    var xhr_gi = new XMLHttpRequest();

    xhr_gi.open("POST", urlCheckAccount);
    xhr_gi.setRequestHeader("Content-Type", "application/json");
    xhr_gi.responseType = "json";
    xhr_gi.send(jsonIdStudent);

    // ???????? ????????????
    xhr_gi.onload = function() {
        var responseObj = xhr_gi.response;

        console.log(xhr_gi.status);

        if (xhr_gi.status == 200) {
            resultDiv.innerHTML = paymentFormHTML(responseObj.customer.name);

            // set transaction_id
            transaction_id = responseObj.transaction.transaction_number;
        } else if (xhr_gi.status == 403) {
            resultDiv.innerHTML = "Something went wrong, please try ag";
        } else {
            console.log("");
        }
    };
    // checkAccountInput.value = "";
}

function make_payment() {
    var input_amount = document.getElementById("amount-id");

    var body_data = JSON.stringify({
        account_number: input.value,
        amount: parseInt(input_amount.value),
        transaction_num: transaction_id,
        operator_id: operator_id,
    });

    console.log("Send payment request....");

    xhr_mp = new XMLHttpRequest();

    if (input_amount.value <= 0) {
        resultDiv.innerHTML +=
            '<h4 style="color: red; text-align:center;">?????????????? ?????????? ???????????? ?????? ????????</h4>';
    } else if (isNaN(input_amount.value)) {
        resultDiv.innerHTML +=
            '<h4 style="color: red; text-align:center;">???????????? ??????????!</h4>';
    } else {
        console.log("initiating request....");
        xhr_mp.open("POST", urlpayAccount);
        xhr_mp.setRequestHeader("Content-Type", "application/json");
        xhr_mp.send(body_data);
        xhr_mp.onload = function() {
            var responseObjpay = JSON.parse(xhr_mp.response);
            if (responseObjpay.success == true) {
                input_amount.value = "";
                resultDiv.innerHTML +=
                    '<h4 style="text-align:center;">' +
                    responseObjpay.message +
                    "</h4>";
                // window.close();
            } else {
                if (responseObjpay.detail.status == "False") {
                    input.value = "";
                    resultDiv.innerHTML +=
                        '<h4 style="text-align:center;">' +
                        "???????????? ???? ????????????" +
                        "</h4>";
                }
                // resultDiv.innerHTML +=
                //   '<h5 style="text-align:center;>???????????? ???? ????????????</h5>';
            }
        };
    }
}""" % {
        "cashregister_id": cashregister_id,
        "kiosk_id": kiosk_id,
        "receipt_id": receipt_id,
        "productcode": productcode,
        "partner_id": partner_id,
        "user_name": user_name,
        "signature": signature,
    }


def html(js):
    text1 = f""" <div class="container">
        <!-- header -->
        <div class="header__div">
          <div class="header__div-item">
            <h1>
              <strong class="header__div-item-label">??????????</strong>
            </h1>
          </div>
        </div>
        <!-- header end-->

        <!-- main -->
        <div class="main">
          <input type="button" onclick="openAccountNumber()" id="back-to-acc" value="??????????" style="display: none;">
          <div class="main__div">
            <div class="main__div-text-type">
              <h2 class="main__div-text">?????????????? ????????</h2>

            </div>
            <!-- ===== -->
            <div class="main__div-input-type">
              <input
                type="number"
                class="main__div-input"
                id="main__div-input"
              />
            </div>
            <!-- ===== -->
            <div class="main__div-button-type">
              <button class="main__div-button" onclick="getInfo()">
                ??????????????????
              </button>
            </div>
          </div>
          <!-- main__div end -->
          <div></div>

          <div class="result__div" id="result__div"></div>


          <div>
            <div id="cancel-payment-div"></div>
            <div style="display: flex; justify-content: space-evenly; margin-top: 70px;">
              <button id="cancel-payment" onclick="openInput()">????????????????</button>
              <button id="close-window" onclick="btnClose()">??????????????</button>
            </div>
          </div>

          <!-- <div>
            <button id="close-window" onclick="btnClose()">??????????????</button>
          </div> -->
        </div>
        <!-- main end-->
        <script>{js}{js_file2()}</script>

        <style>{css_text}</style>

      </div>
      <!-- container end -->
    """
    return text1
