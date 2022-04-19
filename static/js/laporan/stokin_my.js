$(function(){
    var loadLaporan = function(){
        var selected = $(this);
        var value  = selected.val();
        $.ajax({
            url:"/laporan/stok-reporting-date/in/",
            type:"GET",
            data:{value:value},
            success:function(data){
                $("#table-stokin tbody").html(data.html_stok_list);
                $("#view_report").attr("href","/laporan/stok-view-reporting-date/in/"+value+"/");
                $("#download_report").attr("href","/laporan/stok-download-reporting-date/in/"+value+"/");
            },
        });
    };


    $("#tanggalselect").change(loadLaporan);
    $("#bulanselect").change(loadLaporan);
    $("#tahunselect").change(loadLaporan);

});