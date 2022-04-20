$(function(){
    var loadTable = function(){
        var btn = $(this);
        var akun = btn.attr("data-id");
        var nama = btn.attr("data-nama");
        $.ajax({
            url:btn.attr("data-url"),
            type:"GET",
            data:{akun_id:akun,nama:nama},
            dataType:"JSON",
            success:function(data){
                $("#table-bukubesar tbody").html(data.html_bukubesar_list);
                $("#nama_akun").text(nama);
                $("#jenis_akun").text(data.kategori_akun);
            },
        });
    };

    $(".js-load-table").click(loadTable);
});