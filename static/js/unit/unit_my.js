$(function(){
    var loadForm = function(){
        var btn = $(this);
        $.ajax({
            url:btn.attr("data-url"),
            type:"GET",
            dataType:"JSON",
            beforeSend:function(){
                $("#modal-unit").modal("show");
            },
            success:function(data){
                $("#modal-unit .modal-content").html(data.html_form);
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
                    alert("data Success in action");
                    $("#table-unit tbody").html(data.html_unit_list);
                    $("#modal-unit").modal("hide");
                }
                else{
                    $("#modal-unit .modal-content").html(data.html_form);
                }
            },
        });
        return false;
    };

    $(".js-create-unit").click(loadForm);
    $("#modal-unit").on("submit",".js-unit-create-form",saveForm);
    $("#table-unit tbody").on("click",".js-update-unit",loadForm);
    $("#modal-unit").on("submit",".js-unit-update-form",saveForm);
    $("#table-unit tbody").on("click",".js-delete-unit",loadForm);
    $("#modal-unit").on("submit",".js-unit-delete-form",saveForm);
});
