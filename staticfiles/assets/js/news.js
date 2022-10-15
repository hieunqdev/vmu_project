var a_list = document.getElementsByClassName("show");
for (var i = 0; i < a_list.length; i++){
    a_list[i].onclick = function(){
        alert('Vui lòng đăng nhập để xem chi tiết thông báo');
        return false;
    }
};