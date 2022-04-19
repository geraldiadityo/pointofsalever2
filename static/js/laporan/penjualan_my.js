$(function(){
    var loadLaporan = function(){
        var selected = $(this);
        var value = selected.val();
        $.ajax({
            url:'/laporan/sale-reporting-date/',
            type:'GET',
            data:{value:value},
            success:function(data){
                $("#table-sale tbody").html(data.html_sale_list);
                $("#view-report").attr("href","/laporan/sale-view-reporting-date/"+value+"/");
                $("#cetak-report").attr("href","/laporan/sale-download-reporting-date/"+value+"/");
            },
        });
    };

    $("#tanggalselect").change(loadLaporan);
    $("#bulanselect").change(loadLaporan);
    $("#tahunselect").change(loadLaporan);
});