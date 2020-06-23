$(function(){
    'use-strict';
    // Adjusts Slider height
    var winH = $(window).height(),
        navH = $('.navbar').innerHeight();
    $('.carousel-item img').height(winH-navH);
 


});

window.onscroll = function () {fixedFunc()}

var navbar = document.getElementById("main-navbar"),
    sticky = navbar.offsetTop;

function fixedFunc(){

    if (window.pageYOffset >= sticky){
        navbar.classList.add("fixed-top");
    } else {
        navbar.classList.remove("fixed-top");
    }
}

$(function () {
    $('.material-tooltip-main').tooltip({
      template: '<div class="tooltip md-tooltip"><div class="tooltip-arrow md-arrow"></div><div class="tooltip-inner md-inner"></div></div>'
    });
  })


window.onload = function (){
    const query = window.location.search.split('=')[1];
    const endpoint = '/api/product-list/' + query;

    $.ajax({
        method: 'GET',
        url: endpoint,
        success: function(data){
            for(n in data){
                item = data[n];
                let category = item.PRDcategory
                
                if(category === null){
                    category = '<br>';
                }
                
                let isTrend = '';
                let isNew = '';
                if(item.PRDisTrend){
                    isTrend = '<span class="badge badge-danger">trending</span>'
                }
                if(item.PRDisNew){
                    isNew = '<span class="badge badge-success">New</span>'
                }

                document.getElementById('items-row').innerHTML += `
                <div class="col-sm-12 col-md-4 col-lg-2 mt-3 column">
                <div class="card animated fadeIn">
                <a href="${item.url}">
                    <img class="card-img-top" src="${item.img}" alt="${item.PRDname}">
                </a>
                <div class="card-body">
                    <center><h5 class="grey-text">${category}</h5></center>
                    <center><a href="${item.url}"><h4 class="card-title">${item.PRDname}</h4></center></a>
                    
                        <center>
                        ${isTrend}
                        ${isNew}
                        </center>
                        
                    <center><h4 class="item-price"><strong>${item.PRDprice}</strong></h4></center>

                </div>
              </div>
              </div>`
            }

        },
        error: function(error){
            console.log(this.url);
            console.log(error)
        },
    });
};

function filter(filter){
    const query = window.location.search.split('=')[1];
    const endpoint = '/api/product-list/' + query;

    filter_id = filter+'-filter';

    filter = '?filter=' + filter

    document.getElementById('items-row').innerHTML = '';

    document.querySelector('.nav-link.active').classList.remove("active");

    document.getElementById(filter_id).classList.add("active");

    $.ajax({
        method: 'GET',
        url: endpoint + filter,
        success: function(data){
            for(n in data){
                item = data[n];
                
                let category = item.PRDcategory
                
                if(category === null){
                    category = '<br>';
                }

                let isTrend = '';
                let isNew = '';
                
                if(item.PRDisTrend){
                    isTrend = '<span class="badge badge-danger">trending</span>'
                }
                if(item.PRDisNew){
                    isNew = '<span class="badge badge-success">New</span>'
                }
                
                document.getElementById('items-row').innerHTML += `
                <div class="col-sm-12 col-md-4 col-lg-2 mt-3 colum">
                <div class="card animated fadeIn">
                <a href="${item.url}">
                    <img class="card-img-top" src="${item.img}" alt="${item.PRDname}">
                </a>
                <div class="card-body">
                    <center><h5 class="grey-text">${category}</h5></center>
                    <center><a href="${item.url}"><h4 class="card-title">${item.PRDname}</h4></center></a>
                    
                        <center>
                        ${isTrend}
                        ${isNew}
                        </center>
                        
                    <center><h4 class="item-price"><strong>${item.PRDprice}</strong></h4></center>

                </div>
                </div>
                </div>`
            }

        },
        error: function(error){
            console.log(this.url);
            console.log(error)
        },
    });
};

function trackResult(){
    input = document.querySelector('input[name=order_ref]');
    order_ref = input.value.trim();
    const endpoint = '/api/order-list/?order_ref=' + order_ref 
    //TODO:let token = 0

    $.ajax({
        method: 'GET',
        url: endpoint,
        success: function(data){
            order = data[0];
            tableDiv = document.getElementById('row-order-table');

            ordered_date = new Date(order.ordered_date).toLocaleString();
            tableDiv.innerHTML = '';
            tableDiv.innerHTML += `

                <div class="col-sm-12">
                    <table class="table table-bordered">
                        <thead class="thead-dark">
                            <tr class="text-uppercase">
                            <th class="font-weight-bold" scope="col">Ordered Date</th>
                            <th class="font-weight-bold" scope="col">Items</th>
                            <th class="font-weight-bold" scope="col">Total</th>
                            <th class="font-weight-bold" scope="col">Shipping Address</th>
                            <th class="font-weight-bold" scope="col">State</th>
                            <th id="cancel-order" class="font-weight-bold" scope="col">Cancel Order</th>
                            </tr>
                        </thead>
                        <tbody id="order-table-body">
                            <tr id="order-table-row">
                            <td class="font-weight-bold">${ordered_date}</td>
                                <td class="font-weight-bold">
                                    <ul id="order-items-list">
                                        
                                    </ul>
                                </td>
                                <td class="font-weight-bold">${order.total}</td>
                                <td class="font-weight-bold">
                                    ${order.shippingAddress.address2} 
                                <br>${(order.shippingAddress.street_address).slice(0,19)}
                                <br>${order.shippingAddress.zipCode}
                                <br>${order.shippingAddress.city}
                                </td>
                                <td id="order-state" class="text-uppercase font-weight-bold">
                                ${order.state}
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <br>
                    <br>
                    <br>
                    <br>
                    <br>
                    <br>
                </div>
                
                `;

            $('#cancel-order').hide();


            for (n in order.items){
                let orderitem = order.items[n];
                let item = orderitem.split("of",2);
                item = item[0] + ' of ' + item[1]
                document.getElementById('order-items-list').innerHTML += `<li>${item}</li>`
            };


            if (order.state === 'Delivered'){
                $('#order-state').addClass('text-success')

            }
            else if (order.state === 'Shipped'){
                $('#order-state').addClass('text-info')
            }
            else if (order.state === 'Processing'){
                $('#order-state').addClass('text-primary');
                $('#cancel-order').show()
                $('#order-table-row').append(`
                <td class="font-weight-bold">
                <a href="${order.cancel_url}">
                <h5><span class="badge badge-danger">Cancel</span></h5>
                </a>
                </td>
                `)
            }
        },
        error: function(error){

        }
    });
};