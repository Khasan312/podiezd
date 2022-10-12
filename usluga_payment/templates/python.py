css = """
   /* ALL */
*, *::after, *::before{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* ALL END  */

/* CONTAINER */

.container{
  width: 750px;
  margin: 100px auto;

  font-family: 'Roboto Condensed', sans-serif;
}

/* CONTAINER END */

/* HEADER */

.header__div{
  background-color: #f5f5f5;
  border: 1px solid #ddd;
  border-radius: 6px 6px 0 0;
}

.header__div-item-label{
  font-size: 18px;
  font-weight: 700;
  margin: 0 0 2px 35px;

}

.main__div-text{
  font-size: 18px;
}

/* HEADER END */


/* MAIN */

.main{
  width: 750px;
  min-height: 210px;
  background-color: #f5f5f5;
  border: 1px solid #ddd;
  border-radius: 0 0 6px 6px;
}

.main__div{
  margin: 15px 0px 0px 35px;
  display: flex;
  flex-wrap: wrap


}

.main__div-text{
  margin-top: 1px;
}

.main__div-input-type{
  margin-left: 40px;
  margin-top: 0px;
}

.main__div-input{
  width: 200px;
  height: 30px;
  border: 1px solid #ddd;
  border-radius: 6px;
  padding: 5px;
}

.main__div-input:focus{
  box-shadow: 1px 1px 10px #008000;
}

.main__div-button-type{
  margin: 2px 0px 0px 40px;
}

.main__div-button{
  width: 95px;
  height: 28px;
  border-radius: 6px;
  border: 1px solid #ddd;
  
}

.main__div-button:hover{
  background-color:bisque;
}
.main__div-button:active{
  background-color: #fff;
}

.result__from-js{
 
  width: 75%;
  margin: 20px 0;
  line-height: 2;
  display: flex;
  justify-content: space-around;
}

.result__from-js__button{
  width: 95px;
  height: 28px;
  border-radius: 6px;
  border: 1px solid #ddd;
}

.result__from-js__button:hover{
  background-color:bisque;
}
.result__from-js__button:active{
  background-color: #fff;
}

.result__from-js-input-sum{
  width: 130px;
  height: 30px;
  border: 1px solid #ddd;
  border-radius: 6px;
  padding: 5px;
  
  
}

.result__from-js-input-sum:focus{
  box-shadow: 1px 1px 10px #008000;
}

/* MAIN end */
/* FOOTER start */

.footer{
  flex-wrap: wrap;
  justify-content: center;
  bottom:0;
  display: flex;
  margin-top: 100px;
  margin-bottom: 5px;
}

.footer__url{
  width: 105px;
  height: 30px;
  border-radius: 6px;
  border: 1px solid #ddd;
}

.footer__url:hover{
  background-color:bisque;
}

.footer__url:active{
  background-color: #fff;
}

.footer__pay{
  margin-right: 25px;
}

.footer__close{
  margin-left: 25px;
}


/* FOOTER end */

/* RESULT START */


.result__button-pay{
  margin-top: 13vh;
}

/* RESULT END */


"""


