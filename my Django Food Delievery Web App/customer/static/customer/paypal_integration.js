const CLIENT_ID = "AdF_iZDs4UXAo7WKaS5R66PC1VC4niy4HbRZ5jPGZwzX_GV2kVje9YMNW4Fv2Vo59dPJBG65NRW_u3oq"

const total = parseFloat(document.getElementById('total').innerText)
const pk = parseInt(document.getElementById('id').innerText)

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {

        const cookies = document.cookie.split(';');
        console.log('cookies ', cookies)

        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();

            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
        console.log('cookieValue ', cookieValue)
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');
console.log('csrftoken', csrftoken)

paypal.Button.render({
    // Configure environment
    env: 'sandbox',
    client: {
        sandbox: CLIENT_ID,
        production: 'demo_production_client_id'
    },
    // Customize button (optional)
    locale: 'en_US',
    style: {
        size: 'large',
        color: 'blue',
        shape: 'rect'
    },

    // Enable Pay Now checkout flow (optional)
    commit: true,

    // Set up a payment
    payment: function (data, actions) {
        console.log('payment created ', data)
        return actions.payment.create({
            transactions: [
                {
                    amount: {
                        total: "1",
                        currency: 'USD'
                    }
                }
            ]
        });
    },


    // Execute the payment
    onAuthorize: function (data, actions) {
        console.log('payment executed ')

        return actions.payment.execute().then(function () { // Show a confirmation message to the buyer
            alert('thankyou your payment is passesd')

            $.ajax({
                type: 'POST',
                url: "{% url 'order_confirmation' pk %}",
                beforeSend: function (request) {
                    request.setRequestHeader('X-CSRFToken', csrftoken)
                },
                data: JSON.stringify(
                    {'isPaid': true}
                ),
                success: function (data) {
                    window.location.href = '/payment_confirmation/'
                }
            })
        });
    }
}, '#paypal-button');
