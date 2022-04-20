$(function(){
    var loadForm = function(){
        var btn = $(this);
        $.ajax({
            url:btn.attr("data-url"),
            type:"GET",
            dataType:"JSON",
            beforeSend:function(){
                $("#modal-jurnal").modal("show");
            },
            success:function(data){
                $("#modal-jurnal .modal-content").html(data.html_form);
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
                if (data.form_is_valid){
                    alert("data action success!");
                    $("#table-jurnal tbody").html(data.html_jurnal_list);
                    $("#modal-jurnal").modal("hide");
                }
                else{
                    $("#modal-jurnal .modal-content").html(data.html_form);
                }
            },
        });
        return false;
    };

    $(".js-jurnal-create").click(loadForm);
    $("#modal-jurnal").on("submit",".js-jurnal-create-form",saveForm);
    $("#table-jurnal tbody").on("click",".js-jurnal-edit",loadForm);
    $("#modal-jurnal").on("submit",".js-jurnal-update-form",saveForm);
    $("#table-jurnal tbody").on("click",".js-jurnal-delete",loadForm);
    $("#modal-jurnal").on("submit",".js-jurnal-delete-form",saveForm);
});