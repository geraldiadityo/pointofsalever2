$(function(){
    var loadForm = function(){
        var btn = $(this);
        $.ajax({
            url:btn.attr("data-url"),
            type:"GET",
            dataType:"JSON",
            beforeSend:function(){
                $("#modal-item").modal("show");
            },
            success:function(data){
                $("#modal-item .modal-content").html(data.html_form);
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
                    alert("data success in action");
                    $("#table-item tbody").html(data.html_item_list);
                    $("#modal-item").modal("hide");
                }
                else{
                    $("#modal-item .modal-content").html(data.html_form);
                }
            },
        });
        return false;
    };

    $(".js-create-item").click(loadForm);
    $("#modal-item").on("submit",".js-item-create-form",saveForm);
    $("#table-item tbody").on("click",".js-update-item",loadForm);
    $("#modal-item").on("submit",".js-item-update-form",saveForm);
    $("#table-item tbody").on("click",".js-delete-item",loadForm);
    $("#modal-item").on("submit",".js-item-delete-form",saveForm);
    $("#table-item tbody").on("click",".js-view-item",loadForm);
});