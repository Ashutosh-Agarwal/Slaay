from authorizenet import apicontractsv1
from authorizenet.apicontrollers import*
from decimal import*
from credential import * 

def payment(name,key,card_number,expiration_date,amount,merchant_id):
       merchantAuth = apicontractsv1.merchantAuthenticationType()
       merchantAuth.name = name
       merchantAuth.transactionKey = key
        
       creditCard = apicontractsv1.creditCardType()
       creditCard.cardNumber = card_number
       creditCard.expirationDate = expiration_date
        
       payment = apicontractsv1.paymentType()
       payment.creditCard = creditCard
        
       transactionrequest = apicontractsv1.transactionRequestType()
       transactionrequest.transactionType ="authCaptureTransaction"
       transactionrequest.amount = Decimal (amount)
       transactionrequest.payment = payment
        
        
       createtransactionrequest = apicontractsv1.createTransactionRequest()
       createtransactionrequest.merchantAuthentication = merchantAuth
       createtransactionrequest.refId = merchant_id
        
       createtransactionrequest.transactionRequest = transactionrequest
       createtransactioncontroller = createTransactionController(createtransactionrequest)
       createtransactioncontroller.execute()
        
       response = createtransactioncontroller.getresponse()
        
       if (response.messages.resultCode=="Ok"):
              return response.transactionResponse.transId
              print("Transaction ID : %s"% response.transactionResponse.transId)
       else:
              return response.messages.resultCode
              print("response code: %s"% response.messages.resultCode)

if __name__ == '__main__':
       trans =payment(name,key,"4111111111111111", "2020-12", '10.55', "MerchantID-0001")
       print(trans)
