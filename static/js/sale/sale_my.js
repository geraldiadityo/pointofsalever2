$(function(){
    var loadForm = function(){
        var btn = $(this);
        $.ajax({
            url:btn.attr("data-url"),
            type:"GET",
            dataType:"JSON",
            beforeSend:function(){
                $("#modal-sale").modal("show");
            },
            success:function(data){
                $("#modal-sale .modal-content").html(data.html_form);
            },
        });
    };
    $(".js-search-item").click(loadForm);
    $("#modal-sale").on("click",".js-dataitem-take",function(){
        var btn = $(this);
        var itemid = btn.attr("data-item");
        var barcode = btn.attr("data-barcode");
        var harga = btn.attr("data-harga");

        $("#product_id").val(itemid);
        $("#harga").val(harga);
        $("#barcode").val(barcode);
        $("#modal-sale").modal("hide");
    });

    $(".js-add-cart").click(function(){
        var itemid = $("#product_id").val();
        var harga = $("#harga").val();
        var qty = $("#qty").val();
        var btn = $(this);

        $.ajax({
            url:btn.attr("data-url"),
            type:"GET",
            data:{itemid:itemid,harga:harga,qty:qty},
            success:function(data){
                $("#table-keranjang tbody").html(data.html_keranjang_list);
                $("#id_totalharga").val(data.totalbyr);
                $("#id_discount").val(data.discount);
                $("#id_total_bayar").val(data.totalbyr);
                $("#grand_total").text(data.grand_total);
                $("#id_total_pendapatan").val(data.totaluntung);
                $("#barcode").val("");
                $("#itemid").val("");
                $("#harga").val("");
                $("#qty").val(1);
                $("#barocde").focus();
            },
        });
    });
    
    $("#barcode").keypress(function(e){
        var text_field = $(this);
        var barcode_value = $(this).val();
        keypressed = e.keyCode || e.which
        if (keypressed === 13){
            $.ajax({
                url:text_field.attr("data-url"),
                type:"GET",
                data:{barcode:barcode_value},
                success:function(data){
                    $("#product_id").val(data.product_id);
                    $("#harga").val(data.harga);
                },
            });
            e.preventDefault();
            return false;
        };
    });

    $("#id_cash").keypress(function(e){
        var form = $(this);
        var cash = $(this).val();
        var totalbyr = $("#id_total_bayar").val();
        var keypressed = e.keyCode || e.which
        
        if (keypressed === 13){
            $.ajax({
                url:form.attr("data-url"),
                type:"GET",
                data:{cash:cash,totalbyr:totalbyr},
                dataType:"JSON",
                success:function(data){
                    $("#id_kembalian").val(data.kembalian);
                },
            });
            e.preventDefault();
            return false;
        };
    });

    $("#table-keranjang tbody").on("click",".js-delete-isi-keranjang",function(){
        var btn = $(this);
        var keranjangid = btn.attr("data-id")
        $.ajax({
            url:btn.attr("data-url"),
            type:"GET",
            data:{keranjangid:keranjangid},
            success:function(data){
                $("#id_totalharga").val(data.totalbyr);
                $("#id_total_bayar").val(data.totalbyr);
                $("#id_total_pendapatan").val(data.total_untung);
                $("#grand_total").text(data.grand_total);
                $("#table-keranjang tbody").html(data.html_keranjang_list);

            },
        });
    });
});