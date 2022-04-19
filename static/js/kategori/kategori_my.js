$(function(){
    var loadForm = function(){
        var btn = $(this);
        $.ajax({
            url:btn.attr("data-url"),
            type:"GET",
            dataType:"JSON",
            beforeSend:function(){
                $("#modal-kategori").modal("show");
            },
            success:function(data){
                $("#modal-kategori .modal-content").html(data.html_form);
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
                    alert("data success Sender");
                    $("#table-kategori tbody").html(data.html_kategori_list);
                    $("#modal-kategori").modal("hide");
                }
                else{
                    $("#modal-kategori .modal-content").html(data.html_form);
                }
            },
        });
        return false;
    };
    $(".js-create-kategori").click(loadForm);
    $("#modal-kategori").on("submit",".js-kategori-create-form",saveForm);
    $("#table-kategori tbody").on("click",".js-update-kategori",loadForm);
    $("#modal-kategori").on("submit",".js-kategori-update-form",saveForm);
    $("#table-kategori tbody").on("click",".js-delete-kategori",loadForm);
    $("#modal-kategori").on("submit",".js-kategori-delete-form",saveForm);


});