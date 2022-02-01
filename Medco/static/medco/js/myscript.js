$(".plus-cart").click(function() {
    var id =$(this).attr("pid").toString();
    var eml=this.parentNode.children[2]
    
    $.ajax({
        type:"GET",
        url:"/plus_cart",
        data:{
            prod_id:id
        },
        success:function(data) {
            eml.innerText = data.quantity
            document.getElementById("totalammount").innerText = data.totalamount
            document.getElementById("totalammount_l").innerText = data.totalamount
            
            
        }
    })
})

$(".minus-cart").click(function() {
    var id =$(this).attr("pid").toString();
    var eml=this.parentNode.children[2]
    
    $.ajax({
        type:"GET",
        url:"/minus_cart",
        data:{
            prod_id:id
        },
        success:function(data) {
            eml.innerText = data.quantity
            document.getElementById("totalammount").innerText = data.totalamount
            document.getElementById("totalammount_l").innerText = data.totalamount
            
            
        }
    })
})


$(".remove-cart").click(function() {
    var id =$(this).attr("pid").toString();
    var eml=this
    
    $.ajax({
        type:"GET",
        url:"/remove_cart",
        data:{
            prod_id:id
        },
        success:function(data) {
            
            document.getElementById("totalammount").innerText = data.totalamount
            document.getElementById("totalammount_l").innerText = data.totalamount
            eml.parentNode.parentNode.parentNode.parentNode.remove()
            
            
        }
    })
})