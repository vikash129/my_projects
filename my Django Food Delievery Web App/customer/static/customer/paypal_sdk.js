
paypal.Buttons({
    style: {
      layout: 'vertical',
      color:  'blue',
      shape:  'rect',
      label:  'paypal'
    } 
    , 
    createOrder: function(data, actions) {
      console.log('created order' , data)
        return actions.order.create({
          purchase_units: [{
            amount: {
              value: 1
            }
          }]
        });
      }
      ,
    onApprove: function(data, actions) {
      console.log('onapprove order' , data)
  
      return actions.order.capture().then(function(details) {
        alert('Transaction completed by ' + details.payer.name.given_name);
      });
    }
    ,
    onCancel: function (data) {
      // Show a cancel page, or return to cart
      console.log('cancel ' , data)
    }
    ,
    onError: function (err) {
      // For example, redirect to a specific error page
      console.log('error ' , err)
  
      window.location.href = "/";
    }
  
  }).render('#paypal-button-container');
  
  