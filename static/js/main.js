
        var loading=true;
        storeArray= new Array();
        storeArraynews= new Array();
        storeArrayfullnews= new Array();
        bckgrnd = new Array();
        var frm=0;
        var tll=3;
        var frmn=0;
        var tlln=9;
        function load(){
            var $article = $("#articles");
            var $name = $("#name");
            var $desc = $("#desc");

            $.ajax({
                type: 'GET',
                //url:"{{ url_for('.articles') }}",
                url:"/World",
                success: function(data, textStatus, xhr) {
                    console.log(data);
                    $.each(data['tag'], function(i, el){

                        storeArray[i]=new Array(el.title, el.full_story,el.image);
                    });

                    for(i=frm;i<tll;i++){
                        //console.log(storeArray[i][0])
                        //console.log(storeArray[i][1])
                        //$("#live_buzz").append("<div>" + storeArray[i][0] + "</div>");
                        //$("#live_buzz").append("<div>" + storeArray[i][1] + "</div>");
                        //$("#live_buzz").css('background-image','url(' + storeArray[i][2] + ')');
                    }
                    loading=false;
                    $(".loading").remove();
                },
                error: function(){
                    alert("error loading news");
                }
            });
        }
        function loadnews(){
            var $article = $("#articles");
            var $name = $("#name");
            var $desc = $("#desc");

            $.ajax({
                type: 'GET',
                //url:"{{ url_for('.articles') }}",
                url:"/World",
                success: function(data, textStatus, xhr) {
                    console.log(data);
                    $.each(data['tag'], function(i, el){

                        storeArraynews[i]=new Array(el.title, el.description,el.image,el.pubdate);
                    });

                    for(j=0;j<20;j++){
                        //console.log(storeArray[i][0])
                        //console.log(storeArray[i][1])
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



        function loadfullnews(){
            var $article = $("#articles");
            var $name = $("#name");
            var $desc = $("#desc");
            array=new Array();

            $.ajax({
                type: 'GET',

                //url:"{{ url_for('.articles') }}",
                url:"/news.json/155",
                success: function(data, textStatus, xhr) {

                    console.log("reached somw where")
                    $.each(data['article'], function (i, el) {
                            array=new Array(el.category,el.image,el.title,el.pubdate,el.full_story);
                            $("<div />", { "class":"fullnews", id:"newsdiv"})
                         .append($("<div />", {  class:"fn-category",id:"fn-category" }))
                         .append($("<div />", {  class:"fn-img",id:"fn-img" }))
                         .append($("<div />", {  class:"fn-title",id:"fn-title" }))
                         .append($("<div />", {  class:"fn-pub",id:"fn-pub" }))
                         .append($("<div />", {  class:"fn-fullstory",id:"fn-fullstory"}))
                         .appendTo("#fullnews");
                    });

                    $("#fn-category").append("<div>" + array[0][0]+ "</div>");
                        $("#fn-img").css('background-image', 'url(' + array[0][1] + ')');
                        $("#fn-title").append("<div>" + array[0][2] + "</div>");
                        $("#fn-pub").append("<div>" + array[0][3] + "</div>");
                        $("#fn-fullstory").append("<div>" + array[0][4] + "</div>");
                    //console.log(storeArray[i][0])
                    //console.log(storeArray[i][1])

                },

                error: function(){
                    alert("error loading news");
                }
            });
        }


        function loadslider() {

            $.ajax({
                type: 'GET',
                //url:"{{ url_for('.articles') }}",
                url:"/news.json",
                success: function(data, textStatus, xhr) {
                    console.log(data);
                    $.each(data['articles'], function(i, el){
                        $("#t" + i).append( el.title );
                        $("#c" + i).append(  el.description );
                        $("#img" + i).attr('src',el.image);
                       var y=el.image;

                        if(y=="http://timesofindia.indiatimes.com/photo/7787613.cms"){

                             $("#img" + i).attr('src','../static/img/pasaulis1.jpg');
                        }
                    });

                },
                error: function(){
                    alert("error loading news");
                }
            });
        }


        function loadtags() {
            var t=0;
            for(j=1;j<=5;j++){
                var article = $("#pt" + j + "info").text();

                console.log(article)
                $.ajax({
                    type: 'GET',
                    //url:"{{ url_for('.articles') }}",
                    url:"/" + article ,
                   // url:"/World",
                    //url:"/news.json",

                    success: function(data, textStatus, xhr) {
                        $.each(data['tag'], function(i, el){
                                bckgrnd[i] = el.image;
                                console.log(bckgrnd[i])
                                console.log(el.image)

                        });
                        t=t+1;
                        console.log(t)
                        $("#live_buzz").css('background-image','url(' + bckgrnd[t] + ')');
                        $("#pt" + t).css('background-image','url(' + bckgrnd[t] + ')');
                        var y=$("#pt" + t).css('background-image');
                        if(y=="http://timesofindia.indiatimes.com/photo/7787613.cms"){
                            $("#pt" + t).css('background-image','url(../static/img/pasaulis1.jpg)');
                        }
                    },
                    error: function(){
                        alert("error loading news");
                    }
                });
            }
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
            loadslider();

            loadtags();

            load();
           // document.getElementById("content").style.visibility = "hidden";
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
            //loadnews();
            //loadfullnews();
            console.log("yahaan pahuche?")
            $("#newstag").scroll(function(){
                var curScroll = $(this)[0].scrollTop;
                var maxScroll = $(this)[0].scrollHeight- $(this).height();

                console.log(curScroll);
                console.log(maxScroll);
                console.log(loading);
                console.log("yahaan pahuche5");
                if((curScroll >= maxScroll - 400) && loading == false){
                    loading = true;
                    frmn=tlln;
                    tlln += 9;
                    //$("#live_buzz").append("<div class='.loading'>loading</div>");
                    $(this)[0].scrollTop = $(this)[0].scrollHeight- $(this).height();
                    loadnews();
                }
            });
                $('#w-forecast').hover(function(){alert("coming in phase two")});
                $('#w-title').hover(function(){alert("coming in phase two")});
               $('#pt1').hover(function(){

                  $('#pt1info').css('background-color','white');
                  $('#pt1info').css('border-color','black');
                  $('#pt1info').css('color','black');

               },

                function(){
                    $('#pt1info').css('background-color','transparent');
                     $('#pt1info').css('border-color','white');
                      $('#pt1info').css('color','white');

                });
                $('#pt2').hover(function(){

                  $('#pt2info').css('background-color','white');
                  $('#pt2info').css('border-color','black');
                  $('#pt2info').css('color','black');

               },

                function(){
                    $('#pt2info').css('background-color','transparent');
                     $('#pt2info').css('border-color','white');
                      $('#pt2info').css('color','white');

                });
                $('#pt3').hover(function(){

                  $('#pt3info').css('background-color','white');
                  $('#pt3info').css('border-color','black');
                  $('#pt3info').css('color','black');

               },

                function(){
                    $('#pt3info').css('background-color','transparent');
                     $('#pt3info').css('border-color','white');
                      $('#pt3info').css('color','white');

                });
                $('#pt4').hover(function(){

                  $('#pt4info').css('background-color','white');
                  $('#pt4info').css('border-color','black');
                  $('#pt4info').css('color','black');

               },

                function(){
                    $('#pt4info').css('background-color','transparent');
                     $('#pt4info').css('border-color','white');
                      $('#pt4info').css('color','white');

                });

        });