def js_file(
    cashregisterId,
    kioskId,
    receiptId,
    productCode,
    partnerId,
    userName,
    time,
    signature,
):
    text = """ var input = document.getElementById("main__div-input");
        var resultDiv = document.getElementById("result__div");
        var accountNumber;
    


        function btnClose () {
        
        window.close();
        };

        function paymentFormHTML(clientName) {
          var text =  '<div class="result__from-js">'+
                  "<div>" +
                  "<div>" +
                  "<strong>"+
                  "Абонент:</strong> " + 
                  clientName + 
                  "</div>"+
                  '<div style="display: flex;">'+  
                  '<div>'+
                  'Сумма платежа'+
                  '</div>'+
                  '<div style="margin-left: 20px;">'+
                  '<input type"number" class="result__from-js-input-sum" id="amount-id"> сом.'  +
                  '</div>'+
                  '</div>'+ 
                  '</div>'+ 
                  '<div>'+
                  '<button onclick="but()" class="result__from-js__button">Оплатить</button>'+
                  '</div>' +
                  '</div>"';
            return text;
        };
        """
    text2 = f"""
        var urlCheckAccount = 'http://192.168.3.190:8000/api/check-account/?cashregister_id={cashregisterId}&kiosk_id={kioskId}&receipt_id={receiptId}&productcode={productCode}&partner_id={partnerId}&user_name={userName}&time={time}&signature={signature}";';
        var urlpayAccount = 'http://192.168.3.190:8000/api/make-payment';
        """
    text3 = """
        var xhr = new XMLHttpRequest();

        function getInfo() {
            // console.log(checkAccountInput.value);
            var inputNumber = input.value;
            console.log(inputNumber + " getCheck inputNumber");
            var jsonIdStudent = JSON.stringify({
                account_number: inputNumber
            });
            xhr.open("POST", urlCheckAccount);
            xhr.setRequestHeader("Content-Type", "application/json");
            xhr.send(jsonIdStudent);
            console.log(jsonIdStudent)
            // тело ответа 
            xhr.onload = function () {
                var responseObj = JSON.parse(xhr.response);
                resultDiv.innerHTML = "XHR";
                console.log(responseObj["message"]);
                resultDiv.innerHTML = paymentFormHTML(responseObj.message);
            };
            // checkAccountInput.value = "";
        };


        function but() {
          var input_amount = document.getElementById("amount-id");

          var body_data = JSON.stringify({
            account_number: input.value,
            amount: parseInt(input_amount.value)
          });

          console.log(body_data);

          if (input_amount.value <= 0) {
            resultDiv.innerHTML += '<h4 style="color: red; text-align:center;">Введите сумму больше чем ноль</h4>';
          } else {
            xhr.open('POST', urlpayAccount);
            xhr.setRequestHeader("Content-Type", "application/json");
            xhr.send(body_data);
            xhr.onload = function () {
              var responseObjpay = JSON.parse(xhr.response);
              console.log(responseObjpay);
              if (responseObjpay.success === true) {
                input_amount.value = "";
                resultDiv.innerHTML += '<h4 style="text-align:center;">' + responseObjpay.message + '</h4>';
                window.close();
              } else {
                resultDiv.innerHTML += '<h5 style="text-align:center;>Оплата не прошла</h5>';
              }
            };
          };
        };"""
    fullText = text + text2 + text3
    return fullText


def html(jsParams):
    html_ = f""" <div class="container">
  <style>{css}</style>
  <!-- header -->
  <div class="header__div">

    <div class="header__div-item">
      <h1>
        <strong class="header__div-item-label">Уборка подъездов</strong>
      </h1>
    </div>

  </div>
  <!-- header end-->

  <!-- main -->
  <div class="main">
    <div class="main__div">
      <div class="main__div-text-type">
        <h2 class="main__div-text">Введите код</h2>
      </div>
      <!-- ===== -->
      <div class="main__div-input-type">
        <input type="number" class="main__div-input" id="main__div-input">
      </div>
      <!-- ===== -->
      <div class="main__div-button-type">
        <button class="main__div-button" onclick="getInfo()">Проверить</button>
      </div>
    </div>
    <!-- main__div end -->
    <div>

    </div>

    <div class="result__div" id="result__div">
    
    </div>


  </div> <!-- main end-->
  <div class="footer">
    <div>
      <!-- <a href="#" class="footer__pay footer__url">Оплата</a> -->
      <button onclick="" class="footer__pay footer__url">Оплата</button>
    </div>
    <div>
      <!-- <a href="#" class="footer__cancel footer__url">Отмена</a> -->
      <button onclick="" class="footer__cancel footer__url">Отмена</button>
    </div>

    <div>
      <!-- <a href="#" class="footer__close footer__url">Отмена</a> -->
      <button onclick="btnClose()" class="footer__close footer__url">Закрыть</button>
    </div>
   
  </div>
  <hr/>
  <script>{jsParams}</script>
</div> <!-- container end -->"""

    return html_
