$(function(){
    var loadForm = function(){
        var btn = $(this);
        $.ajax({
            url:btn.attr("data-url"),
            type:"GET",
            dataType:"JSON",
            beforeSend:function(){
                $("#modal-create-stokout").modal("show");
            },
            success:function(data){
                $("#modal-create-stokout .modal-content").html(data.html_form);
            },
        });
    };
    $(".js-stokout-search").click(loadForm);
    $("#modal-create-stokout").on("click",".js-dataitem-take",function(){
        var btn = $(this);
        var item = btn.attr("data-item");
        var unit = btn.attr("data-unit");
        var stok = btn.attr("data-stok");
        var hargaawal = btn.attr("data-hargaawal");

        $("#id_product option[value="+item+"]").attr("selected","selected");
        $("#item_id").val(item);
        $("#unit").val(unit);
        $("#stok_awal").val(stok);
        $("#id_hargabeli").val(hargaawal);
        $("#modal-create-stokout").modal("hide");
        $("#id_qty").focus();
    });

    $("#id_product").change(function(){
        var field = $(this);
        var field_value = $(this).val();
        $.ajax({
            url:"/stok/selected-product-stokin/",
            type:"GET",
            data:{field_value:field_value},
            success:function(data){
                $("#item_id").val(data.itemid);
                $("#unit").val(data.unit);
                $("#stok_awal").val(data.stok_awal);

            },
        });
    });

    $("#id_qty").keypress(function(e){
        var hargabeli = $("#id_hargabeli").val();
        var qty = $(this).val();
        var keypressed = e.keyCode || e.which;
        if (keypressed === 13){
            $.ajax({
                url:"/stok/get_total/",
                type:"GET",
                data:{hargabeli:hargabeli,qty:qty},
                success:function(data){
                    $("#id_total").val(data.totalharga);
                    $("#id_detail").focus();
                }
            });
            e.preventDefault();
            return false;
        }
    });
});