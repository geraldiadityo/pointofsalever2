$(function(){
    var loadForm = function(){
        var btn = $(this);
        $.ajax({
            url:btn.attr("data-url"),
            type:"GET",
            dataType:"JSON",
            beforeSend:function(){
                $("#modal-create-stokin").modal("show");
            },
            success:function(data){
                $("#modal-create-stokin .modal-content").html(data.html_form);
            },
        });
    };
    $(".js-search-item").click(loadForm);
    $("#modal-create-stokin").on("click",".js-dataitem-take",function(){
        var btn = $(this);
        var item = btn.attr("data-item");
        var unit = btn.attr("data-unit");
        var stokawal = btn.attr("data-stok");

        $("#id_product option[value="+item+"]").attr("selected","selected");
        $("#item_id").val(item);
        $("#unit").val(unit);
        $("#stok_awal").val(stokawal);
        $("#modal-create-stokin").modal("hide");
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
                },
            });
            e.preventDefault();
            return false;
        };
    });
});