function Auth() {

}

Auth.prototype.listenloginbtnclickevent = function(){
    $(".btn").click(function (e) {
    //window.location.reload()
    })
};

Auth.prototype.run = function(){
this.listenloginbtnclickevent();

};

$(function () {
    var auth = new Auth();
    auth.run();
});

window.delay = new Auth();