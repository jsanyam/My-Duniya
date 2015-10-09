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
            console.log(x)
            var y=x.split('/');
            var l= y.length;
            console.log(y[l-2])

            $.ajax({
                type: 'GET',
                //url:"{{ url_for('.articles') }}",
                url:"/"+y[l-1],
                success: function(data, textStatus, xhr) {
                    console.log(data);
                    $.each(data['tag'], function(i, el){
                        console.log(el.title);
                        storeArraynews[i]=new Array(el.title, el.description,el.image,el.pubdate,el.id, el.category);
                    });
                    console.log("pahuche")

                    for(j=frmn;j<tlln;j++){
                        console.log(frmn)
                        console.log(tlln)
                        $("<div />", { "class":"newsblock", id:"news"+j })
                         .append($("<a />", {  class:"n-a",id:"n-img-a"+j }))
                         .append($("<a />", {  class:"n-a",id:"n-title"+j }))
                         .append($("<div />", {  class:"n-pub",id:"n-pub"+j }))
                         .appendTo("#newsdiv");

                        // $("#newsdiv").append("<div>",{ "class":"wrapper", id:"product"+i } "<div>" + storeArraynews[i][0] + "</div><div>" + storeArraynews[i][3] + "</div><div>" + storeArraynews[i][1] + "</div>");
                        $("#newstitle").append("<div>" + storeArraynews[j][5] + "</div>");
                        $("#n-fullstory" + j).append("<div>" + storeArraynews[j][1] + "</div>");
                        $("#n-img-a" + j).append($("<img />", {  class:"n-img",id:"n-img"+j }));
                        $("#n-title" + j).append("<div>" + storeArraynews[j][0] + "</div>");
                        $("#n-pub" + j).append("<div>" + storeArraynews[j][3] + "</div>");
                        $("#n-img" + j).attr('src' , storeArraynews[j][2]);
               //         $("#n-img-a" + j).prop("href" , "/fullnews/" + storeArraynews[j][4]);
                        console.log($("#n-img-a"+j).attr('href') )
                        var y=storeArraynews[j][2];

                        $(".n-a").attr('href','/full_news/'+storeArraynews[j][4]);

                        if(y=="http://timesofindia.indiatimes.com/photo/7787613.cms"){

                             $("#n-img" + j).attr('src','../static/img/pasaulis1.jpg');
                        }


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
            //document.getElementById("content").style.visibility = "hidden";
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


