const $btnPrint = document.querySelector("#btnPrint");
const $btnSelesai = document.querySelector("#btnSelesai");
$btnPrint.addEventListener("click", () => {
    window.print();
});

$btnSelesai.addEventListener("click", () => {
    window.location="/sale/delete-all-item-keranjang/";
});