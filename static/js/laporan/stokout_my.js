$(function(){
    var loadLaporan = function(){
        var selected = $(this);
        var value = selected.val();
        $.ajax({
            url:"/laporan/stok-reporting-date/out/",
            type:"GET",
            data:{value:value},
            success:function(data){
                $("#table-stokout tbody").html(data.html_stok_list);
                $("#view_report").attr("href","/laporan/stok-view-reporting-date/out/"+value+"/");
                $("#download_report").attr("href","/laporan/stok-download-reporting-date/out/"+value+"/");
            },
        });
    };

    $("#tanggalselect").change(loadLaporan);
    $("#bulanselect").change(loadLaporan);
    $("#tahunselect").change(loadLaporan);
});