$(function(){
    var loadForm = function(){
        var btn = $(this);
        $.ajax({
            url:btn.attr("data-url"),
            type:"GET",
            dataType:"JSON",
            beforeSend:function(){
                $("#modal-akun").modal("show");
            },
            success:function(data){
                $("#modal-akun .modal-content").html(data.html_form);
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
                    $("#table-akun tbody").html(data.html_akun_list);
                    $("#modal-akun").modal("hide");
                }
                else{
                    $("#modal-akun .modal-content").html(data.html_form);
                }
            },
        });
        return false;
    };

    $(".js-akun-create").click(loadForm);
    $("#modal-akun").on("submit",".js-akun-create-form",saveForm);
    $("#table-akun tbody").on("click",".js-akun-edit",loadForm);
    $("#modal-akun").on("submit",".js-akun-update-form",saveForm);
    $("#table-akun tbody").on("click",".js-akun-delete",loadForm);
    $("#modal-akun").on("submit",".js-akun-delete-form",saveForm);
});