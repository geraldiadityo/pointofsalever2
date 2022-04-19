$(function(){
    var loadForm = function(){
        var btn = $(this);
        $.ajax({
            url:btn.attr("data-url"),
            type:"GET",
            dataType:"JSON",
            beforeSend:function(){
                $('#modal-supplier').modal('show');
            },
            success:function(data){
                $('#modal-supplier .modal-content').html(data.html_form);
            }
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
                    alert("data success sender");
                    $('#table-supplier tbody').html(data.html_supplier_list);
                    $('#modal-supplier').modal("hide");
                }
                else{
                    $('#modal-supplier .modal-content').html(data.html_form);
                }
            }
        });
        return false
    };

    $(".js-create-supplier").click(loadForm);
    $("#modal-supplier").on("submit",".js-supplier-create-form",saveForm);
    $("#table-supplier tbody").on("click",".js-update-supplier",loadForm);
    $("#modal-supplier").on("submit",".js-supplier-update-form",saveForm);
    $("#table-supplier tbody").on("click",".js-delete-supplier",loadForm);
    $("#modal-supplier").on("submit",".js-supplier-delete-form",saveForm);
    
});