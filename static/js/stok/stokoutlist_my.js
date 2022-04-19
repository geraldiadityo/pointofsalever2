$(function(){
    var loadForm = function(){
        var btn = $(this);
        $.ajax({
            url:btn.attr("data-url"),
            type:"GET",
            dataType:"JSON",
            beforeSend:function(){
                $("#modal-stokout").modal("show");
            },
            success:function(data){
                $("#modal-stokout .modal-content").html(data.html_form);
            },
        });
    };

    var saveForm = function(){
        var form = $(this);
        $.ajax({
            url:form.attr("action"),
            type:form.attr("method"),
            data:form.serialize(),
            dataType:"JSON",
            success:function(data){
                if(data.form_is_valid){
                    alert("data action success");
                    $("#table-stokout tbody").html(data.html_stok_list);
                    $("#modal-stokout").modal("hide");
                }
                else{
                    $("#modal-stokout .modal-content").html(data.html_form);
                }
            },
        });
        return false;
    };

    $("#table-stokout tbody").on("click",".js-view-detail-stokout",loadForm);
    $("#table-stokout tbody").on("click",".js-delete-stokout",loadForm);
    $("#modal-stokout").on("submit",".js-stok-delete-form",saveForm);
})