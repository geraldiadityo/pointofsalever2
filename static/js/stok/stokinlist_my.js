$(function(){
    var loadForm = function(){
        var btn = $(this);
        $.ajax({
            url:btn.attr("data-url"),
            type:"GET",
            dataType:"JSON",
            beforeSend:function(){
                $("#modal-stokin").modal("show");
            },
            success:function(data){
                $("#modal-stokin .modal-content").html(data.html_form);
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
                    alert("data Action Success");
                    $("#table-stokin tbody").html(data.html_stokin_list);
                    $("#modal-stokin").modal("hide");
                }
                else{
                    $("#modal-stokin .modal-content").html(data.html_form);
                }
            },
        });
        return false;
    };

    $("#table-stokin tbody").on("click",".js-view-detail-stokin",loadForm);
    $("#table-stokin tbody").on("click",".js-delete-stokin",loadForm);
    $("#modal-stokin").on("submit",".js-stokin-delete-form",saveForm);
});
