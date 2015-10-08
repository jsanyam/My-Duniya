/**
 * Created by SANCHIT on 10/7/2015.
 */
        //storeArrayurl=new Array();
        var loading=true;
        storeArray= new Array();
        storeArraynews= new Array();
        storeArrayfullnews= new Array();
        bckgrnd = new Array();

        var frmn=0;
        var tlln=9;

        function loadnews(){
            var $article = $("#articles");
            var $name = $("#name");
            var $desc = $("#desc");
            var x = $(location).attr('href');
            console.log(x);
            var y=x.split('/');
            var l= y.length;
            console.log(y[l-1]);
            var z=y[l-1];
            console.log(z)
            $.ajax({
                type: 'GET',
                //url:"{{ url_for('.articles') }}",
                url:"/" + z,
                success: function(data, textStatus, xhr) {
                    console.log(data);
                    $.each(data['tag'], function(i, el){
                        console.log(el.title);
                        storeArraynews[i]=new Array(el.title, el.description,el.image,el.pubdate,el.category);
                    });
                    console.log("pahuche");
                    console.log(storeArraynews[0][4]);
                    $("#newstitle").append("<div>" +  storeArraynews[0][4] + "</div>");
                    for(j=frmn;j<tlln;j++){
                        console.log(frmn);
                        console.log(tlln);
                        $("<div />", { "class":"newsblock", id:"news"+j })
                         .append($("<div />", {  class:"n-img",id:"n-img"+j }))
                         .append($("<div />", {  class:"n-title",id:"n-title"+j }))
                         .append($("<div />", {  class:"n-pub",id:"n-pub"+j }))
                         .append($("<div />", {  class:"n-fullstory",id:"n-fullstory" }))
                         .appendTo("#newsdiv");

                        // $("#newsdiv").append("<div>",{ "class":"wrapper", id:"product"+i } "<div>" + storeArraynews[i][0] + "</div><div>" + storeArraynews[i][3] + "</div><div>" + storeArraynews[i][1] + "</div>");
                        $("#n-fullstory" + j).append("<div>" + storeArraynews[j][1] + "</div>");
                        $("#n-title" + j).append("<div>" + storeArraynews[j][0] + "</div>");
                        $("#n-pub" + j).append("<div>" + storeArraynews[j][3] + "</div>");
                        $("#n-img" + j).css('background-image','url(' + storeArraynews[j][2] + ')');


                    }
                    loading=false;
                    $(".loading").remove();
                },
                error: function(){
                    alert("error loading news");
                }
            });
        }






         /*   function loadNowPlaying(){
                 $("#now_playing").load("now_playing.php");
            }
            setInterval(function(){loadNowPlaying()},5000);
            $("#Add").click(function(){
                console.log("reached");
                var user = {
                    Name: $name.val(),
                    Desc: $desc.val()
                };
                console.log(user.Name);
                $.ajax({
                    type: 'POST',
                    url: "/news/",
                    data: user,
                    success: function(newUser){
                        //$article.append("<li>" + newUser.name + "</li><li>" + newUser.desc + "</li><b r><br>");
                        console.log(newUser.name, newUser.desc);
                    },
                    error: function(){
                        alert("error saving data");
                    }
                });
            });
           */
        $(function(){
            //loadslider();

            //loadtags();

            //load();
            //document.getElementById("newstag").style.visibility = "hidden";
            //$(".p-tags").click(function() {
              //   document.getElementById("newstag").style.visibility = "block";

//            });
            /*
            $("#live_buzz").scroll(function(){
                var curScroll = $(this)[0].scrollTop;
                var maxScroll = $(this)[0].scrollHeight- $(this).height();

                console.log(curScroll);
                console.log(maxScroll);
                console.log(loading);
                //console.log("yahaan pahuche2");
                if((curScroll >= maxScroll - 400) && loading == false){
                    loading = true;
                    frm=tll;
                    tll += 3;
                    //$("#live_buzz").append("<div class='.loading'>loading</div>");
                    $(this)[0].scrollTop = $(this)[0].scrollHeight- $(this).height();
                    //load();
                }
            });
               */
            loadnews();
           // loadfullnews();

            $("#newstag").scroll(function(){
                var curScroll = $(this)[0].scrollTop;
                var maxScroll = $(this)[0].scrollHeight- $(this).height();

                console.log(curScroll);
                console.log(maxScroll);
                console.log(loading);
                console.log("yahaan pahuche5");
                if((curScroll >= maxScroll - 400) && loading == false){
                    loading = true;
                    console.log("yahaan?")
                    frmn=tlln;
                    tlln += 9;
                    //$("#live_buzz").append("<div class='.loading'>loading</div>");
                    $(this)[0].scrollTop = $(this)[0].scrollHeight- $(this).height();
                    loadnews();
                }
            });

        });


